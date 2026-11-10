import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import worker from './worker.mjs';
const origin='https://ruvnet-field-guide.cognitum-consulting-mail.workers.dev';
const request=(path,method='GET')=>worker.fetch(new Request(origin+path,{method}));
test('artifact is served with working integrity and browser policy',async()=>{
 const response=await request('/');assert.equal(response.status,200);
 const body=await response.text();assert.equal(body,await readFile(new URL('index.html',import.meta.url),'utf8'));
 for(const match of body.matchAll(/<script>([\s\S]*?)<\/script>/g))assert.ok(response.headers.get('content-security-policy').includes("'sha256-"+createHash('sha256').update(match[1]).digest('base64')+"'"));
 assert.match(response.headers.get('content-security-policy'),/frame-ancestors 'none'/);
 assert.equal(response.headers.get('x-content-type-options'),'nosniff');
 const health=await (await request('/health')).json();assert.equal(health.status,'ok');assert.equal(response.headers.get('x-artifact-version'),health.version);
});
test('same origin font and snapshot survive deployment without transformation',async()=>{
 const font=await request('/font.woff2');assert.equal(font.headers.get('content-type'),'font/woff2');
 assert.deepEqual(Buffer.from(await font.arrayBuffer()),await readFile(new URL('font.woff2',import.meta.url)));
 const source=await (await request('/source-snapshot.json')).json();assert.equal(source.npm_unique_packages,new Set(source.npm_package_names).size);assert.equal(source.npm_unique_packages,source.npm_maintainer_search_total);
 assert.equal(source.pages[3].count,0);assert.equal(source.public_repositories,233);assert.equal(source.public_nonfork_repositories,206);
});
test('HEAD, missing pages and unsupported methods are bounded',async()=>{
 const head=await request('/','HEAD');assert.equal(head.status,200);assert.equal(await head.text(),'');
 assert.equal((await request('/missing')).status,404);
 const post=await request('/','POST');assert.equal(post.status,405);assert.equal(post.headers.get('allow'),'GET, HEAD');
});
