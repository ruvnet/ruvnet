import assert from 'node:assert/strict';
import {readFileSync,readdirSync,existsSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../',import.meta.url)),json=p=>JSON.parse(readFileSync(resolve(root,p),'utf8')),pkg=json('package.json');
for(const p of ['.claude-plugin/plugin.json','.codex-plugin/plugin.json']){const m=json(p);assert.equal(m.name,'ruvnet');assert.equal(m.version,pkg.version);assert.ok(existsSync(resolve(root,m.skills)));assert.ok(existsSync(resolve(root,m.mcpServers)));}
assert.deepEqual(json('.mcp.json'),{mcpServers:{'ruvnet-federation':{type:'http',url:'https://x.ruv.io/mcp'}}});
const catalog=json('data/catalog.json');assert.equal(new Set(catalog.projects.map(p=>p.id)).size,catalog.projects.length);
for(const p of catalog.projects){assert.ok(p.boundary);for(const url of [p.repository,p.docs])assert.equal(new URL(url).hostname,'github.com');}
for(const skill of readdirSync(resolve(root,'skills'))){const file=resolve(root,'skills',skill,'SKILL.md'),text=readFileSync(file,'utf8');assert.ok(text.startsWith('---\nname: '+skill+'\n'));assert.match(text,/\ndescription: .+/);assert.ok(!text.includes('[TODO:'));for(const m of text.matchAll(/\]\(([^)]+)\)/g))if(!m[1].startsWith('https:'))assert.ok(existsSync(resolve(dirname(file),m[1])),m[1]);}
const repo=resolve(root,'../..');if(existsSync(resolve(repo,'.claude-plugin/marketplace.json'))){const a=JSON.parse(readFileSync(resolve(repo,'.claude-plugin/marketplace.json')));assert.equal(a.name,'ruvnet');assert.equal(resolve(repo,a.plugins[0].source),resolve(root));const b=JSON.parse(readFileSync(resolve(repo,'.agents/plugins/marketplace.json')));assert.equal(resolve(repo,b.plugins[0].source.path),resolve(root));assert.equal(b.plugins[0].policy.installation,'AVAILABLE');}
console.log('PASS: manifests, marketplace paths, skill references, catalog and fixed MCP endpoint');
