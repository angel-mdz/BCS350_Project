/* Enhance location feedback only; native links own scrolling, focus and history. */
(() => {
  const header = document.querySelector('.site-header');
  const links = [...document.querySelectorAll('nav[aria-label="Primary"] a')];
  const sections = links.map(link => document.getElementById(link.hash.slice(1)));
  if (!header || sections.some(section => !section)) return;

  let observer;
  let frame = 0;
  let readingLine = 0;

  function updateCurrent() {
    frame = 0;
    let current = 0;
    sections.forEach((section, index) => {
      if (section.getBoundingClientRect().top <= readingLine + 2) current = index;
    });

    // Contact can be too short to reach the reading line before scrolling ends.
    const page = document.documentElement;
    if (window.scrollY > 0 && Math.ceil(window.scrollY + window.innerHeight) >= page.scrollHeight - 2) {
      current = sections.length - 1;
    }
    links.forEach((link, index) => {
      if (index === current) {
        if (link.getAttribute('aria-current') !== 'location') link.setAttribute('aria-current', 'location');
      } else if (link.hasAttribute('aria-current')) link.removeAttribute('aria-current');
    });
  }

  function scheduleUpdate() {
    if (!frame) frame = requestAnimationFrame(updateCurrent);
  }

  function measure() {
    // Match native anchor clearance, but also cover unexpectedly tall wrapped headers.
    const rootStyle = getComputedStyle(document.documentElement);
    const clearance = (parseFloat(rootStyle.scrollPaddingTop) || 0) * (parseFloat(rootStyle.zoom) || 1);
    readingLine = Math.min(window.innerHeight - 1, Math.max(header.getBoundingClientRect().bottom, clearance));
    observer?.disconnect();
    if ('IntersectionObserver' in window) {
      observer = new IntersectionObserver(scheduleUpdate, {
        rootMargin: `-${readingLine}px 0px 0px 0px`,
        threshold: 0
      });
      sections.forEach(section => observer.observe(section));
    }
    scheduleUpdate();
  }

  // Geometry, rather than intersection ratios, keeps long and short sections consistent.
  // A passive, frame-coalesced scroll check also covers the exact page bottom and jumps
  // across several sections between observer deliveries.
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', measure);
  window.addEventListener('hashchange', scheduleUpdate);
  window.addEventListener('pageshow', measure);
  window.addEventListener('load', measure);
  document.querySelectorAll('details').forEach(details => details.addEventListener('toggle', scheduleUpdate));
  if ('ResizeObserver' in window) {
    const sizes = new ResizeObserver(measure);
    sizes.observe(header);
    sections.forEach(section => sizes.observe(section));
  }
  if (document.fonts) document.fonts.ready.then(measure);
  measure();
})();
