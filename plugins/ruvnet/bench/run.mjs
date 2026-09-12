import {performance} from 'node:perf_hooks';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {CATALOG,discover} from '../lib/core.mjs';
const inputs=['swarm federation','vector memory','wifi csi','harness scaffold','sandbox runtime','latent alignment'],n=10000,samples=[];
for(let i=0;i<1000;i++)discover(inputs[i%inputs.length]);
for(let i=0;i<n;i++){const t=performance.now();discover(inputs[i%inputs.length]);samples.push(performance.now()-t);}
samples.sort((a,b)=>a-b);const cold=[];
for(let i=0;i<20;i++){const t=performance.now(),r=spawnSync(process.execPath,[fileURLToPath(new URL('../bin/ruvnet.mjs',import.meta.url)),'catalog','memory'],{timeout:5000});if(r.status!==0)throw Error('CLI benchmark failed');cold.push(performance.now()-t);}
cold.sort((a,b)=>a-b);
const result={kind:'local-dispatch-benchmark',node:process.version,platform:process.platform,arch:process.arch,projects:CATALOG.projects.length,catalogSha256:createHash('sha256').update(readFileSync(new URL('../data/catalog.json',import.meta.url))).digest('hex'),samples:n,discoveryMs:{p50:samples[Math.floor(n*.5)],p95:samples[Math.floor(n*.95)]},coldCliSamples:cold.length,coldCliMs:{p50:cold[10],p95:cold[19]},rssBytes:process.memoryUsage().rss,excludes:['model inference','semantic recall','network latency','host UI installation','end-to-end agent quality'],gates:{discoveryP95Below5ms:samples[Math.floor(n*.95)]<5,coldCliP95Below1000ms:cold[19]<1000}};
console.log(JSON.stringify(result,null,2));if(Object.values(result.gates).some(v=>!v))process.exitCode=1;
