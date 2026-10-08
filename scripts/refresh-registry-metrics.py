#!/usr/bin/env python3
"""Recount official registries, then render/validate the profile (does not publish).

The milestone basis is npm events since 2025-10-01 plus cumulative crates.io
counts. The separate rolling-year window ends at the last positive cohort day,
not at an unreported all-zero API day. Requires Python 3 and Node.js.
"""
import concurrent.futures
import datetime as dt
import email.utils
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
PERIOD_START = '2025-10-01'
HEADERS = {
    'Accept': 'application/json',
    'User-Agent': 'ruvnet-profile-registry-audit/1.0 (+https://github.com/ruvnet/ruvnet)',
}


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z')


def fetch_json(url):
    """Bounded retries; respect rate limits and fail before changing published data."""
    for attempt in range(8):
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read()
            return json.loads(raw), {
                'source': url,
                'retrieved_at': stamp(),
                'response_sha256': hashlib.sha256(raw).hexdigest(),
            }
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == 7:
                raise
            retry_after = error.headers.get('Retry-After', '10')
            try:
                delay = float(retry_after)
            except ValueError:
                delay = (email.utils.parsedate_to_datetime(retry_after)
                         - dt.datetime.now(dt.timezone.utc)).total_seconds()
            time.sleep(max(10, delay, 2 * (attempt + 1)))
        except (TimeoutError, urllib.error.URLError):
            if attempt == 7:
                raise
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f'Unable to retrieve {url}')


def npm_inventory():
    packages = set()
    responses = []
    offset = 0
    while True:
        url = ('https://registry.npmjs.org/-/v1/search?'
               f'text=maintainer%3Aruvnet&size=250&from={offset}')
        body, receipt = fetch_json(url)
        responses.append(receipt)
        rows = body['objects']
        for item in rows:
            package = item['package']
            if any(m.get('username', m.get('name')) == 'ruvnet'
                   for m in package.get('maintainers', [])):
                packages.add(package['name'])
        offset += len(rows)
        if offset >= body['total']:
            break
        if not rows:
            raise ValueError('npm inventory ended before its declared total')
    if len(packages) < 300:
        raise ValueError(f'Unexpectedly low npm inventory: {len(packages)}')
    return sorted(packages), responses


def crate_inventory():
    crates, responses = [], []
    page = 1
    while True:
        url = f'https://crates.io/api/v1/crates?page={page}&per_page=100&user_id=339999'
        body, receipt = fetch_json(url)
        responses.append(receipt)
        rows = body['crates']
        crates.extend({'id': row['id'], 'downloads': row['downloads']} for row in rows)
        if len(crates) >= body['meta']['total']:
            break
        if not rows:
            raise ValueError('crates.io inventory ended before its declared total')
        page += 1
        time.sleep(1.1)
    if len(crates) < 300 or len({row['id'] for row in crates}) != len(crates):
        raise ValueError('Unexpectedly low or duplicate crate inventory')
    if any(type(row['downloads']) is not int or row['downloads'] < 0 for row in crates):
        raise ValueError('Invalid crate download count')
    return sorted(crates, key=lambda row: row['id']), responses


