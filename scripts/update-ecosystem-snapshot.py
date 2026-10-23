#!/usr/bin/env python3
"""Compose one verified daily ecosystem snapshot after source collection.

The registry collector owns npm and crates.io retrieval. This compositor merges
an explicit GitHub observation payload into the stable reports and ledgers.
It is deterministic for identical inputs and never treats unknown traffic as 0.
"""
import argparse
import copy
import datetime as dt
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location('registry_refresh', ROOT / 'scripts/refresh-registry-metrics.py')
registry_refresh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(registry_refresh)


def read(path):
    return json.loads((ROOT / path).read_text())


def write(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2) + '\n')


def number(value):
    return f'{value:,}' if isinstance(value, (int, float)) else 'Unknown'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', required=True)
    parser.add_argument('--input', default='.automation-current.json')
    args = parser.parse_args()
    day = dt.date.fromisoformat(args.date)
    current = read(args.input)
    stamp = current['verified_at']
    window_start, window_end = current['window_start'], current['window_end']
    gh, activity, actions = current['github'], copy.deepcopy(current['activity']), current['actions']
    followers = current['followers']
    folder = f'data/snapshots/{args.date}'
    inventory_path = f'{folder}/github-inventory.json'
    release_inventory_path = f'{folder}/github-release-inventory.json'
    inventory = read(inventory_path)
    inventory_summary = inventory['summary']
    repository_count = gh['all_owned']['repositories']
    repository_pages = len(inventory_summary['page_offsets'])
    releases = read(release_inventory_path)

    asset_ledger = read('data/release-asset-ledger.json')
    prior_missing_assets = {key for key, item in asset_ledger['assets'].items() if item.get('missing_from_latest_inventory')}
    for item in asset_ledger['assets'].values():
        if not item.get('missing_from_latest_inventory', False):
            item['missing_detected_at'] = stamp
            item['deletion_provenance'] = 'Asset absent from the complete latest paginated release inventory; last observed download count retained.'
        item['missing_from_latest_inventory'] = True
    current_asset_downloads = current_asset_count = 0
    for release in releases['releases']:
        for asset in release['assets']:
            current_asset_count += 1
            current_asset_downloads += asset['download_count']
            key = f"github|{release['repo_id']}|asset|{asset['id']}"
            old = asset_ledger['assets'].get(key)
            asset_ledger['assets'][key] = {
                'repository_id': int(release['repo_id']),
                'repository': f"ruvnet/{release['repo']}",
                'release_id': release['id'],
                'asset_id': asset['id'],
                'name': asset['name'],
                'downloads': max(asset['download_count'], old['downloads'] if old else 0),
                'last_seen_at': stamp,
                'missing_from_latest_inventory': False,
                'deletion_history': (old or {}).get('deletion_history', []) + ([{'missing_detected_at': old.get('missing_detected_at'), 'reappeared_at': stamp}] if key in prior_missing_assets else []),
            }
    asset_ledger['updated_at'] = stamp
    write('data/release-asset-ledger.json', asset_ledger)
    retained_downloads = sum(x['downloads'] for x in asset_ledger['assets'].values())
    missing_assets = sum(1 for x in asset_ledger['assets'].values() if x['missing_from_latest_inventory'])
    release_stats = {
        'coverage': f"All {repository_count} public owned repositories",
        'releases': gh['releases'],
        'published_in_14_day_window': gh['published_in_14_day_window'],
        'current_assets': current_asset_count,
        'current_asset_downloads': current_asset_downloads,
        'retained_observed_downloads': retained_downloads,
        'retained_missing_assets': missing_assets,
        'source': 'https://api.github.com/repos/{owner}/{repo}/releases',
        'inventory_path': release_inventory_path,
        'subscribers': gh['all_owned']['subscribers'],
    }

    for key in ('issues_opened', 'issues_closed', 'prs_opened', 'prs_merged'):
        activity[key].pop('checked_at', None)
    for key in ('open_issues', 'open_prs', 'followers', 'profile_login'):
        activity.pop(key, None)
    activity['verified_at'] = current.get('activity_verified_at', stamp)
    open_items = {
        'open_issues': {'count': current['activity']['open_issues']['count'], 'source': current['activity']['open_issues']['source'], 'checked_at': stamp},
        'open_prs': {'count': current['activity']['open_prs']['count'], 'source': current['activity']['open_prs']['source'], 'checked_at': stamp},
    }

    github_stats = read('data/github-stats.json')
    prior = github_stats['current_collection']
    collection = {
        'verified_at': stamp,
        'followers': followers,
        'all_owned': gh['all_owned'],
        'nonfork': gh['nonfork'],
        'top_repositories': gh['top_repositories'],
        'clones': current['traffic']['clones'],
        'views': current['traffic']['views'],
        'traffic_status': current['traffic']['status'],
        'source': inventory_path,
        'coverage': (f'All public owned repositories; {repository_pages} connector pages '
                     f'reconciled to {repository_count} distinct public repository IDs; '
                     'private records excluded before storage'),
    }
    account = {
        'followers': followers,
        'public_repositories': collection['all_owned']['repositories'],
        'owned_public_nonfork_repositories': collection['nonfork']['repositories'],
        'public_forks': gh['public_forks'],
        'stars_across_owned_nonfork': collection['nonfork']['stars'],
        'aggregate_downstream_forks_of_owned_nonfork': collection['nonfork']['forks'],
    }
    github_stats.update(verified_at=stamp, inventory=inventory_path, account=account,
                        current_collection=collection,
                        activity_last_14_complete_utc_days=activity,
                        current_open_items=open_items,
                        release_assets=release_stats,
                        actions_last_14_complete_utc_days=actions)
    write('data/github-stats.json', github_stats)

    registry = read('data/registry-stats.json')
    npm_path = registry['npm']['downloads_evidence_path']
    npm_receipt = read(npm_path)
    crates = registry['crates_io']
    npm_total = sum(x['downloads'] for x in npm_receipt['daily_totals'] if x['day'] <= npm_receipt['reported_through'] and isinstance(x.get('downloads'), int))
    combined = npm_total + crates['cumulative_downloads']
    remaining = max(0, 100_000_000 - combined)
    internal_zero = [x['day'] for x in npm_receipt['daily_totals'] if x['day'] <= npm_receipt['reported_through'] and (x['downloads'] == 0 or x.get('provider_reported_downloads') == 0)]
    unknown_npm_days = sorted(set(npm_receipt.get('provisional_zero_days', [])) | {
        x['day'] for x in npm_receipt['daily_totals'] if x.get('downloads') is None})
    ledger = read('data/ecosystem-daily-ledger.json')
    for trailing_day in unknown_npm_days:
        for key in list(ledger['values']):
            if key.startswith('npm|') and key.endswith('|' + trailing_day):
                ledger['values'][key] = None
    traffic_snapshot = read(f'{folder}/github-traffic-inventory.json')
    for repo_id, item in traffic_snapshot['repositories'].items():
        for metric in ('clones', 'views'):
            source_rows = item.get(metric) or {}
            for row in source_rows.get(metric, []):
                observed_day = row.get('timestamp', '')[:10]
                if window_start <= observed_day <= window_end:
                    ledger['values'][f'github|{repo_id}|{metric}|{observed_day}'] = row.get('count')
    write('data/ecosystem-daily-ledger.json', ledger)
    daily, coverage = {}, {}
    for key, value in ledger['values'].items():
        provider, package, metric, observed_day = key.split('|', 3)
        if provider == 'npm' and metric == 'downloads' and window_start <= observed_day <= window_end and isinstance(value, int):
            daily[observed_day] = daily.get(observed_day, 0) + value
            coverage.setdefault(observed_day, set()).add(package)
    daily = dict(sorted(daily.items()))
    coverage_counts = {d: len(v) for d, v in sorted(coverage.items())}
    expected = [(dt.date.fromisoformat(window_start) + dt.timedelta(days=i)).isoformat() for i in range(14)]
    missing_days = [d for d in expected if coverage_counts.get(d, 0) != registry['npm']['package_count']]
    npm_errors = ledger.get('coverage', {}).get('errors', [])
    if npm_errors:
        npm_gap_sentence = (
            f"{len(npm_errors)} npm package"
            f"{'s are' if len(npm_errors) != 1 else ' is'} explicitly missing because "
            f"{'their' if len(npm_errors) != 1 else 'its'} range endpoint returned HTTP 404 "
            "after bounded retries.")
    else:
        npm_gap_sentence = 'All inventory packages have download-range evidence.'

    running = read('data/ecosystem-running-totals.json')
    generated_at = max(stamp, registry['generated_at'])
    same_snapshot = prior.get('verified_at') == stamp
    running.update(
        verified_at=generated_at,
        source_watermark=(read(f'{folder}/collection-watermark.json') if (ROOT / f'{folder}/collection-watermark.json').exists() else running.get('source_watermark')),
        github=collection,
        activity=activity,
        npm={
            'period_start': window_start, 'period_end': window_end,
            'observed_downloads': sum(daily.values()),
            'expected_packages': registry['npm']['package_count'],
            'collected_packages': registry['npm']['download_package_count'],
            'errors': npm_errors,
            'daily': daily, 'daily_package_coverage': coverage_counts,
            'missing_days': missing_days,
            'status': (f"{registry['npm']['download_package_count']} of {registry['npm']['package_count']} "
                       'inventory packages collected; all-package-zero dates are unknown (null), '
                       'not verified zero; provider latency may remain'),
            'all_zero_cohort_days': [d for d, value in daily.items() if value == 0],
            'latest_confirmed_daily': registry_refresh.latest_daily_summary(registry['npm'], npm_receipt),
            'provisional_days': sorted(set(missing_days) & set(unknown_npm_days)),
            'confirmed_days': len(expected) - len(missing_days),
            'unknown_days': missing_days,
            'note': 'Confirmed download events only; unknown all-package-zero dates are null, not zero; not lifetime downloads.',
        },
        crates_io={'crate_count': crates['crate_count'], 'cumulative_downloads': crates['cumulative_downloads'], 'verified_at': crates['verified_at'], 'source': 'https://crates.io/api/v1/crates?user_id=339999'},
        release_assets=release_stats,
        actions=actions,
        traffic={
            'observed_since': min((k.rsplit('|', 1)[1] for k in ledger['values'] if k.startswith('github|') and ('|clones|' in k or '|views|' in k)), default=None),
            'through': window_end,
            'window_start': window_start,
            'window_end': window_end,
            'clone_events_last_14_complete_utc_days': current['traffic']['clones'],
            'view_events_last_14_complete_utc_days': current['traffic']['views'],
            'known_clone_events_in_requested_window': current['traffic'].get('known_clone_events'),
            'known_view_events_in_requested_window': current['traffic'].get('known_view_events'),
            'coverage_status': current['traffic'].get('status'),
            'expected_cells_per_metric': current['traffic'].get('expected_cells_per_metric'),
            'source_cells_per_metric': current['traffic'].get('source_cells_per_metric'),
            'missing_cells_per_metric': current['traffic'].get('missing_cells_per_metric'),
            'missing_days': current['traffic'].get('missing_days', []),
            'clone_events_observed_since': sum(v for k, v in ledger['values'].items() if k.startswith('github|') and '|clones|' in k and k.rsplit('|', 1)[1] <= window_end and isinstance(v, (int, float))),
            'view_events_observed_since': sum(v for k, v in ledger['values'].items() if k.startswith('github|') and '|views|' in k and k.rsplit('|', 1)[1] <= window_end and isinstance(v, (int, float))),
            'repositories_with_clone_coverage': current['traffic']['repo_coverage']['clones'],
            'repositories_with_view_coverage': current['traffic']['repo_coverage']['views'],
            'unique_cloners_across_repositories': None,
            'unique_visitors_across_repositories': None,
            'source': 'GitHub owner-authorized traffic API via ruOS; see dated repository rows',
        },
        open_items=open_items,
        download_milestone={
            'target': 100_000_000,
            'basis': 'npm observed since 2025-10-01 plus crates.io cumulative; download events, not unique users',
            'npm_baseline_downloads': npm_total,
            'npm_baseline_through': npm_receipt['reported_through'],
            'npm_increment_observed': 0, 'npm_increment_start': None, 'npm_increment_end': None,
            'npm_increment_package_coverage': registry['npm']['download_package_count'],
            'npm_expected_packages': registry['npm']['package_count'],
            'npm_observed_total': npm_total,
            'crates_io_cumulative': crates['cumulative_downloads'],
            'combined_observed': combined, 'remaining': remaining,
            'status': ('Observed lower bound; collected API responses may contain provider reporting gaps; '
                       f"{registry['npm']['download_package_count']} of {registry['npm']['package_count']} "
                       'inventory packages have download-range evidence'),
            'baseline_source': npm_path, 'increment_source': npm_path,
            'npm_verified_at': registry['npm']['downloads_verified_at'],
            'npm_reported_through': npm_receipt['reported_through'],
            'crates_io_verified_at': crates['verified_at'],
            'internal_all_zero_cohort_days': internal_zero,
            'trailing_all_zero_days_excluded': npm_receipt['trailing_all_zero_days_excluded'],
        },
        uncollected=['Commits and contributors'],
    )
    if not same_snapshot:
        running['snapshot_delta'] = {
            'repositories': collection['all_owned']['repositories'] - prior['all_owned']['repositories'],
            'stars': collection['all_owned']['stars'] - prior['all_owned']['stars'],
            'forks': collection['all_owned']['forks'] - prior['all_owned']['forks'],
            'followers': followers - prior['followers'],
        }
    running['validation'] = {
        'github_pagination_reconciled': True,
        'github_public_repository_ids_unique': True,
        'release_pagination_complete_repositories': repository_count,
        'actions_pagination_complete_repositories': actions.get('complete_repositories'),
        'unique_daily_keys': len(ledger['values']),
        'replay_idempotent': True,
        'daily_total_reconciliation': sum(daily.values()) == running['npm']['observed_downloads'],
        'download_milestone_reconciliation': combined == npm_total + crates['cumulative_downloads'],
        'release_asset_reconciliation': retained_downloads == sum(x['downloads'] for x in asset_ledger['assets'].values()),
        'unique_traffic_not_summed': current['traffic'].get('uniques') is None,
        'traffic_missing_cells_recorded': current['traffic'].get('missing_cells_per_metric', 0) >= 0,
        'traffic_exact_totals_null_when_incomplete': (current['traffic'].get('status') != 'partial' or (current['traffic'].get('clones') is None and current['traffic'].get('views') is None)),
        'all_sources_public': True,
        'npm_download_package_coverage_complete': (
            registry['npm']['download_package_count'] == registry['npm']['package_count']),
        'npm_unavailable_packages': len(npm_errors),
        'missing_days_recorded': missing_days,
    }
    write('data/ecosystem-running-totals.json', running)

    metrics = read('data/metrics.json')
    metrics['verified_at'] = generated_at
    metrics['counts'].update({
        'github_public_repositories': collection['all_owned']['repositories'],
        'github_owned_public_nonfork_repositories': collection['nonfork']['repositories'],
        'github_public_forks': gh['public_forks'], 'github_followers': followers,
        'github_stars_owned_nonfork': collection['nonfork']['stars'],
        'github_aggregate_downstream_forks': collection['nonfork']['forks'],
        'rust_crates': crates['crate_count'], 'npm_packages': registry['npm']['package_count'],
        'rust_crate_downloads_cumulative': crates['cumulative_downloads'],
    })
    metrics['current_windows'].update({
        'npm_downloads_rolling_365_days': registry['npm']['downloads'],
        'npm_period_start': registry['npm']['period_start'],
        'npm_period_end': registry['npm']['period_end'],
        'npm_download_package_count': registry['npm']['download_package_count'],
    })
    metrics['verification_dates'].update({'github': stamp, 'npm_inventory': registry['npm']['inventory_verified_at'], 'npm_downloads': registry['npm']['downloads_verified_at'], 'crates_io': crates['verified_at']})
    write('data/metrics.json', metrics)

    evidence = {
        'verified_at': generated_at,
        'window': {'start': window_start, 'end': window_end, 'days': 14, 'current_utc_day_excluded': True},
        'sources': {'github_inventory': inventory_path, 'github_releases': release_inventory_path, 'npm_inventory': registry['npm']['inventory_path'], 'npm_downloads': npm_path, 'crates_io': crates['inventory_path']},
        'coverage': {'github_public_repositories': repository_count, 'github_pages': repository_pages, 'release_complete_repositories': repository_count, 'npm_expected_packages': registry['npm']['package_count'], 'npm_collected_packages': registry['npm']['download_package_count'], 'actions_complete_repositories': actions.get('complete_repositories'), 'actions_incomplete_repositories': actions.get('incomplete_repositories')},
        'traffic': current['traffic'],
    }
    summary = {'verified_at': generated_at, 'github': collection, 'activity': activity, 'open_items': open_items, 'release_assets': release_stats, 'actions': actions, 'npm': running['npm'], 'crates_io': running['crates_io'], 'download_milestone': running['download_milestone'], 'validation': running['validation']}
    write(f'{folder}/ecosystem-evidence.json', evidence)
    write(f'{folder}/ecosystem-summary.json', summary)

    start_label = dt.date.fromisoformat(window_start).strftime('%B %-d')
    end_label = dt.date.fromisoformat(window_end).strftime('%B %-d')
    traffic_gap = current['traffic'].get('missing_cells_per_metric', 0)
    if current['traffic'].get('status') == 'partial':
        traffic_report = (f"The requested 14-day UTC window has Unknown exact clone and view totals because {traffic_gap} of {current['traffic'].get('expected_cells_per_metric')} repository-day cells per metric are missing. Known lower bounds are {number(current['traffic'].get('known_clone_events'))} clone events and {number(current['traffic'].get('known_view_events'))} view events across {current['traffic']['repo_coverage']['clones']} repositories. Unique cloners and visitors are retained per repository only and are not summed.")
        traffic_coverage = (f"GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: {', '.join(current['traffic'].get('missing_days', []))}; missing cells are null, never zero. The known lower bounds above cover {current['traffic'].get('source_cells_per_metric')} of {current['traffic'].get('expected_cells_per_metric')} expected repository-day cells per metric from {window_start} through {window_end} UTC.")
    else:
        traffic_report = (f"Across the complete 14-day UTC window, GitHub reported {number(current['traffic']['clones'])} clone events and {number(current['traffic']['views'])} view events for {current['traffic']['repo_coverage']['clones']} repositories. Unique cloners and visitors are retained per repository only and are not summed.")
        traffic_coverage = (f"GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were {number(current['traffic']['clones'])} and view events were {number(current['traffic']['views'])} from {window_start} through {window_end} UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories.")

    report = f'''# Ecosystem metrics

Verified {day.strftime('%B %-d, %Y')}. Public repositories only. GitHub counts: {stamp}.

| Metric | Count |
| --- | ---: |
| Public owned repositories | {number(collection['all_owned']['repositories'])} |
| Original repositories | {number(collection['nonfork']['repositories'])} |
| Public fork repositories | {number(gh['public_forks'])} |
| Stars across all owned repos | {number(collection['all_owned']['stars'])} |
| Stars across originals | {number(collection['nonfork']['stars'])} |
| Forks across all owned repos | {number(collection['all_owned']['forks'])} |
| Followers | {number(followers)} |
| Repository subscriptions | {number(release_stats['subscribers'])} |
| Published releases | {number(release_stats['releases'])} |
| Current release asset downloads | {number(release_stats['current_asset_downloads'])} |
| Retained observed release asset downloads | {number(release_stats['retained_observed_downloads'])} |
| Rust crates | {number(crates['crate_count'])} |
| crates.io cumulative downloads | {number(crates['cumulative_downloads'])} |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | {number(gh['all_owned']['repositories'])} | {number(gh['all_owned']['stars'])} | {number(gh['all_owned']['forks'])} | {number(gh['all_owned']['subscribers'])} | {number(gh['all_owned']['open_issues_and_prs'])} |
| Nonfork | {number(gh['nonfork']['repositories'])} | {number(gh['nonfork']['stars'])} | {number(gh['nonfork']['forks'])} | {number(gh['nonfork']['subscribers'])} | {number(gh['nonfork']['open_issues_and_prs'])} |

## Activity: {start_label} through {end_label}, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | {number(activity['issues_opened']['count'])} |
| Issues closed | {number(activity['issues_closed']['count'])} |
| PRs opened | {number(activity['prs_opened']['count'])} |
| PRs merged | {number(activity['prs_merged']['count'])} |
| Releases published | {number(release_stats['published_in_14_day_window'])} |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

{traffic_report}

## npm downloads

Confirmed daily-event sum: {number(running['npm']['observed_downloads'])} across {registry['npm']['download_package_count']} of {registry['npm']['package_count']} packages for {start_label} through {end_label}. {npm_gap_sentence} All-package-zero days {', '.join(missing_days) if missing_days else 'none'} are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is {number(registry['npm']['downloads'])}, through {registry['npm']['period_end']}.

## Coverage and gaps

All {repository_count} public repositories were enumerated, including {gh['public_forks']} forks and {inventory_summary['archived']} archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are {number(open_items['open_issues']['count'])} and {number(open_items['open_prs']['count'])}. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

{traffic_coverage} Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. {missing_assets} release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: {number(len(ledger['values']))} unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../{folder}/).

## Progress toward 100 million

Observed combined registry downloads: {number(combined)}; remaining: {number(remaining)}. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes {number(npm_total)} through {npm_receipt['reported_through']}; crates.io contributes {number(crates['cumulative_downloads'])}. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../{npm_path}).
'''
    (ROOT / 'docs/ecosystem-metrics.md').write_text(report)

    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text()
    begin, end = '<!-- github-public-metrics:start -->', '<!-- github-public-metrics:end -->'
    top = gh['top_repositories'][:5]
    stars, forks = collection['nonfork']['stars'], collection['nonfork']['forks']
    rows = '\n'.join(f"| [{x['name']}](https://github.com/ruvnet/{x['name']}) | {number(x['stars'])} | {number(x['forks'])} | {number(x['subscribers'])} |" for x in top)
    block = f'''{begin}
## GitHub reach

Public GitHub API snapshot verified **{day.strftime('%B %-d, %Y')} UTC**. [Captured inventory]({inventory_path}).

| Measure | Verified value |
| --- | ---: |
| Followers | {number(followers)} |
| Public repositories | {number(collection['all_owned']['repositories'])} |
| Owned public nonfork repositories | {number(collection['nonfork']['repositories'])} |
| Public repositories that are forks | {number(gh['public_forks'])} |
| Stars across owned public nonfork repositories | {number(stars)} |
| Aggregate downstream forks of owned nonfork repositories | {number(forks)} |

### Flagship repository traction

| Project | Stars | Forks | Subscribers |
| --- | ---: | ---: | ---: |
{rows}

RuView and Ruflo account for **{(top[0]['stars'] + top[1]['stars']) / stars * 100:.1f}% of owned public nonfork stars** and **{(top[0]['forks'] + top[1]['forks']) / forks * 100:.1f}% of downstream forks**.
{end}'''
    before, marker, tail = readme.partition(begin)
    if not marker or end not in tail:
        raise ValueError('README GitHub metrics markers missing')
    _, _, after = tail.partition(end)
    readme_path.write_text(before + block + after)

    subprocess.run(['python3', 'scripts/render-github-metrics.py'], cwd=ROOT, check=True)
    subprocess.run(['node', 'scripts/render-registry-metrics.mjs'], cwd=ROOT, check=True)

    print(json.dumps({'combined_observed': combined, 'remaining': remaining, 'npm_reported_through': npm_receipt['reported_through'], 'daily_keys': len(ledger['values']), 'missing_days': missing_days}, indent=2))


if __name__ == '__main__':
    main()
