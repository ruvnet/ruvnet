(async () => {
  const report = {viewport: {width: innerWidth, height: innerHeight}, checks: [], failures: [], stages: []};
  const assert = (name, pass, detail) => {report.checks.push({name, pass: Boolean(pass), ...(detail ? {detail} : {})}); if (!pass) report.failures.push(name);};
  const settle = () => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  try {
    await document.fonts.ready;
    assert('self hosted font loaded', [...document.fonts].some(f => f.family === 'Manrope' && f.status === 'loaded'));
    assert('no horizontal overflow', document.documentElement.scrollWidth <= innerWidth, {documentWidth: document.documentElement.scrollWidth});
    const brand = document.querySelector('.brand').getBoundingClientRect();
    const nav = document.querySelector('.nav').getBoundingClientRect();
    assert('header controls do not overlap', brand.right <= nav.left);
    const motion = document.querySelector('#motion');
    if (motion.getAttribute('aria-pressed') !== 'true') motion.click();
    assert('motion pause is reflected in accessible state', document.body.classList.contains('motion-off') && motion.getAttribute('aria-label') === 'Enable animations');
    for (const i of [0, 1, 2, 3, 4, 0]) {
      document.querySelector('[data-jump="'+i+'"]').click();
      await settle();
      const scene = document.querySelector('.visual').dataset.scene;
      assert('chapter '+(i+1)+' follows navigation', scene === String(i), {actual: scene});
      assert('only one illustration visible at chapter '+(i+1), document.querySelectorAll('.scene.on').length === 1);
      report.stages.push({chapter:i+1, visualBottom:document.querySelector('.visual').getBoundingClientRect().bottom, paragraphTop:document.querySelector('[data-step="'+i+'"] p').getBoundingClientRect().top});
    }
    for (const [filter, expected] of [['work',1],['memory',3],['evaluate',2],['all',6]]) {
      document.querySelector('[data-filter="'+filter+'"]').click();
      assert(filter+' filter count', document.querySelectorAll('.ecosystem-card').length === expected);
      assert(filter+' filter accessible state', document.querySelector('[data-filter="'+filter+'"]').getAttribute('aria-pressed') === 'true');
    }
    const card = document.querySelector('.ecosystem-card'); card.focus(); card.click();
    const dialog = document.querySelector('dialog');
    assert('package details opens', dialog.open && document.querySelector('#dialog-title').textContent === 'Ruflo');
    assert('dialog has a real project destination', document.querySelector('#dialog-link').href === 'https://github.com/ruvnet/ruflo');
    document.querySelector('.close').click(); await settle();
    assert('dialog closes and restores focus', !dialog.open && document.activeElement === card);
    const sources = document.querySelector('.sources details'); sources.open = true;
    assert('sources are present and readable', sources.textContent.includes('November 10, 2026') && sources.querySelectorAll('a').length >= 6);
    assert('external tabs protected', [...document.querySelectorAll('a[target="_blank"]')].every(a => a.rel.includes('noopener')));
    assert('no horizontal overflow after interactions', document.documentElement.scrollWidth <= innerWidth);
    document.querySelector('[data-jump="1"]').click(); await settle();
    motion.click(); assert('animations can resume', !document.body.classList.contains('motion-off'));
  } catch (error) {report.failures.push(String(error));}
  report.ok = report.failures.length === 0;
  const output = document.createElement('script'); output.type = 'application/json'; output.id = 'qa-result'; output.textContent = JSON.stringify(report); document.body.appendChild(output);
})();
