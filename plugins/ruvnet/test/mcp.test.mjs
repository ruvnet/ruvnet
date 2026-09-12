import test from 'node:test';
import assert from 'node:assert/strict';
import {Client} from '@modelcontextprotocol/sdk/client/index.js';
import {StdioClientTransport} from '@modelcontextprotocol/sdk/client/stdio.js';
import {InMemoryTransport} from '@modelcontextprotocol/sdk/inMemory.js';
import {createServer} from '../lib/mcp.mjs';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const bin=fileURLToPath(new URL('../bin/ruvnet.mjs',import.meta.url));
async function exercise(c){
 const t=await c.listTools();assert.equal(t.tools.length,5);assert.ok(t.tools.every(x=>x.annotations.readOnlyHint&&x.annotations.destructiveHint===false));
 for(const [name,args] of [['ruvnet_discover',{query:'wifi'}],['ruvnet_project',{id:'ruflo'}],['ruvnet_changes',{limit:2}],['ruvnet_plan',{goal:'build harness'}],['ruvnet_connect',{host:'chatgpt'}]]){const r=await c.callTool({name,arguments:args});assert.ok(!r.isError);assert.doesNotThrow(()=>JSON.parse(r.content[0].text));}
 for(const [name,args] of [['ruvnet_project',{id:'../../etc/passwd'}],['ruvnet_changes',{limit:21}],['ruvnet_connect',{host:'evil'}],['ruvnet_plan',{}],['ruvnet_discover',{execute:true}],['publish',{}]])assert.equal((await c.callTool({name,arguments:args})).isError,true);
 const rs=await c.listResources();assert.equal(rs.resources.length,3);for(const r of rs.resources)assert.ok((await c.readResource({uri:r.uri})).contents.length);
 await assert.rejects(c.readResource({uri:'file:///etc/passwd'}));assert.equal((await c.listPrompts()).prompts[0].name,'ruvnet-start');assert.equal((await c.getPrompt({name:'ruvnet-start',arguments:{goal:'memory'}})).messages[0].role,'user');await assert.rejects(c.getPrompt({name:'other',arguments:{goal:'memory'}}));await assert.rejects(c.getPrompt({name:'ruvnet-start'}));await c.ping();
}
test('official SDK negotiation and protocol errors',async()=>{
 const [a,b]=InMemoryTransport.createLinkedPair(),s=createServer(),c=new Client({name:'test',version:'1.0.0'});try{await s.connect(b);await c.connect(a);await exercise(c);}finally{await c.close();await s.close();}
});
test('subprocess stdio tools, resources, prompts and clean shutdown',async()=>{
 const t=new StdioClientTransport({command:process.execPath,args:[bin,'mcp'],stderr:'pipe'}),c=new Client({name:'stdio-test',version:'1.0.0'});try{await c.connect(t);await exercise(c);}finally{await c.close();}
});
test('oversized stdin fails before SDK buffering',()=>{const r=spawnSync(process.execPath,[bin,'mcp'],{input:Buffer.alloc(70000,65),timeout:5000});assert.equal(r.status,1);assert.match(r.stderr.toString(),/64 KiB/);assert.equal(r.stdout.length,0);});
test('CLI success and invalid-command exit codes',()=>{
 for(const args of [[],['--help'],['--version'],['catalog','memory'],['project','ruflo'],['changes'],['changes','2'],['plan','harness'],['connect','stdio']]){const r=spawnSync(process.execPath,[bin,...args],{encoding:'utf8',timeout:5000});assert.equal(r.status,0);assert.equal(r.stderr,'');assert.ok(r.stdout);}
 for(const args of [['nonsense'],['mcp','extra'],['project'],['changes','21'],['changes','2','extra'],['connect','evil'],['plan']]){const r=spawnSync(process.execPath,[bin,...args],{encoding:'utf8',timeout:5000});assert.equal(r.status,1);assert.equal(r.stdout,'');assert.ok(r.stderr);}
});
