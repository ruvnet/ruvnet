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
def render_growth(n):
    from itertools import accumulate
    from html import escape
    rows=n['monthly_downloads']; cumulative=list(accumulate(row['downloads'] for row in rows))
    total=cumulative[-1]; ceiling=max(20_000_000,math.ceil(total/20_000_000)*20_000_000)
    points=[(80+i*1010/(len(rows)-1),425-235*v/ceiling) for i,v in enumerate(cumulative)]
    d='M'+'L'.join(f'{x:.2f} {y:.2f}' for x,y in points)
    ratio=rows[-1]['downloads']/rows[0]['downloads'] if rows[0]['downloads'] else None
    def text(x,y,value,size=13,color='#95aabe',anchor='start'):
        return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(str(value))}</text>'
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="550" viewBox="0 0 1200 550" role="img" aria-labelledby="title desc"><title id="title">Cumulative npm download growth</title><desc id="desc">{total:,} download events summed from {n['monthly_period_start']} through {n['monthly_period_end']}. Linear scale, month end observations. This is period cumulative, not lifetime downloads.</desc><defs><linearGradient id="line"><stop stop-color="#9de8d0"/><stop offset="1" stop-color="#ffae73"/></linearGradient><linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#f69a62" stop-opacity=".3"/><stop offset="1" stop-color="#f69a62" stop-opacity=".01"/></linearGradient><clipPath id="reveal"><rect class="reveal" x="75" y="180" width="1030" height="250"/></clipPath></defs><style>text{{font-family:ui-monospace,Consolas,monospace}}.reveal{{animation:reveal 10s cubic-bezier(.25,.1,.25,1) infinite;transform-origin:75px 0}}.energy{{stroke-dasharray:8 110;animation:flow 5s linear infinite}}.pulse{{animation:pulse 3s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}@keyframes reveal{{0%,5%{{transform:scaleX(0)}}70%,100%{{transform:scaleX(1)}}}}@keyframes flow{{to{{stroke-dashoffset:-236}}}}@keyframes pulse{{50%{{opacity:.35;transform:scale(1.4)}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><rect width="1200" height="550" rx="16" fill="#080e19"/><rect x=".5" y=".5" width="1199" height="549" rx="16" fill="none" stroke="#26354b"/>'''
    s+=text(34,36,'RUVNET / NPM DOWNLOAD GROWTH',13,'#9de8d0')+text(34,91,f'{total:,}',46,'#eef5ff')+text(36,120,'CUMULATIVE DOWNLOAD EVENTS IN THIS PERIOD',12)
    s+=text(1164,67,f'{ratio:.1f}×' if ratio is not None else 'N/A',35,'#ffae73','end')+text(1164,93,'LAST MONTH / FIRST MONTH VOLUME',11,anchor='end')
    s+=text(34,156,f"{n['monthly_period_start']} → {n['monthly_period_end']}  ·  {n['download_package_count']} PACKAGE COHORT",12)
    s+=text(1164,156,'LINEAR SCALE · MONTH END TOTALS',10,anchor='end')
    for i in range(6):
        y=425-235*i/5;s+=f'<path d="M80 {y}H1090" stroke="#1c2b3d"/>'+text(67,y+4,f'{ceiling*i/5/1e6:.0f}M',11,anchor='end')
    s+=f'<path d="{d}" fill="none" stroke="#314351" stroke-width="1.5"/><g clip-path="url(#reveal)"><path d="{d}L1090 425L80 425Z" fill="url(#area)"/><path id="cumulative-line" d="{d}" fill="none" stroke="url(#line)" stroke-width="3.5"/><path class="energy" d="{d}" fill="none" stroke="#fff4dc" stroke-width="2"/>'
    for (x,y),row,total_at_month in zip(points,rows,cumulative):
        s+=f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="#e4ffef"><title>{row["month"]}: {total_at_month:,} cumulative; {row["downloads"]:,} this month</title></circle>'
    s+='</g>'
    x,y=points[-1];s+=f'<circle class="pulse" cx="{x:.2f}" cy="{y:.2f}" r="8" fill="none" stroke="#ffae73"/>'+text(x-12,y-16,f'{total/1e6:.2f}M',14,'#ffc295','end')
    for (x,y),row in zip(points,rows):
        s+=text(x,451,date(row['month']+'-01','%b'),11,anchor='middle')
    s+=text(80,470,rows[0]['month'][:4],10)+text(1090,470,rows[-1]['month'][:4],10,anchor='end')
    s+=text(34,508,f"SOURCE: REPO REGISTRY JSON · VERIFIED {n['downloads_verified_at'][:10]}",11)+text(34,529,'Sum of measured calendar months. Download events include CI and reinstalls; not unique users.',11)
    s+='</svg>'
    ET.fromstring(s)
    (ROOT/'assets/ruvnet/npm-cumulative-growth.svg').write_text(s)

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
    put(34,301,f"NPM / CUMULATIVE DOWNLOADS · {n['download_package_count']} PACKAGES")
    months=n['monthly_downloads']
    # The published schema stores a list of month/download records.
    if isinstance(months,dict): months=[{'month':k,'downloads':v} for k,v in sorted(months.items())]
    assert len(months)>1 and all(x['downloads']>=0 for x in months)
    from itertools import accumulate
    totals=list(accumulate(x['downloads'] for x in months))
    top=max(1_000_000, math.ceil(totals[-1]/1_000_000)*1_000_000)
    for i,y in enumerate([340,405,470,535]): put(34,y,f'{top*(3-i)/3/1e6:.1f}M')
    points=[(62+667*i/(len(months)-1),531-195*value/top) for i,value in enumerate(totals)]
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
    put(734,301,'')
    put(62,561,'PERIOD CUMULATIVE · NOT LIFETIME')
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
    render_growth(n)
    print(f'Rendered {out.relative_to(ROOT)} and cumulative chart from repository JSON')
if __name__=='__main__': render()
