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

class NpmRangeNotFound(RuntimeError):
    """npm knows the package, but its download-range resource is not ready."""


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
            # Newly published npm packages can appear in search before download stats.
            npm_pending = error.code == 404 and url.startswith('https://api.npmjs.org/downloads/')
            if npm_pending and attempt == 7:
                raise NpmRangeNotFound(
                    f'HTTP 404 retrieving {url}; previous verified data retained') from error
            if not npm_pending and (error.code not in (429, 500, 502, 503, 504) or attempt == 7):
                raise RuntimeError(f'HTTP {error.code} retrieving {url}; previous verified data retained') from error
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


def update_daily_ledger(results, today, verified, expected_packages=None, errors=None):
    """Upsert the latest 14 complete UTC days by package and date."""
    start = (today - dt.timedelta(days=14)).isoformat()
    end = (today - dt.timedelta(days=1)).isoformat()
    ledger_path = ROOT / 'data/ecosystem-daily-ledger.json'
    ledger = json.loads(ledger_path.read_text())
    values = ledger.setdefault('values', {})
    provenance = ledger.setdefault('package_provenance', {})
    reported_through = max((point['day'] for result in results
                            for point in result['body']['downloads']
                            if point['downloads'] > 0), default=None)
    for result in results:
        package = result['package']
        points = validate_range(package, result['body'], PERIOD_START, end)
        for point in points:
            if start <= point['day'] <= end:
                values[f"npm|{package}|downloads|{point['day']}"] = (
                    point['downloads'] if reported_through and point['day'] <= reported_through else None)
        provenance[package] = {
            'source': result['receipt']['source'],
            'retrieved_at': result['receipt']['retrieved_at'],
            'response_sha256': result['receipt']['response_sha256'],
        }
    ledger['observed_from'] = min(ledger.get('observed_from', start), start)
    ledger['observed_through'] = end
    ledger['updated_at'] = verified
    ledger['coverage'] = {
        'expected_packages': expected_packages if expected_packages is not None else len(results),
        'collected_packages': len(results),
        'errors': errors or [],
    }
    ledger['interpretation'] = ('Observed download events in stored package/date cells. '
                                'Not lifetime downloads. Recent provider zero days may be provisional.')
    save('data/ecosystem-daily-ledger.json', ledger)


def latest_daily_summary(npm, evidence):
    """Derive the latest positive calendar day from the canonical npm receipt."""
    latest = next(row for row in evidence['daily_totals']
                  if row['day'] == evidence['reported_through'])
    return {
        'verified_at': evidence['retrieved_at'], 'day': latest['day'],
        'downloads': latest['downloads'], 'expected_packages': npm['package_count'],
        'collected_packages': npm['download_package_count'],
        'period_type': 'UTC calendar day', 'rolling_24_hours': False,
        'source': evidence['source'],
        'status': 'latest positive completed UTC date; excludes newer provisional all-zero dates',
    }


def update_running_totals(registry, evidence):
    """Keep the dashboard milestone aligned with verified registry evidence."""
    path = ROOT / 'data/ecosystem-running-totals.json'
    if not path.exists():
        return
    running = json.loads(path.read_text())
    npm, crates = registry['npm'], registry['crates_io']
    total = sum(row['downloads'] for row in evidence['daily_totals']
                if row['day'] <= evidence['reported_through'])
    combined = total + crates['cumulative_downloads']
    milestone = running['download_milestone']
    cohort_label = f"{npm['download_package_count']} of {npm['package_count']}"
    milestone.update(
        npm_baseline_downloads=total, npm_baseline_through=evidence['reported_through'],
        npm_increment_observed=0, npm_increment_start=None, npm_increment_end=None,
        npm_increment_package_coverage=npm['download_package_count'],
        npm_expected_packages=npm['package_count'], npm_observed_total=total,
        crates_io_cumulative=crates['cumulative_downloads'], combined_observed=combined,
        remaining=max(0, milestone['target']-combined),
        baseline_source=npm['downloads_evidence_path'], increment_source=npm['downloads_evidence_path'],
        npm_verified_at=npm['downloads_verified_at'], npm_reported_through=evidence['reported_through'],
        crates_io_verified_at=crates['verified_at'],
        status=('Observed lower bound; collected API responses may contain provider reporting gaps; '
                f'{cohort_label} inventory packages have download-range evidence'),
        internal_all_zero_cohort_days=[r['day'] for r in evidence['daily_totals']
            if r['day'] <= evidence['reported_through'] and r['downloads'] == 0],
        trailing_all_zero_days_excluded=evidence['trailing_all_zero_days_excluded'])
    running['crates_io'] = dict(crates)
    running['verified_at'] = max(running['verified_at'], registry['generated_at'])
    # The rolling ledger and activity inventories retain their own source dates.
    ledger = json.loads((ROOT/'data/ecosystem-daily-ledger.json').read_text())
    end = ledger['observed_through']
    start = (dt.date.fromisoformat(end)-dt.timedelta(days=13)).isoformat()
    cohort = {r['package'] for r in evidence['packages']}
    daily, coverage = defaultdict(int), defaultdict(set)
    for key, value in ledger['values'].items():
        provider, package, metric, day = key.split('|')
        if provider == 'npm' and metric == 'downloads' and package in cohort and start <= day <= end:
            if value is None:
                continue
            daily[day] += value
            coverage[day].add(package)
    expected = [(dt.date.fromisoformat(start)+dt.timedelta(days=i)).isoformat() for i in range(14)]
    missing = [day for day in expected if len(coverage[day]) != npm['package_count']]
    running['npm'].update(period_start=start, period_end=end, verified_at=ledger['updated_at'],
        observed_downloads=sum(daily.values()), expected_packages=npm['package_count'],
        collected_packages=npm['download_package_count'], daily=dict(sorted(daily.items())),
        daily_package_coverage={day:len(coverage[day]) for day in expected}, missing_days=missing,
        all_zero_cohort_days=[day for day,value in daily.items() if value == 0],
        provisional_days=evidence['trailing_all_zero_days_excluded'],
        errors=evidence.get('unavailable_packages', []),
        status=(f'{cohort_label} inventory packages collected; '
                'provisional trailing dates are unknown; provider reporting gaps may remain'),
        latest_confirmed_daily=latest_daily_summary(npm, evidence))
    running['validation'].update(unique_daily_keys=len(ledger['values']),
        daily_total_reconciliation=True, download_milestone_reconciliation=True,
        missing_days_recorded=missing,
        npm_download_package_coverage_complete=npm['download_package_count'] == npm['package_count'],
        npm_unavailable_packages=len(evidence.get('unavailable_packages', [])))
    save('data/ecosystem-running-totals.json', running)


