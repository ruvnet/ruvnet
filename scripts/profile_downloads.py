"""Canonical provider-specific download claims for the profile. No network access."""
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ROOT = Path(__file__).resolve().parents[1]

def validate_goal_reconciliation(running, read_json):
    goal = running['npm_billion_goal']
    source = read_json(goal['reconciliation_source'])
    assert source['schema_version'] == 2
    ledger = read_json('data/ecosystem-daily-ledger.json')['values']
    prior = read_json(source['prior_summary'])['npm_billion_goal']
    assert source['prior_summary_sha256'] == hashlib.sha256(json.dumps(read_json(source['prior_summary']), indent=2).encode() + b'\n').hexdigest()
    prior_cells = read_json(source['prior_covered_ledger'])
    assert source['prior_covered_ledger_sha256'] == hashlib.sha256(json.dumps(prior_cells, indent=2).encode()+b'\n').hexdigest()
    expected_changed = {k for k,v in prior_cells['values'].items() if ledger.get(k) != v}
    adjustment = prior.get('baseline_covered_day_revision_adjustment', 0)
    seen = set()
    for row in source['covered_revisions']:
        key = row['key']; assert key not in seen; seen.add(key)
        provider, name, metric, day = key.split('|')
        assert provider == 'npm' and metric == 'downloads' and day <= goal['baseline_through']
        old = read_json(row['prior_source']); new = read_json(row['source'])
        assert old['values'][name] == row['prior']
        assert new['values'][name] == row['current'] == ledger[key]
        assert row['source_sha256'] == hashlib.sha256(json.dumps(new, indent=2).encode()+b'\n').hexdigest()
        adjustment += row['current'] - row['prior']
    assert seen == expected_changed, 'Omitted or spurious covered-date revision'
    assert adjustment == goal['baseline_covered_day_revision_adjustment'], 'Incorrect covered-day revision adjustment'
    cells = {k:v for k,v in ledger.items() if k.startswith('npm|') and goal['baseline_through'] < k.rsplit('|',1)[-1] <= source['through'] and type(v) is int}
    assert source['increment_cells'] == cells
    assert sum(cells.values()) == goal['nonoverlapping_daily_increment']
    assert sorted({k.rsplit('|',1)[-1] for k in cells}) == goal['increment_dates']
    assert goal['verified_at'] == source['verified_at']
    baseline = read_json(goal['baseline_source'])
    baseline_total = sum(row['downloads'] or 0 for row in baseline['daily_totals'] if row['day'] <= baseline['reported_through'])
    assert baseline_total == goal['baseline_download_events']
    assert goal['observed_download_events_lower_bound'] == baseline_total + adjustment + sum(cells.values())

def validate_goal_revision(running, read_json):
    if running['npm_billion_goal'].get('reconciliation_source'):
        return validate_goal_reconciliation(running, read_json)
    goal = running['npm_billion_goal']
    adjustment = goal.get('baseline_covered_day_revision_adjustment', 0)
    if not adjustment:
        return
    receipt = read_json('data/snapshots/' + running['source_watermark']['snapshot_date'] + '/collection-receipt.json')['applied_reconciliation']
    source = read_json(goal['baseline_revision_source'])
    row = source['results'][0]
    point = row['body']['downloads'][0]
    assert receipt['canonical_applied'] is True
    assert receipt['key'] == 'npm|' + row['package'] + '|downloads|' + point['day']
    assert receipt['current'] == point['downloads']
    assert adjustment == receipt['current'] - receipt['prior'], 'Incorrect covered-day revision adjustment'
    assert receipt['source'] == goal['baseline_revision_source']
    assert receipt['source_sha256'] == hashlib.sha256(json.dumps(source, indent=2).encode() + b'\n').hexdigest()
    assert goal['verified_at'] == row['receipt']['retrieved_at']
    assert goal['observed_download_events_lower_bound'] == goal['baseline_download_events'] + adjustment + goal['nonoverlapping_daily_increment']

def validate_latest_cohort(latest, point, inventory_count, inventory_ids=None, creations=None):
    assert point["day"] == latest["day"], "Mismatched latest UTC date"
    assert not point.get("provider_data_provisional") and not point.get("provisional"), "Provisional provider day cannot be confirmed"
    exclusions = point.get('excluded_created_after_target_day', {})
    assert len(point['values']) == latest['collected_packages']
    assert latest['expected_packages'] + len(exclusions) == inventory_count
    for package, created in exclusions.items():
        at = created if isinstance(created, str) else created.get('created_at')
        try:
            created = dt.datetime.fromisoformat(at.replace('Z','+00:00'))
            assert created.tzinfo is not None
        except (ValueError, AttributeError, TypeError):
            raise AssertionError('Invalid package creation timestamp')
        assert created.astimezone(dt.timezone.utc).date().isoformat() > latest['day'], 'Unverified postwindow creation exclusion'
        assert package not in point['values'], 'Excluded package also counted'
        if creations is not None: assert creations.get(package) == at, 'Unverified creation provenance'
    if inventory_ids is not None: assert set(point['values']) | set(exclusions) == set(inventory_ids), 'Unknown or missing inventory ID'
    assert latest['collected_packages'] == latest['expected_packages']

