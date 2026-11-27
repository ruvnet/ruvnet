// Run after: npm install --no-save playwright@1.56.1
// Use the existing browser path, or install Playwright's browser separately.
import {createRequire} from 'node:module';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const base=process.env.STORY_URL || 'https://ruvnet-field-guide.cognitum-consulting-mail.workers.dev/';
const dir=new URL('./',import.meta.url);
const qa=await readFile(new URL('qa-browser.js',dir),'utf8');
const browser=await chromium.launch({headless:true, ...(process.env.CHROMIUM_PATH ? {executablePath:process.env.CHROMIUM_PATH} : {})});
const reports=[];
try {
  for(const [width,height] of [[320,812],[390,844],[768,1024],[1440,1000]]) {
    const context=await browser.newContext({viewport:{width,height},isMobile:width<760,hasTouch:width<760});
    const page=await context.newPage();const errors=[];page.on('pageerror',error=>errors.push(String(error)));
    await page.goto(base,{waitUntil:'networkidle'});
    // evaluate is a test harness, not a shipped feature.
    await page.evaluate(qa);
    await page.waitForSelector('#qa-result',{state:'attached'});
    const report=JSON.parse(await page.locator('#qa-result').textContent());report.pageErrors=errors;reports.push(report);
    await context.close();
  }
  const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
  await page.goto(base,{waitUntil:'networkidle'});
  reports.push({name:'reduced motion preference',ok:await page.locator('body').evaluate(el=>el.classList.contains('motion-off'))});
} finally {await browser.close()}
console.log(JSON.stringify(reports,null,2));
if(reports.some(r=>!r.ok || r.pageErrors?.length))process.exitCode=1;