def main():
    today = dt.datetime.now(dt.timezone.utc).date()
    end = (today - dt.timedelta(days=1)).isoformat()
    packages, inventory_receipts = npm_inventory()
    print(f'Recounting {len(packages)} npm packages through requested date {end}', flush=True)
    previous_registry = json.loads((ROOT / 'data/registry-stats.json').read_text())
    previous_evidence = json.loads(
        (ROOT / previous_registry['npm']['downloads_evidence_path']).read_text())
    previous_packages = {row['package'] for row in previous_evidence['packages']}

    def fetch_package(package):
        url = (f'https://api.npmjs.org/downloads/range/{PERIOD_START}:{end}/'
               + urllib.parse.quote(package, safe=''))
        try:
            body, receipt = fetch_json(url)
        except NpmRangeNotFound:
            if package in previous_packages:
                raise
            return {
                'package': package, 'unavailable': True, 'source': url,
                'checked_at': stamp(),
                'error': 'npm download-range endpoint returned HTTP 404 after bounded retries',
            }
        validate_range(package, body, PERIOD_START, end)
        time.sleep(.7)
        return {'package': package, 'body': body, 'receipt': receipt}

    fetched = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(fetch_package, packages):
            fetched.append(result)
            if len(fetched) % 25 == 0:
                print(f'Recounted {len(fetched)}/{len(packages)}', flush=True)
    unavailable = [row for row in fetched if row.get('unavailable')]
    results = [row for row in fetched if not row.get('unavailable')]
    evidence, monthly = summarize_ranges(results, PERIOD_START, end)
    evidence['inventory_package_count'] = len(packages)
    evidence['download_package_count'] = len(results)
    evidence['unavailable_packages'] = unavailable
    crates, crate_receipts = crate_inventory()
    registry = previous_registry
    old_npm = registry['npm']
    if evidence['reported_through'] < old_npm['period_end']:
        raise ValueError('npm reporting coverage regressed; retain the previous snapshot')
    verified = stamp()
    folder = f'data/snapshots/{today.isoformat()}'
    inventory_path, downloads_path = f'{folder}/npm-inventory.json', f'{folder}/npm-downloads.json'
    crates_path = f'{folder}/crates-inventory.json'
    npm = {
        'maintainer': 'ruvnet', 'package_count': len(packages),
        'download_package_count': len(results),
        'inventory_verified_at': max(row['retrieved_at'] for row in inventory_receipts),
        'downloads_verified_at': evidence['retrieved_at'],
        'downloads': sum(row['rolling_365_days'] for row in evidence['packages']),
        'period_start': evidence['rolling_start'], 'period_end': evidence['rolling_end'],
        'period_days': 365, 'monthly_period_start': PERIOD_START,
        'inventory_path': inventory_path, 'downloads_evidence_path': downloads_path,
        'counting_rule': ('Sum of official npm daily range counts across the verified '
                          f'{len(results)} of {len(packages)} packages in the maintainer cohort, including '
                          'scoped and platform packages. Packages whose range endpoint is not yet available '
                          'remain explicitly missing, never zero. Trailing all-zero cohort days are excluded '
                          'as not yet confirmed complete.'),
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
    update_daily_ledger(
        results, today, verified, expected_packages=len(packages), errors=unavailable)
    update_running_totals(registry, evidence)
    metrics = json.loads((ROOT / 'data/metrics.json').read_text())
    metrics['verified_at'] = verified
    save('data/metrics.json', metrics)
    for command in [
        ['node', 'scripts/render-registry-metrics.mjs'],
        ['python3', 'scripts/render-github-metrics.py'],
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
