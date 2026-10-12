#!/usr/bin/env python3
"""Reconcile profile claims from a complete dated public GitHub inventory."""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def reconcile(github, inventory):
    rows = inventory['repositories']
    user = inventory['user']
    assert user['login'] == 'ruvnet'
    assert len(rows) == user['public_repos'] == len({r['id'] for r in rows})
    assert all(r['full_name'].startswith('ruvnet/') and not r.get('private', False) for r in rows)
    owned = [r for r in rows if not r['fork']]
    github['account'] = {
        'followers': user['followers'], 'public_repositories': len(rows),
        'owned_public_nonfork_repositories': len(owned), 'public_forks': len(rows)-len(owned),
        'stars_across_owned_nonfork': sum(r['stargazers_count'] for r in owned),
        'aggregate_downstream_forks_of_owned_nonfork': sum(r['forks_count'] for r in owned),
    }
    by_name = {r['full_name'].split('/')[1].lower(): r for r in rows}
    for flagship in github['flagships']:
        row = by_name[flagship['name'].lower()]
        assert isinstance(row.get('subscribers_count'), int), 'Flagship subscriber evidence required'
        flagship.update(stars=row['stargazers_count'], forks=row['forks_count'],
                        watchers=row['subscribers_count'])
    leaders = [by_name[name] for name in ('ruview', 'ruflo')]
    github['concentration'] = {
        'two_flagship_share_of_owned_nonfork_stars': sum(r['stargazers_count'] for r in leaders)/github['account']['stars_across_owned_nonfork'],
        'two_flagship_share_of_aggregate_forks': sum(r['forks_count'] for r in leaders)/github['account']['aggregate_downstream_forks_of_owned_nonfork'],
    }
    return github


def main():
    path = ROOT/'data/github-stats.json'
    github = json.loads(path.read_text())
    inventory = json.loads((ROOT/github['inventory']).read_text())
    reconcile(github, inventory)
    path.write_text(json.dumps(github, indent=2)+'\n')
    running_path=ROOT/'data/ecosystem-running-totals.json'
    if running_path.exists():
        running=json.loads(running_path.read_text())
        running['github']=github['current_collection']
        running['verified_at']=max(running['verified_at'],github['verified_at'])
        running_path.write_text(json.dumps(running,indent=2)+'\n')
    metrics_path = ROOT/'data/metrics.json'
    metrics = json.loads(metrics_path.read_text())
    keys = {'followers':'github_followers', 'public_repositories':'github_public_repositories',
            'owned_public_nonfork_repositories':'github_owned_public_nonfork_repositories',
            'public_forks':'github_public_forks', 'stars_across_owned_nonfork':'github_stars_owned_nonfork',
            'aggregate_downstream_forks_of_owned_nonfork':'github_aggregate_downstream_forks'}
    for key, target in keys.items():metrics['counts'][target]=github['account'][key]
    metrics['verification_dates']['github']=github['verified_at']
    metrics['verified_at']=max(metrics['verified_at'],github['verified_at'])
    metrics_path.write_text(json.dumps(metrics,indent=2)+'\n')
    account=github['account'];f=lambda value:f'{value:,}'
    day=dt.date.fromisoformat(github['verified_at'][:10])
    labels=['Followers','Public repositories','Owned public nonfork repositories','Public repositories that are forks','Stars across owned public nonfork repositories','Aggregate downstream forks of owned nonfork repositories']
    counts='\n'.join(f'| {label} | {f(value)} |' for label,value in zip(labels,account.values()))
    rows='\n'.join(f"| [{x['name']}](https://github.com/ruvnet/{x['name']}) | {f(x['stars'])} | {f(x['forks'])} | {f(x['watchers'])} |" for x in github['flagships'])
    concentration=github['concentration']
    block=f'''<!-- github-public-metrics:start -->
## GitHub reach

Public GitHub API snapshot verified **{day.strftime('%B %-d, %Y')} UTC**. [Captured inventory]({github['inventory']}).

| Measure | Verified value |
| --- | ---: |
{counts}

### Flagship repository traction

| Project | Stars | Forks | Subscribers |
| --- | ---: | ---: | ---: |
{rows}

RuView and Ruflo account for **{concentration['two_flagship_share_of_owned_nonfork_stars']:.1%} of owned public nonfork stars** and **{concentration['two_flagship_share_of_aggregate_forks']:.1%} of downstream forks**.
<!-- github-public-metrics:end -->'''
    readme=ROOT/'README.md';text=readme.read_text()
    before, marker, tail=text.partition('<!-- github-public-metrics:start -->')
    assert marker and '<!-- github-public-metrics:end -->' in tail
    readme.write_text(before+block+tail.split('<!-- github-public-metrics:end -->',1)[1])
    print('Reconciled GitHub account, flagships, metrics and README from '+github['inventory'])


if __name__=='__main__':main()
