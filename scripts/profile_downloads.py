"""Canonical provider-specific download claims for the profile. No network access."""
import copy
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ROOT = Path(__file__).resolve().parents[1]

def canonical(running):
    goal = running['npm_billion_goal']
    latest = running['npm']['daily_latest']
    watermark = running['source_watermark']
    events = goal['observed_download_events_lower_bound']
    assert type(events) is int and events >= 0
    assert goal['observed_since'] == '2025-10-01'
    assert latest['coverage_complete'] and type(latest['downloads']) is int
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
        'latest': latest, 'watermark': digest,
        'npm_at': npm_at,
        'crates_at': running['crates_io']['verified_at'],
        'assets_at': watermark['github_verified_at'],
        'packages': running['npm']['expected_packages'],
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
    return c

if __name__ == '__main__':
    running = json.loads((ROOT / 'data/ecosystem-running-totals.json').read_text())
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