def validate_range(package, body, start, end):
    if (body.get('package'), body.get('start'), body.get('end')) != (package, start, end):
        raise ValueError(f'Wrong package or date range for {package}')
    points = body.get('downloads')
    expected_days = (dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days + 1
    if not isinstance(points, list) or len(points) != expected_days:
        raise ValueError(f'Incomplete daily range for {package}')
    first = dt.date.fromisoformat(start)
    for index, point in enumerate(points):
        expected = (first + dt.timedelta(days=index)).isoformat()
        if (point.get('day') != expected or type(point.get('downloads')) is not int
                or point['downloads'] < 0):
            raise ValueError(f'Invalid or missing daily observation for {package}')
    return points


def summarize_ranges(results, start, end):
    """Keep fixed-period and rolling totals independent, including zero tails."""
    if not results or len({row['package'] for row in results}) != len(results):
        raise ValueError('Missing or duplicate npm package rows')
    daily = defaultdict(int)
    for result in results:
        for point in validate_range(result['package'], result['body'], start, end):
            daily[point['day']] += point['downloads']
    positive_days = [day for day, value in daily.items() if value > 0]
    if not positive_days:
        raise ValueError('No positive cohort day; retain the previous verified snapshot')
    through = max(positive_days)
    rolling_start = (dt.date.fromisoformat(through) - dt.timedelta(days=364)).isoformat()
    if rolling_start < start:
        raise ValueError('Not enough observations for a full rolling year')
    monthly = defaultdict(int)
    for day, value in sorted(daily.items()):
        if day <= through:
            monthly[day[:7]] += value
    packages = []
    for result in results:
        buckets = defaultdict(int)
        points = result['body']['downloads']
        for point in points:
            if point['day'] <= through:
                buckets[point['day'][:7]] += point['downloads']
        packages.append({
            'package': result['package'],
            'monthly_downloads': dict(sorted(buckets.items())),
            'rolling_365_days': sum(point['downloads'] for point in points
                                    if rolling_start <= point['day'] <= through),
            'response_sha256': result['receipt']['response_sha256'],
            'retrieved_at': result['receipt']['retrieved_at'],
        })
    evidence = {
        'retrieved_at': max(row['receipt']['retrieved_at'] for row in results),
        'source': f'https://api.npmjs.org/downloads/range/{start}:{end}/{{urlencoded_package}}',
        'requested_start': start, 'requested_end': end,
        'reported_through': through,
        'trailing_all_zero_days_excluded': [day for day in sorted(daily) if day > through],
        'package_count': len(packages),
        'rolling_start': rolling_start, 'rolling_end': through,
        'daily_totals': [{'day': day, 'downloads': value} for day, value in sorted(daily.items())],
        'packages': sorted(packages, key=lambda row: row['package']),
    }
    return evidence, dict(sorted(monthly.items()))


def save(relative_path, data):
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')


def main():
    today = dt.datetime.now(dt.timezone.utc).date()
    end = (today - dt.timedelta(days=1)).isoformat()
    packages, inventory_receipts = npm_inventory()
    print(f'Recounting {len(packages)} npm packages through requested date {end}', flush=True)

    def fetch_package(package):
        url = (f'https://api.npmjs.org/downloads/range/{PERIOD_START}:{end}/'
               + urllib.parse.quote(package, safe=''))
        body, receipt = fetch_json(url)
        validate_range(package, body, PERIOD_START, end)
        time.sleep(.7)
        return {'package': package, 'body': body, 'receipt': receipt}

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(fetch_package, packages):
            results.append(result)
            if len(results) % 25 == 0:
                print(f'Recounted {len(results)}/{len(packages)}', flush=True)
    evidence, monthly = summarize_ranges(results, PERIOD_START, end)
    crates, crate_receipts = crate_inventory()
    registry = json.loads((ROOT / 'data/registry-stats.json').read_text())
    old_npm = registry['npm']
    if evidence['reported_through'] < old_npm['period_end']:
        raise ValueError('npm reporting coverage regressed; retain the previous snapshot')
    verified = stamp()
    folder = f'data/snapshots/{today.isoformat()}'
    inventory_path, downloads_path = f'{folder}/npm-inventory.json', f'{folder}/npm-downloads.json'
    crates_path = f'{folder}/crates-inventory.json'
    npm = {
        'maintainer': 'ruvnet', 'package_count': len(packages),
        'download_package_count': len(packages),
        'inventory_verified_at': max(row['retrieved_at'] for row in inventory_receipts),
        'downloads_verified_at': evidence['retrieved_at'],
        'downloads': sum(row['rolling_365_days'] for row in evidence['packages']),
        'period_start': evidence['rolling_start'], 'period_end': evidence['rolling_end'],
        'period_days': 365, 'monthly_period_start': PERIOD_START,
        'inventory_path': inventory_path, 'downloads_evidence_path': downloads_path,
        'counting_rule': ('Sum of official npm daily range counts across the verified '
                          f'{len(packages)}-package maintainer cohort, including scoped and platform '
                          'packages. Trailing all-zero cohort days are excluded as not yet confirmed complete.'),
    }
    through = dt.date.fromisoformat(evidence['reported_through'])
    next_day = through + dt.timedelta(days=1)
    partial = next_day.month == through.month
    complete_end = through.replace(day=1) - dt.timedelta(days=1) if partial else through
    npm['monthly_period_end'] = complete_end.isoformat()
    npm['monthly_downloads'] = [
        {'month': month, 'downloads': value} for month, value in monthly.items()
        if month <= complete_end.isoformat()[:7]
    ]
    if partial:
        month = through.isoformat()[:7]
        npm['current_month'] = {
            'month': month, 'downloads': monthly[month], 'period_start': month + '-01',
            'period_end': through.isoformat(),
            'status': 'partial month; trailing all-zero API days excluded',
            'verified_at': evidence['retrieved_at'],
        }
    crate_total = sum(row['downloads'] for row in crates)
    registry.update(generated_at=verified, npm=npm, crates_io={
        'user_id': 339999, 'verified_at': max(row['retrieved_at'] for row in crate_receipts),
        'crate_count': len(crates), 'cumulative_downloads': crate_total,
        'inventory_path': crates_path,
        'counting_rule': 'Sum of the downloads field for every crate returned by the crates.io owner API for user_id 339999.',
    })
    # No published file is changed until every official API response is complete and validated.
    save(inventory_path, {'retrieved_at': npm['inventory_verified_at'],
                         'source': 'https://registry.npmjs.org/-/v1/search?text=maintainer%3Aruvnet',
                         'packages': packages, 'responses': inventory_receipts})
    save(downloads_path, evidence)
    save(crates_path, {'retrieved_at': registry['crates_io']['verified_at'],
                      'source': 'https://crates.io/api/v1/crates?user_id=339999',
                      'responses': crate_receipts, 'crates': crates})
    save('data/registry-stats.json', registry)
    metrics = json.loads((ROOT / 'data/metrics.json').read_text())
    metrics['verified_at'] = verified
    save('data/metrics.json', metrics)
    for command in [
        ['node', 'scripts/render-registry-metrics.mjs'],
        ['python3', 'scripts/render-visual-profile.py'],
        ['python3', 'scripts/render-constellation.py'],
        ['python3', '-m', 'unittest', 'discover', '-s', 'scripts/tests'],
        ['node', 'scripts/verify-profile.mjs'],
    ]:
        subprocess.run(command, cwd=ROOT, check=True)
    period_total = sum(monthly.values())
    combined = period_total + crate_total
    print(json.dumps({
        'npm_period_cumulative': period_total, 'npm_period_start': PERIOD_START,
        'npm_reported_through': evidence['reported_through'],
        'npm_rolling_365_days': npm['downloads'], 'rust_cumulative': crate_total,
        'combined_milestone_total': combined, 'remaining_to_100m': max(0, 100_000_000 - combined),
        'reached_100m': combined >= 100_000_000,
        'note': 'Mixed npm period and Rust cumulative windows; download events, not unique users.',
    }, indent=2))


if __name__ == '__main__':
    main()
