#!/usr/bin/env python3
"""Build self-contained animated SVG chapter banners and a conceptual ecosystem map."""
from pathlib import Path
from html import escape
import math
OUT=Path(__file__).resolve().parents[1]/'assets/ruvnet'
OUT.mkdir(parents=True,exist_ok=True)
CSS='''text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.signal{stroke-dasharray:3 13;animation:signal 5s linear infinite}.orbit{animation:turn 32s linear infinite;transform-box:fill-box;transform-origin:center}.reverse{animation-direction:reverse;animation-duration:47s}.pulse{animation:pulse 4s ease-in-out infinite}.draw{stroke-dasharray:900;animation:draw 9s ease-in-out infinite}.float{animation:float 6s ease-in-out infinite}@keyframes signal{to{stroke-dashoffset:-160}}@keyframes turn{to{transform:rotate(360deg)}}@keyframes pulse{50%{opacity:.3}}@keyframes draw{0%{stroke-dashoffset:900}60%,100%{stroke-dashoffset:0}}@keyframes float{50%{transform:translateY(-5px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}'''
CSS += """
.sonar{animation:sonar 4s ease-out infinite;transform-origin:0 0}.layer{animation:layer 5s ease-in-out infinite}.route{stroke-dasharray:8 75;animation:route 3s linear infinite}.sweep{animation:turn 6s linear infinite;transform-origin:0 0}.gate{animation:gate 5s ease-in-out infinite}.scanline{animation:scanline 6s ease-in-out infinite}.glint{animation:glint 6s ease-in-out infinite}.satellite{animation:turn 9s linear infinite;transform-origin:0 0}.satellite.reverse{animation-direction:reverse;animation-duration:13s}
@keyframes sonar{0%{transform:scale(.4);opacity:0}20%{opacity:.7}100%{transform:scale(1.7);opacity:0}}
@keyframes layer{50%{transform:translateY(-6px)}}
@keyframes route{to{stroke-dashoffset:-166}}
@keyframes gate{0%,20%,85%,100%{opacity:.2}40%,65%{opacity:1}}
@keyframes scanline{0%,100%{transform:translateX(0);opacity:0}15%,85%{opacity:.5}90%{transform:translateX(230px);opacity:0}}
@keyframes glint{0%,25%,100%{opacity:.1}45%,65%{opacity:.8}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}.sonar,.scanline{display:none}}
"""
CSS += """
.edgeglow{stroke-dasharray:10 90;animation:edgeglow 9s linear infinite}.sheen{animation:sheen 11s ease-in-out infinite;opacity:0}.iconhalo{animation:iconhalo 5s ease-in-out infinite}.beacon{animation:beacon 4s ease-in-out infinite}.chevron{animation:chevron 3s ease-in-out infinite}.highlight{animation:highlight 6s ease-in-out infinite}
@keyframes edgeglow{to{stroke-dashoffset:-100}}
@keyframes sheen{0%,15%{transform:translateX(-200px);opacity:0}25%{opacity:.07}65%{transform:translateX(var(--travel));opacity:.07}75%,100%{transform:translateX(var(--travel));opacity:0}}
@keyframes iconhalo{50%{opacity:.18}}
@keyframes beacon{50%{opacity:.35}}
@keyframes chevron{50%{transform:translateX(5px)}}
@keyframes highlight{0%,100%{stroke-opacity:.2}50%{stroke-opacity:.8}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}.sheen,.edgeglow{display:none}}
"""
def start(w,h,title,desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#163047" stroke-opacity=".3"/></pattern><radialGradient id="halo"><stop stop-color="#233759"/><stop offset="1" stop-color="#080e19"/></radialGradient><linearGradient id="sheen"><stop stop-color="#9de8d0" stop-opacity="0"/><stop offset=".5" stop-color="#d5eaff"/><stop offset="1" stop-color="#a5b5ff" stop-opacity="0"/></linearGradient><clipPath id="panelclip"><rect width="{w}" height="{h}" rx="14"/></clipPath></defs><style>{CSS}</style><rect width="{w}" height="{h}" rx="14" fill="#080e19"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/><g clip-path="url(#panelclip)" aria-hidden="true"><rect class="sheen" opacity="0" style="--travel:{w+200}px" x="-180" width="180" height="{h}" fill="url(#sheen)"/><rect class="edgeglow" x="1" y="1" width="{w-2}" height="{h-2}" rx="14" pathLength="100" stroke="#9de8d0" stroke-opacity=".55" fill="none"/></g>'''
def txt(x,y,s,size=14,color='#a7b8ce',anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>'
def icon(kind,color):
    common=f'fill="none" stroke="{color}" stroke-width="1.5"'
    shapes={
    'sense':'<circle r="25"/><circle r="16" stroke-dasharray="3 6"/><path d="M-32 0H32M0-32V32M0 0L22-22"/><circle cx="13" cy="-12" r="3" fill="currentColor"/>',
    'memory':'<path d="M-28-12L0-27 28-12 0 3ZM-28-2L0 13 28-2M-28 9L0 24 28 9M-28 20L0 35 28 20"/><path class="signal" d="M0-27V35"/>',
    'agents':'<path d="M0-20V0M0 0L-26 23M0 0L26 23M-26 23H26"/><circle cy="-24" r="7"/><circle cx="-26" cy="23" r="7"/><circle cx="26" cy="23" r="7"/><circle r="5"/>',
    'runtime':'<path d="M0-30L27-15V15L0 30-27 15V-15ZM-27-15L0 0 27-15M0 0V30"/><path class="signal" d="M0-30V0L-27 15"/>',
    'evaluate':'<path d="M-28-27V27H30M-20 14L-8 2 4 8 25-16"/><circle cx="25" cy="-16" r="6"/><path d="M-20-20H5M-20-12H-4"/>',
    'proof':'<path d="M0-30L25-20V3Q25 22 0 32Q-25 22-25 3V-20ZM-12 0L-2 10 15-10"/>'}
    art='<circle class="iconhalo" r="39" fill="currentColor" fill-opacity=".06" stroke="none"/>'+shapes[kind]
    if kind=='sense':
        art+='<circle class="sonar" r="25"/><circle class="sonar" style="animation-delay:-2s" r="25"/><g class="sweep"><path d="M0 0L29-18A34 34 0 0 1 34 0Z" fill="currentColor" fill-opacity=".2" stroke="none"/></g>'
    elif kind=='memory':
        art='<g class="layer">'+art+'</g><path class="route" d="M-28 20L0 35 28 20M-28-12L0-27 28-12" stroke-width="3"/><circle class="gate" cy="4" r="4" fill="currentColor"/>'
    elif kind=='agents':
        art+='<path class="route" d="M0-24V0L-26 23H26L0 0" stroke-width="3"/><circle class="sonar" r="12"/><circle class="gate" cx="26" cy="23" r="4" fill="currentColor"/>'
    elif kind=='runtime':
        art='<g class="layer">'+art+'<path class="gate" d="M0-30L27-15 0 0-27-15Z" fill="currentColor" fill-opacity=".2"/></g><ellipse class="pulse" cy="36" rx="33" ry="7"/>'
    elif kind=='evaluate':
        art+='<path class="route" d="M-20 14L-8 2 4 8 25-16" stroke-width="3"/><circle class="sonar" cx="25" cy="-16" r="8"/>'
    else:
        art+='<path class="draw" d="M-12 0L-2 10 15-10" stroke-width="3"/><path class="route" d="M0-30L25-20V3Q25 22 0 32Q-25 22-25 3V-20Z"/>'
    return f'<g {common} color="{color}">{art}</g>'

headers=[('constellation','01','A constellation of capabilities','Explore the systems and their roles','runtime','#a5b5ff'),('journey','02','From signal to useful work','Perceive / remember / coordinate / execute / evaluate','sense','#f6a675'),('build','03','Choose your entry point','Start with a task. Follow the evidence.','agents','#9de8d0'),('evidence','04','Reach, with receipts','Published snapshots / explicit windows / reproducible sources','proof','#a5b5ff'),('evolution','05','An ecosystem in motion','New systems, deeper capabilities, preserved provenance','evaluate','#f6a675'),('memory','06','Memory that travels','State / evidence / portable execution','memory','#9de8d0')]
for name,num,title,sub,kind,color in headers:
    s=start(1200,132,title,sub)
    s+=f'<path d="M24 112H1176" stroke="#23334c"/><path class="signal" d="M24 112H1176" stroke="{color}"/>'
    s+=txt(28,38,f'RUVNET / {num}',11,color)+txt(28,72,title,27,'#ecf3ff')+txt(28,96,sub,12)
    s+=f'<g transform="translate(1100 62)"><circle r="46" stroke="{color}" stroke-opacity=".15" fill="none"/><g class="orbit"><circle r="42" stroke="{color}" stroke-dasharray="40 15 2 15" fill="none"/></g>'+icon(kind,color)+'</g></svg>'
    (OUT/f'{name}.svg').write_text(s)
s=start(1200,660,'The rUv constellation','Conceptual relationships between sensing, memory, coordination, execution, evaluation, and governed adaptation. Links illustrate roles, not guaranteed integrations or live telemetry.')
s+=txt(30,40,'RUV / SYSTEMS CONSTELLATION',14,'#dce9ff')+txt(1170,40,'ROLE MAP · NOT LIVE TELEMETRY',10,anchor='end')
s+='<ellipse cx="600" cy="330" rx="400" ry="220" fill="none" stroke="#20304a" stroke-dasharray="2 8"/><ellipse cx="600" cy="330" rx="310" ry="175" fill="none" stroke="#1b2940"/>'
nodes=[(210,175,'PERCEIVE','RuView · rvCSI · RuField','Spatial observations','sense','#f6a675'),(600,125,'REMEMBER','RuVector · AgentDB · AgenticOW','Vector, graph and episodic memory','memory','#9de8d0'),(990,175,'COORDINATE','Ruflo','Agents, tasks and shared context','agents','#a5b5ff'),(990,480,'EXECUTE','RVF · RVForge · RVM','Portable state and capability controls','runtime','#9de8d0'),(600,545,'EVALUATE','MetaHarness · APx','Changes, outcomes and useful work','evaluate','#f6a675'),(210,480,'ADAPT','Autogenous · Dream Machine','Proposals and promotion boundaries','proof','#a5b5ff')]
for i,(x,y,role,names,sub,kind,color) in enumerate(nodes):
    d=f'M600 330Q{(600+x)/2+35} {(330+y)/2} {x} {y}'
    s+=f'<path d="{d}" fill="none" stroke="#2a3b53"/><path class="signal" style="animation-delay:-{i*.7}s" d="{d}" fill="none" stroke="{color}"/>'
s+='<circle cx="600" cy="330" r="100" fill="url(#halo)"/><g transform="translate(600 330)">'
for r,cl,col in [(93,'orbit','#a5b5ff'),(78,'orbit reverse','#9de8d0'),(64,'pulse','#f6a675')]:
    s+=f'<circle class="{cl}" r="{r}" fill="none" stroke="{col}" stroke-opacity=".65" stroke-dasharray="36 9 2 9"/>'
s+=txt(0,-4,'rUv',32,'#edf5ff','middle')+txt(0,20,'ECOSYSTEM',11,'#9de8d0','middle')+'</g>'
for i,(x,y,role,names,sub,kind,color) in enumerate(nodes):
    s+=f'<g transform="translate({x} {y})"><rect x="-164" y="-73" width="328" height="146" rx="12" fill="#0c1422" stroke="#26364d"/><path d="M-148-73H-110M148 73H110" stroke="{color}" stroke-width="2"/><g transform="translate(-120 -26)">'+icon(kind,color)+'</g>'
    s+=txt(-70,-33,f'0{i+1} / {role}',13,color)+txt(-70,-10,'CONNECTED CAPABILITY',9)
    s+=txt(0,29,names,14,'#edf3fd','middle')+txt(0,52,sub,11,'#95a9c0','middle')+'</g>'
s+=txt(30,640,'Explore each project for its own interfaces, maturity and evidence.',11)+txt(1170,640,'MOTION IS DECORATIVE',10,anchor='end')+'</svg>'
(OUT/'constellation-map.svg').write_text(s)
print('Rendered six chapter headers and constellation map')

# Taller chapter art and project cards. No metrics are duplicated in these assets.
extra=[('distribution','07','Published across the stack','npm / Rust / Python / models and spaces','runtime','#9de8d0'),('provenance','08','Evidence is part of the interface','Source / snapshot / counting rule / reproducible check','proof','#a5b5ff'),('archive','09','Explore the deeper archive','Project lineage, earlier snapshots and the complete catalog','memory','#f6a675')]
for name,num,title,sub,kind,color in extra:
    s=start(1200,160,title,sub)
    s+=txt(30,35,f'RUVNET / {num}',11,color)+txt(30,78,title,29,'#edf3ff')+txt(30,109,sub,13)
    s+=f'<path d="M30 140H1170" stroke="#23344b"/><path class="signal" d="M30 140H1170" stroke="{color}"/>'
    s+=f'<g transform="translate(1100 75)"><circle class="orbit" r="55" fill="none" stroke="{color}" stroke-dasharray="30 8 2 8"/>'+icon(kind,color)+'</g></svg>'
    (OUT/f'{name}.svg').write_text(s)
projects=[('ruflo','Ruflo','COORDINATE','Bring agents, tasks and context together.','agents','#a5b5ff'),('ruvector','RuVector','REMEMBER','Vector and graph intelligence for memory.','memory','#9de8d0'),('ruview','RuView','PERCEIVE','Explore spatial intelligence through RF.','sense','#f6a675'),('metaharness','MetaHarness','EVALUATE','Make proposed improvements testable.','evaluate','#a5b5ff'),('rvf','RVF + RVM','CARRY AND EXECUTE','Portable state. Controlled execution.','runtime','#9de8d0'),('autogenous','Autogenous','ADAPT','Preserve proposals and promotion gates.','proof','#f6a675')]
projects += [
 ('agentdb','AgentDB','RETAIN','Persistent memory for agent workflows.','memory','#9de8d0'),
 ('agenticow','AgenticOW','BRANCH','Explore branchable agent memory.','memory','#a5b5ff'),
 ('rvcsi','rvCSI','OBSERVE','Explore wireless channel observations.','sense','#f6a675'),
 ('rufield','RuField','INTERPRET','Explore spatial and multimodal evidence.','sense','#9de8d0'),
 ('dream-machine','Dream Machine','REVIEW','Connect proposals, evaluation and outcomes.','agents','#a5b5ff'),
 ('apx','APx','MEASURE','Measure useful accepted work.','evaluate','#f6a675')]
for index,(slug,name,role,sub,kind,color) in enumerate(projects):
    s=start(580,270,name,sub)
    s+=f'<path d="M20 20H48M20 20V48M560 250H532M560 250V222" fill="none" stroke="{color}"/>'
    s+=txt(32,43,f'0{index+1} / {role}',12,color)+txt(32,94,name,32,'#edf3ff')+txt(32,132,sub,12)
    s+=txt(32,243,'EXPLORE PROJECT',12,color)
    s+=f'<g transform="translate(183 237)"><path class="chevron" d="M-4-5L2 0-4 5M3-5L9 0 3 5" fill="none" stroke="{color}"/></g><path class="highlight" d="M32 105H208" stroke="{color}" stroke-width="2"/><circle class="beacon" cx="548" cy="32" r="3" fill="{color}"/>'
    s+=f'<g transform="translate(492 76)"><circle class="orbit" r="47" fill="none" stroke="{color}" stroke-opacity=".5" stroke-dasharray="25 9 2 9"/>'+icon(kind,color)+'</g>'
    # Decorative topology: layered routes, travelling highlights and phased nodes.
    s+=f'<g stroke="{color}" fill="none" opacity=".65"><path d="M34 194H120L148 170H240L270 204H380L408 178H548" stroke-opacity=".2"/><path class="route" style="animation-delay:-{index*.4}s" d="M34 194H120L148 170H240L270 204H380L408 178H548"/><path d="M34 211H166L192 187H320L348 221H548" stroke-opacity=".2"/>'
    for j,x in enumerate([120,240,380,548]):
        s+=f'<circle class="gate" style="animation-delay:-{j*.8}s" cx="{x}" cy="{194 if j==0 else 170 if j==1 else 204 if j==2 else 178}" r="3" fill="{color}"/>'
    s+='</g>'
    s+=f'<g transform="translate(492 76)"><g class="satellite"><circle cx="54" r="2.5" fill="{color}"/></g><g class="satellite reverse"><circle cy="-57" r="1.8" fill="#edf3ff"/></g></g>'
    s+=f'<path d="M260 239H548" stroke="#26364a"/><path class="signal" style="animation-delay:-{index}s" d="M260 239H548" stroke="{color}"/></svg>'
    (OUT/f'project-{slug}.svg').write_text(s)

def ribbon(filename,title,subtitle,steps):
    s=start(1200,260,title,subtitle)
    s+=txt(30,35,title,15,'#edf3ff')+txt(30,58,subtitle,11)
    for i,(label,detail,kind,color) in enumerate(steps):
        x=30+295*i
        if i<3:
            s+=f'<path class="signal" d="M{x+250} 150H{x+295}" stroke="{color}"/><path d="M{x+285} 145L{x+292} 150 {x+285} 155" fill="none" stroke="{color}"/>'
        s+=f'<rect x="{x}" y="85" width="255" height="145" rx="10" fill="#0d1726" stroke="#263b52"/>'
        s+=f'<g transform="translate({x+48} 137)">'+icon(kind,color)+'</g>'
        s+=txt(x+92,131,f'0{i+1}',11,color)+txt(x+92,156,label,17,'#eef4ff')+txt(x+16,208,detail,11)
    s+='</svg>';(OUT/filename).write_text(s)
ribbon('memory-journey.svg','MEMORY THAT CAN MOVE','Conceptual lifecycle. Follow project documentation for supported formats and interfaces.',[
 ('Remember','RuVector / persistent context','memory','#9de8d0'),('Package','RVF / state and evidence','runtime','#a5b5ff'),('Stage','RVForge / target bundles','agents','#f6a675'),('Execute','RVM / capability controls','proof','#9de8d0')])
ribbon('evidence-chain.svg','FROM SOURCE TO VISIBLE EVIDENCE','Committed snapshots keep measurement windows separate from decorative motion.',[
 ('Source','GitHub / npm / crates.io','sense','#f6a675'),('Snapshot','JSON / dates / scope','memory','#9de8d0'),('Verify','Claims / links / receipts','proof','#a5b5ff'),('Render','SVG / Markdown / workflow','evaluate','#9de8d0')])
print('Rendered project cards, lifecycle illustrations and supporting banners')

# A larger conceptual cutaway adds depth without presenting invented telemetry.
s=start(1200,400,'Inside the capability loop','Illustrated memory, coordination and evaluation roles. Motion is decorative, not measured system activity.')
s+=txt(30,36,'INSIDE THE CAPABILITY LOOP',16,'#edf3ff')+txt(1170,36,'CONCEPTUAL CUTAWAY',11,anchor='end')
for i,(title,sub,kind,color) in enumerate([('MEMORY','Retain context','memory','#9de8d0'),('COORDINATION','Route the work','agents','#a5b5ff'),('EVALUATION','Inspect the outcome','evaluate','#f6a675')]):
    x=30+i*395
    s+=f'<rect x="{x}" y="64" width="350" height="300" rx="14" fill="#0c1625" stroke="#263a51"/>'
    s+=f'<g transform="translate({x+175} 205)"><ellipse rx="134" ry="73" fill="url(#halo)" stroke="#263a51"/><ellipse class="pulse" rx="112" ry="56" fill="none" stroke="{color}" stroke-opacity=".3"/><g transform="scale(2.0)">'+icon(kind,color)+'</g>'
    s+=f'<g class="satellite"><circle cx="102" r="4" fill="{color}"/><circle cx="-102" r="2" fill="{color}"/></g></g>'
    s+=txt(x+22,95,f'0{i+1} / {title}',13,color)+txt(x+175,321,sub,20,'#edf3ff','middle')
    if i<2:s+=f'<path class="route" d="M{x+350} 211H{x+395}" fill="none" stroke="{color}" stroke-width="2"/>'
s+=txt(30,388,'Roles connect the story. Each project documents its own supported interfaces.',11)
s+='</svg>';(OUT/'capability-cutaway.svg').write_text(s)

# Small standalone icons can also be reused in other Markdown documents.
for kind,color in [('sense','#f6a675'),('memory','#9de8d0'),('agents','#a5b5ff'),('runtime','#9de8d0'),('evaluate','#f6a675'),('proof','#a5b5ff')]:
    s=start(112,112,kind+' capability icon','Decorative animated symbol. Does not indicate service status.')
    s+='<g transform="translate(56 56)">'+icon(kind,color)+f'<g class="satellite"><circle cx="45" r="2" fill="{color}"/></g></g></svg>'
    (OUT/f'icon-{kind}.svg').write_text(s)

# Compact linked badges for the README's top navigation bar.
badges=[('ruflo','Ruflo',88,'#a5b5ff'),('ruvector','RuVector',108,'#9de8d0'),('ruview','RuView',96,'#f6a675'),('metaharness','MetaHarness',134,'#a5b5ff'),('rvf','RVF',72,'#9de8d0'),('rvm','RVM',72,'#f6a675')]
for index,(slug,label,width,color) in enumerate(badges):
    badge=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="24" viewBox="0 0 {width} 24" role="img" aria-labelledby="title"><title id="title">Explore {label}</title><style>
    text{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}}.accent{{stroke-dasharray:18 180;animation:travel 7s linear infinite;animation-delay:-{index}s}}.mark{{transform-origin:12px 12px;animation:rotate 12s linear infinite;animation-delay:-{index}s}}@keyframes travel{{to{{stroke-dashoffset:-198}}}}@keyframes rotate{{to{{transform:rotate(360deg)}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
    </style><rect x=".5" y=".5" width="{width-1}" height="23" rx="5" fill="#0c1422" stroke="#29384c"/><path d="M25 5V19" stroke="#29384c"/><path class="mark" d="M12 6L18 12 12 18 6 12Z" stroke="{color}" fill="none"/><circle cx="12" cy="12" r="1.5" fill="{color}"/><text x="34" y="16" font-size="11" fill="#e4ecf7">{label}</text><path class="accent" d="M5 23H{width-5}" stroke="{color}" stroke-width="1"/></svg>'''
    (OUT/f'badge-{slug}.svg').write_text(badge)

# Cognitum homepage hero adaptation, observed 2026-10-07.
# Source: cognitum.one, Index-BtuD0syC.css and homepage hero text.
s='''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="370" viewBox="0 0 1200 370" role="img" aria-labelledby="title desc"><title id="title">Cognitum One: Ambient Intelligence at the edge of the Physical World</title><desc id="desc">Explore Cognitum One at cognitum.one. A homepage inspired banner with teal gradients, a dark atmosphere and animated signal fields.</desc><defs><radialGradient id="bg"><stop stop-color="#0b2c35"/><stop offset="1" stop-color="#030a10"/></radialGradient><linearGradient id="world" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#a5efe4"/><stop offset=".6" stop-color="#19cddd"/><stop offset="1" stop-color="#4bc5e8"/></linearGradient><radialGradient id="glow"><stop stop-color="#19cddd" stop-opacity=".15"/><stop offset="1" stop-color="#19cddd" stop-opacity="0"/></radialGradient><linearGradient id="cta" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#b5fff0"/><stop offset="1" stop-color="#27cede"/></linearGradient><clipPath id="clip"><rect x="1" y="1" width="1198" height="368" rx="16"/></clipPath></defs><style>
text{font-family:Outfit,Inter,Arial,sans-serif}.mono{font-family:ui-monospace,Consolas,monospace}.signal{stroke-dasharray:3 22;animation:signal 9s linear infinite}.field{animation:field 8s ease-in-out infinite;transform-origin:center}.resolve{animation:resolve 1.6s ease-out both}.dot{animation:dot 4s ease-in-out infinite}.arrow{animation:arrow 3s ease-in-out infinite}.code{opacity:0;animation:code 1.6s ease-out both}@keyframes signal{to{stroke-dashoffset:-150}}@keyframes field{50%{opacity:.5;transform:translateY(-6px)}}@keyframes resolve{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}@keyframes dot{50%{opacity:.25}}@keyframes arrow{50%{transform:translateX(4px)}}@keyframes code{0%,15%{opacity:0}25%,65%{opacity:.7}100%{opacity:0}}.still{display:none}.frame{opacity:0;animation:frame 16s steps(1,end) infinite}.frame.first{opacity:1}.floor{animation:floor 8s linear infinite;transform-origin:600px 230px}.orb{animation:orbit3d 20s linear infinite;transform-origin:0 0}.breathe{animation:breathe 4s ease-in-out infinite}.ctaline{stroke-dasharray:45 620;animation:signal 6s linear infinite}@keyframes frame{0%,4.166%{opacity:1}4.167%,100%{opacity:0}}@keyframes floor{0%{transform:scaleY(.75);opacity:.1}50%{opacity:.3}100%{transform:scaleY(1.2);opacity:.1}}@keyframes orbit3d{to{transform:rotate(360deg)}}@keyframes breathe{50%{opacity:.4}}@media(prefers-reduced-motion:reduce){*{animation:none!important}.code,.motion{display:none}.still{display:inline}}
</style><rect x=".5" y=".5" width="1199" height="369" rx="16" fill="url(#bg)" stroke="#17404b"/><g clip-path="url(#clip)"><ellipse cx="270" cy="170" rx="380" ry="280" fill="url(#glow)"/><ellipse cx="940" cy="240" rx="360" ry="240" fill="url(#glow)"/>'''
# Perspective ground and preprojected rotating solids stay behind all text.
s+='<g class="floor" stroke="#2c8d9d" fill="none" opacity=".2">'
for k in range(-10,11):
    s+=f'<path d="M{600+k*24} 230L{600+k*145} 390"/>'
for y in [245,258,276,301,334,376]:
    s+=f'<path d="M0 {y}H1200"/>'
s+='</g>'
for side,cx in enumerate([930]):
    s+=f'<g transform="translate({cx} 177)"><ellipse rx="270" ry="195" fill="url(#glow)"/><g transform="rotate(-24) scale(1 .38)"><circle r="205" fill="none" stroke="#50cbd6" stroke-opacity=".65"/><g class="orb"><circle cx="205" r="5" fill="#9af5e9"/><circle cx="-205" r="3" fill="#39c4d6"/></g></g>'
    frames=[]
    for frame in range(25):
        angle=2*math.pi*frame/24+side*.6
        points=[]
        for x,y,z in [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]:
            xx=x*math.cos(angle)+z*math.sin(angle);zz=-x*math.sin(angle)+z*math.cos(angle)
            yy=y*math.cos(.4)-zz*math.sin(.4);depth=y*math.sin(.4)+zz*math.cos(.4)
            scale=96/(1+depth*.16);points.append((xx*scale,yy*scale))
        frames.append(points)
    for animated in [True,False]:
        s+=f'<g class="{ "motion" if animated else "still"}">'
        for i,j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
            values=[f'M{pts[i][0]:.2f} {pts[i][1]:.2f}L{pts[j][0]:.2f} {pts[j][1]:.2f}' for pts in frames]
            s+=f'<path d="{values[0]}" stroke="#72dbde" stroke-opacity=".85" stroke-width="1.5" fill="none">'
            if animated:s+=f'<animate attributeName="d" values="{ ";".join(values)}" dur="8s" repeatCount="indefinite"/>'
            s+='</path>'
        for i in range(8):
            s+=f'<circle cx="{frames[0][i][0]:.2f}" cy="{frames[0][i][1]:.2f}" r="2.2" fill="#b0f8ed">'
            if animated:
                for coord,axis in enumerate(['cx','cy']):
                    values=';'.join(f'{pts[i][coord]:.2f}' for pts in frames)
                    s+=f'<animate attributeName="{axis}" values="{values}" dur="8s" repeatCount="indefinite"/>'
            s+='</circle>'
        s+='</g>'
    s+='</g>'
for side in [1]:
    x0=930
    s+=f'<g class="field" style="animation-delay:-{side*3}s">'
    for row in range(9):
        points=[]
        for col in range(13):
            x=x0+(col-6)*28
            y=180+(row-4)*20+math.sin(col*.55+row*.28)*22
            points.append((x,y))
        d='M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in points)
        s+=f'<path d="{d}" fill="none" stroke="#35bfcb" stroke-opacity=".06"/><path class="signal" style="animation-delay:-{row*.4}s" d="{d}" fill="none" stroke="#9de8de" stroke-opacity=".15"/>'
        for col in range(0,13,3):
            x,y=points[col];s+=f'<circle class="dot" style="animation-delay:-{(row+col)*.3}s" cx="{x:.1f}" cy="{y:.1f}" r="1.5" fill="#8fe4dd" opacity=".45"/>'
    s+='</g>'
s+='''</g><rect x="60" y="28" width="294" height="30" rx="15" fill="#08191f" stroke="#20505b"/><circle class="dot" cx="81" cy="43" r="3" fill="#71edce"/><text x="207" y="47" text-anchor="middle" font-size="11" letter-spacing="3" fill="#bdd4dc">COGNITUM ONE</text><text class="resolve" x="60" y="124" text-anchor="start" font-size="50" font-weight="600" letter-spacing="-2" fill="#f0f8fa">Ambient Intelligence</text><text x="538" y="92" font-size="12" fill="#d7e6ec">™</text><text class="code mono" x="65" y="116" font-size="16" letter-spacing="10" fill="#8fe4dd">· : + · : · + : ·</text><text class="resolve" style="animation-delay:.16s" x="62" y="165" text-anchor="start" font-size="23" fill="#a6bdc8">at the edge of the</text><text class="resolve" style="animation-delay:.32s" x="60" y="224" text-anchor="start" font-size="56" font-weight="600" letter-spacing="-2" fill="url(#world)">Physical World</text><text class="mono" x="63" y="259" text-anchor="start" font-size="11" letter-spacing="3" fill="#9ebbc7">PERCEPTION / MEMORY / ACTION</text><rect class="breathe" x="51" y="277" width="378" height="64" rx="17" fill="#44e4db" opacity=".12"/><rect x="60" y="284" width="360" height="52" rx="11" fill="url(#cta)"/><rect class="ctaline" x="60" y="284" width="360" height="52" rx="11" fill="none" stroke="#efffff" stroke-width="1.5"/><text x="222" y="317" text-anchor="middle" font-size="21" font-weight="700" fill="#05232c">Build with Cognitum</text><g transform="translate(388 310)"><circle r="16" fill="#062b35" fill-opacity=".12"/><path class="arrow" d="M-7 0H7M1-6L7 0 1 6" fill="none" stroke="#05232c" stroke-width="2"/></g><path d="M60 353H420" stroke="#19414a"/><path class="signal" d="M60 353H420" stroke="#6bdbdb"/></svg>'''
(OUT/'cognitum-banner-v2.svg').write_text(s)
