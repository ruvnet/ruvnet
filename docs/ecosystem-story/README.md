# Ruvnet field guide

An illustrated, responsive scroll story about coordination, memory, portable context and evaluation. It follows one concrete example in five chapters, then offers a filterable explorer of selected ecosystem entry points.

Live artifact: https://ruvnet-field-guide.cognitum-consulting-mail.workers.dev/

## Design and behavior

Custom SVG illustrations and a decorative canvas constellation. Native scrolling with a sticky illustration panel. Phone layouts put the illustration above the text and enlarge chapter controls. Native dialogs provide keyboard focus handling. The pause control stops animation; the page also respects the system reduced motion preference. The story stays readable without animation.

No client framework, build dependencies, application analytics, cookies, forms, runtime API calls or Worker bindings. Manrope is bundled under the SIL Open Font License. All facts are a dated public snapshot; illustrations do not represent measured topology or benchmarks. Downloads are not presented as unique adoption.

## Source files

* `index.html`: complete page, styles, illustrations and interactions.
* `font.woff2` and `FONT-LICENSE.txt`: self hosted Latin variable font and license.
* `source-snapshot.json`: inventory pagination receipt, definitions and integration references.
* `build.mjs`: deterministic Worker generator with CSP hashes and artifact watermark.
* `worker.mjs`: generated Cloudflare module serving the page, font, snapshot, favicon and health check.
* `worker.test.mjs`: routing, source integrity, CSP hash and bounded method checks.
* `qa-browser.js`: interaction checks reusable inside a browser at each viewport.
* `qa.mjs`: Playwright runner for the live artifact, including system reduced motion emulation.
* `validation.json`: observed validation and deployment receipt with explicit limitations.

## Build and verify

```sh
node docs/ecosystem-story/build.mjs
node --test docs/ecosystem-story/worker.test.mjs
```

The build needs Node 20 or newer. The browser runner uses Playwright 1.56.1 and an installed Chromium. It does not install dependencies or a browser automatically. On an environment with those prerequisites:

```sh
CHROMIUM_PATH=/usr/bin/chromium node docs/ecosystem-story/qa.mjs
```

`STORY_URL` can select a preview instead of the published URL. Read the validation receipt for checks actually executed in this delivery. The cloud rendering harness embeds the exact page and font bytes in an isolated document to exercise responsive behavior. That does not replace live checks for the Worker policy and same origin font route.

## Deployment and rollback

Upload `worker.mjs` as the main ES module of the existing `ruvnet-field-guide` Cloudflare Worker with compatibility date `2026-11-10` and no bindings. The Worker is available on its workers.dev route; no custom domains or other applications are changed. Source uploads use the connected Cloudflare API, not credentials in this repository.

After upload, read `/health` and compare the artifact SHA256 with the local build output. Verify `/`, `/font.woff2` and `/source-snapshot.json`, then exercise the story and explorer. To roll back, rebuild a previous source commit and upload that module to the same Worker. Keep the public inventory date explicit when making later edits.

## Acceptance

At 320, 390, 768 and 1440 px widths: no horizontal overflow, no overlapping header controls, all five chapter illustrations follow navigation in both directions, filters return the expected tools, details close and restore focus, motion can pause and resume. The published font, HTML and snapshot must match the source bytes; inline scripts must match the shipped CSP hashes. Check the native reduced motion preference on a capable browser before claiming that preference was exercised.
