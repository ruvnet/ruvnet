#!/usr/bin/env python3
"""Render the profile SVG from published repository snapshots. No network access."""
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
def read(name):
    return json.loads((ROOT / name).read_text())
def date(value, fmt='%b %d'):
    return datetime.fromisoformat(value[:10]).strftime(fmt).upper()
def render():
    m = read('data/metrics.json'); r = read('data/registry-stats.json')
    g = read('data/github-stats.json')
    b = read('data/snapshots/2026-10-02/github-baseline-2026-09-07.json')
    n = r['npm']; a = g['account']; c = m['counts']
    root = ET.parse(ROOT / 'scripts/templates/ruvnet-dashboard.svg').getroot()
    def put(x, y, value):
        matches = [e for e in root.iter(f'{{{NS}}}text') if e.get('x') == str(x) and e.get('y') == str(y)]
        assert len(matches) == 1, (x,y,len(matches))
        matches[0].text = str(value)
    gd, rd, bd = date(g['verified_at']), date(r['generated_at']), date(b['verified_at'])
    root.find(f'{{{NS}}}title').text = 'rUv ecosystem dashboard · published repository evidence'
    root.find(f'{{{NS}}}desc').text = f"{n['downloads']:,} npm download events across {n['download_package_count']} packages, {n['period_start']} through {n['period_end']}. GitHub verified {g['verified_at'][:10]}; registries generated {r['generated_at'][:10]}. Star traces connect two measured snapshots and are not daily histories. Animation is decorative."
    put(34,127,f"{n['package_count']} npm packages · {r['crates_io']['crate_count']} Rust crates · at least {c['published_registry_and_huggingface_artifacts_minimum']} published artifacts")
    put(1045,47,'PUBLISHED REPO SNAPSHOT')
    put(34,182,f"NPM DOWNLOADS / {n['period_days']} DAYS")
    put(34,222,f"{n['downloads']:,}")
    put(34,248,f"{n['download_package_count']} PKGS · {n['period_start']} → {n['period_end']}")
    put(334,182,'STARS / NONFORK REPOS')
    put(334,222,f"{a['stars_across_owned_nonfork']:,}")
    put(334,248,f"{a['owned_public_nonfork_repositories']} NONFORK REPOS · {gd}")
    put(634,222,f"{a['public_repositories']:,}")
    put(634,248,f"INCLUDING {a['public_forks']} FORKS")
    put(934,222,f"{a['followers']:,}")
    put(934,248,f'GITHUB / RUVNET · {gd}')
    put(34,301,f"NPM / MONTHLY DOWNLOADS · {n['download_package_count']} PACKAGES")
    months=n['monthly_downloads']
    # The published schema stores a list of month/download records.
    if isinstance(months,dict): months=[{'month':k,'downloads':v} for k,v in sorted(months.items())]
    assert len(months)>1 and all(x['downloads']>=0 for x in months)
    top=max(1_000_000, math.ceil(max(x['downloads'] for x in months)/1_000_000)*1_000_000)
    for i,y in enumerate([340,405,470,535]): put(34,y,f'{top*(3-i)/3/1e6:.1f}M')
    points=[(62+667*i/(len(months)-1),531-195*x['downloads']/top) for i,x in enumerate(months)]
    path='M'+'L'.join(f'{x:.2f},{y:.2f}' for x,y in points)
    for e in root.iter(f'{{{NS}}}path'):
        if e.get('id')=='realchart' or e.get('class') in ('chartdraw','chartwire'): e.set('d',path)
        if e.get('class')=='chartarea': e.set('d',path+'L729,531L62,531Z')
    for parent in root.iter():
        for child in list(parent):
            if child.tag==f'{{{NS}}}circle' and child.get('class')=='capblink' and float(child.get('cx','9999'))<750:
                parent.remove(child)
    dots=ET.Element(f'{{{NS}}}g',{'aria-hidden':'true'})
    loader=next(e for e in root if e.get('class')=='gameboot')
    root.insert(list(root).index(loader),dots)
    for i,(x,y) in enumerate(points):
        ET.SubElement(dots,f'{{{NS}}}circle',{'class':'capblink','style':f'animation-delay:-{i*.35:.2f}s','cx':f'{x:.2f}','cy':f'{y:.2f}','r':'2','fill':'#ffd1a7'})
    for e in root.iter(f'{{{NS}}}circle'):
        if e.get('class')=='ring' and e.get('cx')=='729.00': e.set('cy',f'{points[-1][1]:.2f}')
    for e in root.iter():
        if e.get('class')=='panelglow': e.set('opacity','0')
    put(734,301,f'{len(months)} MONTHS / UTC')
    put(731,561,f"{date(n['monthly_period_start'],'%b %Y')} → {date(n['monthly_period_end'],'%b %Y')}")
    put(1166,548,f"{r['crates_io']['cumulative_downloads']:,}")
    put(1166,610,f'TWO SNAPSHOTS · {bd} → {gd} · TRACES NORMALIZED')
    now={x['name'].lower():x['stars'] for x in g['flagships']}
    before={x['name'].lower():x['stars'] for x in b['flagships']}
    for i,name in enumerate(['ruflo','ruvector','ruview','metaharness']):
        x=34+300*i; end=x+230; old=before[name]; new=now[name]; delta=new-old
        put(end,641,f'{delta/old:+.1%}' if old else 'N/A')
        put(x,666,f'{new:,} ★');put(end,665,f'{delta:+,} stars')
        put(x,733,f'{bd} / {old:,}');put(end,733,f'{gd} / {new:,}')
        # Two endpoints, independently normalized per panel; no invented observations.
        if delta<=0:
            start_y=708 if delta==0 else 686
            for e in root.iter():
                if e.tag==f'{{{NS}}}path' and e.get('d','').startswith(f'M{40+300*i} 708L{254+300*i} 686'):
                    e.set('d',e.get('d').replace(f'M{40+300*i} 708L{254+300*i} 686',f'M{40+300*i} {start_y}L{254+300*i} 708'))
                if e.tag==f'{{{NS}}}circle' and e.get('cx')==str(254+300*i) and e.get('cy')=='686': e.set('cy','708')
                if e.tag==f'{{{NS}}}circle' and e.get('cx')==str(40+300*i) and e.get('cy')=='708': e.set('cy',str(start_y))
    # Animated markers only traverse decorative paths, never imply measurements.
    for parent in root.iter():
        for child in list(parent):
            if child.get('class')=='historydot': parent.remove(child)
    put(54,784,f'GITHUB: {g["verified_at"][:10]} · REGISTRIES: {r["generated_at"][:10]}')
    put(600,757,f'REPO SNAPSHOT · GITHUB {gd} · REGISTRIES {rd}')
    out=ROOT/'assets/ruvnet/dashboard.svg';out.parent.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(root).write(out,encoding='unicode')
    print(f'Rendered {out.relative_to(ROOT)} from repository JSON')
if __name__=='__main__': render()
