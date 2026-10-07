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
def start(w,h,title,desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#163047" stroke-opacity=".3"/></pattern><radialGradient id="halo"><stop stop-color="#233759"/><stop offset="1" stop-color="#080e19"/></radialGradient></defs><style>{CSS}</style><rect width="{w}" height="{h}" rx="14" fill="#080e19"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>'''
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
    art=shapes[kind]
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
    s+=txt(32,243,'EXPLORE PROJECT  ↗',12,color)
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