def canonical(running):
    goal = running['npm_billion_goal']
    latest = running['npm']['daily_latest']
    watermark = running['source_watermark']
    events = goal['observed_download_events_lower_bound']
    assert type(events) is int and events >= 0
    assert goal['observed_since'] == '2025-10-01'
    assert latest['coverage_complete'] and type(latest['downloads']) is int
    assert latest['day'] not in goal.get('provisional_dates', []), 'Provisional provider day cannot be confirmed'
    through = max(goal.get('increment_dates', []) + [goal['baseline_through']])
    npm_at = goal.get('verified_at', running['npm']['daily_attempt']['verified_at'])
    assert through < npm_at[:10], 'Current incomplete UTC day must not be displayed as completed'
    # Preserve the immutable GitHub watermark; a newer registry baseline carries
    # its own source identity and retrieval date in the composite display digest.
    provenance = {'collection': watermark, 'npm_goal': goal} if goal.get('verified_at') else watermark
    digest = hashlib.sha256(json.dumps(provenance, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {
        'npm': events, 'start': goal['observed_since'], 'through': through,
        'crates': running['crates_io']['cumulative_downloads'],
        'assets': running['release_assets']['retained_observed_downloads'],
        'latest': latest, 'attempt': running['npm']['daily_attempt'], 'watermark': digest,
        'npm_at': npm_at,
        'crates_at': running['crates_io']['verified_at'],
        'assets_at': watermark['github_verified_at'],
        'packages': running['npm']['expected_packages'],
        'provisional_dates': goal.get('provisional_dates', []),
        'provisional_events': goal.get('provisional_observed_downloads'),
        'missing': sorted(set(goal.get('missing_increment_dates', []) + goal.get('historical_unknown_dates', [])))
    }

def apply_downloads(root, running, npm):
    c = canonical(running)
    def put(x, y, value, identifier):
        matches = [e for e in root.iter(f'{{{NS}}}text') if e.get('x') == str(x) and e.get('y') == str(y)]
        assert len(matches) == 1
        matches[0].text = value
        matches[0].set('id', identifier)
    put(34, 182, 'NPM EVENTS / LOWER BOUND', 'npm-observed-label')
    put(34, 222, f"{c['npm']:,}", 'npm-observed-total')
    put(34, 248, 'OBSERVED SINCE OCT 1, 2025', 'npm-observed-basis')
    put(34, 301, f"HISTORICAL NPM CHART / {npm['download_package_count']} PACKAGES", 'npm-history-label')
    put(54, 784, f"NPM THROUGH {c['through']} · CRATES {c['crates_at'][:10]} · ASSETS {c['assets_at'][:10]}", 'download-source-dates')
    group = ET.Element(f'{{{NS}}}g', {'id': 'download-providers', 'role': 'group', 'aria-label': 'Separate provider download counts and latest complete npm day'})
    latest = c['latest']
    lines = [
        ('crates-observed-total', 90, f"CRATES.IO CUMULATIVE: {c['crates']:,}"),
        ('release-assets-observed-total', 108, f"RELEASE ASSETS OBSERVED: {c['assets']:,}"),
        ('npm-latest-complete-total', 126, f"LATEST COMPLETE NPM DAY: {latest['downloads']:,}"),
        ('npm-latest-complete-date', 143, f"{latest['day']} UTC · {latest['collected_packages']}/{latest['expected_packages']} PACKAGES")
    ]
    for identifier, y, value in lines:
        ET.SubElement(group, f'{{{NS}}}text', {'id': identifier, 'x': '1165', 'y': str(y), 'font-size': '11', 'fill': '#9de8d0', 'text-anchor': 'end'}).text = value
    loader = next(e for e in root if e.get('class') == 'gameboot')
    root.insert(list(root).index(loader), group)
    root.set('data-download-watermark', c['watermark'])
    root.set('data-npm-start', c['start'])
    root.set('data-npm-through', c['through'])
    for key in ['npm_at', 'crates_at', 'assets_at']:
        root.set('data-' + key.replace('_', '-'), c[key])
    desc = root.find(f'{{{NS}}}desc')
    desc.text = (
        f"Npm only: {c['npm']:,} observed download events since {c['start']} through {c['through']}; "
        f"lower bound, historical coverage gaps retained, current inventory {c['packages']} packages. "
        f"Unknown source dates: {', '.join(c['missing']) or 'none'}. "
        f"Provisional provider dates: {', '.join(c['provisional_dates']) or 'none'}; observed events {c['provisional_events']}. "
        f"Latest attempted npm UTC day {c['attempt']['day']}: {c['attempt']['observed_downloads']} observed events from {c['attempt']['collected_packages']}/{c['attempt']['expected_packages']} packages; full total {'unknown' if c['attempt']['downloads'] is None else c['attempt']['downloads']}. "
        f"Latest complete npm UTC day {latest['day']}: {latest['downloads']:,} events, "
        f"{latest['collected_packages']}/{latest['expected_packages']} packages, retrieved {latest['verified_at']}. "
        f"Crates.io cumulative downloads: {c['crates']:,}, retrieved {c['crates_at']}. "
        f"Release asset retained observed downloads: {c['assets']:,}, retrieved {c['assets_at']}; not npm downloads. "
        f"Npm reconciliation retrieved {c['npm_at']}. Source watermark SHA256 {c['watermark']}. "
        f"Historical chart only: {npm['download_package_count']} packages, {npm['monthly_period_start']} through "
        f"{npm.get('current_month', {}).get('period_end', npm['monthly_period_end'])}; not current headline coverage. "
        "Stars are current gauges; star traces are not daily histories. Animation is decorative."
    )

def verify_downloads(root, running):
    c = canonical(running)
    by_id = {e.get('id'): e for e in root.iter() if e.get('id')}
    expected = {
        'npm-observed-label': 'NPM EVENTS / LOWER BOUND',
        'npm-observed-total': f"{c['npm']:,}",
        'npm-observed-basis': 'OBSERVED SINCE OCT 1, 2025',
        'crates-observed-total': f"CRATES.IO CUMULATIVE: {c['crates']:,}",
        'release-assets-observed-total': f"RELEASE ASSETS OBSERVED: {c['assets']:,}",
        'npm-latest-complete-total': f"LATEST COMPLETE NPM DAY: {c['latest']['downloads']:,}",
        'npm-latest-complete-date': f"{c['latest']['day']} UTC · {c['latest']['collected_packages']}/{c['latest']['expected_packages']} PACKAGES"
    }
    for identifier, value in expected.items():
        assert by_id.get(identifier) is not None and by_id[identifier].text == value, f"Stale SVG download claim: {identifier}"
    assert by_id['npm-history-label'].text.startswith('HISTORICAL NPM CHART /')
    assert root.get('data-download-watermark') == c['watermark'], 'Stale source watermark'
    assert root.get('data-npm-start') == c['start'] and root.get('data-npm-through') == c['through']
    for key in ['npm_at', 'crates_at', 'assets_at']:
        assert root.get('data-' + key.replace('_', '-')) == c[key], f'Stale retrieval date: {key}'
    desc = root.find(f'{{{NS}}}desc').text
    for value in [f"Npm only: {c['npm']:,}", c['start'], c['through'], 'lower bound', c['watermark'], c['latest']['day'], f"{c['crates']:,}", f"{c['assets']:,}", 'Historical chart only:']:
        assert value in desc, f'Stale accessible description: {value}'
    provisional = f"Provisional provider dates: {', '.join(c['provisional_dates']) or 'none'}; observed events {c['provisional_events']}."
    assert provisional in desc, 'Stale provisional provider disclosure'
    assert f"Latest attempted npm UTC day {c['attempt']['day']}: {c['attempt']['observed_downloads']} observed events from {c['attempt']['collected_packages']}/{c['attempt']['expected_packages']} packages; full total {'unknown' if c['attempt']['downloads'] is None else c['attempt']['downloads']}." in desc, 'Stale partial coverage disclosure'
    assert f"current inventory {c['packages']} packages" in desc, 'Stale inventory coverage'
    return c

if __name__ == '__main__':
    running = json.loads((ROOT / 'data/ecosystem-running-totals.json').read_text())
    validate_goal_revision(running, lambda p: json.loads((ROOT / p).read_text()))
    latest = running['npm']['daily_latest']
    registry = json.loads((ROOT / 'data/registry-stats.json').read_text())
    inventory = json.loads((ROOT / registry['npm']['inventory_path']).read_text())['packages']
    manifests = json.loads((ROOT / ('data/snapshots/' + running['source_watermark']['snapshot_date'] + '/npm-new-manifests.json')).read_text())
    validate_latest_cohort(latest, json.loads((ROOT / latest['source']).read_text()), running['npm']['expected_packages'], inventory, {r['package']:r.get('created_at') for r in manifests['packages']})
    root = ET.parse(ROOT / 'assets/ruvnet/dashboard.svg').getroot()
    result = verify_downloads(root, running)
    # Reproduce the original stale-source defect by substituting the old mixed total.
    broken = copy.deepcopy(root)
    next(e for e in broken.iter() if e.get('id') == 'npm-observed-total').text = f"{running['download_milestone']['combined_observed']:,}"
    try:
        verify_downloads(broken, running)
    except AssertionError:
        pass
    else:
        raise AssertionError('Stale mixed-provider headline was accepted')
    print(json.dumps({'status': 'PASS', 'npm_observed_lower_bound': result['npm'], 'crates_io': result['crates'], 'release_assets': result['assets'], 'stale_source_regression_rejected': True, 'watermark': result['watermark']}))
