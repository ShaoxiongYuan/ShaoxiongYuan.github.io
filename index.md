---
title: "Shaoxiong (Steven) Yuan — Quantitative Researcher"
description: "Quantitative researcher building fundamental + machine-learning investment systems. Co-founder, Orion Alpha Asset Management."
---

{% assign all_notes = site.pages | where: "layout", "morning-note" | sort: "date" | reverse %}

<!-- ═══════════════ HERO ═══════════════ -->
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="hero-eyebrow">Shaoxiong (Steven) Yuan</div>
    <h1 class="hero-title">Quantitative researcher building <em>fundamental + machine-learning</em> investment systems.</h1>
    <p class="hero-lede">I work at the intersection of fundamental equity research, derivatives modelling, and ML-driven portfolio construction — publishing daily market research and building systematic strategies at Orion Alpha Asset Management.</p>
    <div class="hero-ctas">
      <a class="btn btn-gold" href="/research/">Read Latest Research</a>
      <a class="btn btn-outline" href="/orion-alpha/">View Orion Alpha</a>
      <a class="btn btn-outline" href="mailto:ysxstevenpp123@gmail.com">Contact Me</a>
    </div>
    <div class="hero-proofs">
      <div class="hero-proof">
        <div class="hero-proof-title">UCLA MFE '25 · USC '24</div>
        <div class="hero-proof-sub">Financial Engineering · Applied Math · CSBA</div>
      </div>
      <div class="hero-proof">
        <div class="hero-proof-title">Co-Founder, Orion Alpha</div>
        <div class="hero-proof-sub">Fund X Managing Partner · Quantamental AM</div>
      </div>
      <div class="hero-proof">
        <div class="hero-proof-title">Equity Research · Derivatives · ML</div>
        <div class="hero-proof-sub">{{ all_notes.size }} Notes · Sector &amp; Company Coverage</div>
      </div>
    </div>
  </div>
</section>

<main class="main-content">

<!-- ═══════════════ RESEARCH PREVIEW ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Latest Research* {#research}
<a class="view-all" href="/research/">View All →</a>
</div>

Daily morning notes on market structure, macro, and trade ideas — plus sector deep dives and single-name company reports.

<div class="card-grid card-grid--wide">
  {% for note in all_notes limit:3 %}
  <a class="note-card" href="{{ note.url }}">
    <div class="note-card-date">{{ note.date | date: "%b %-d, %Y" }}</div>
    <div class="note-card-title">{{ note.headline | default: note.title }}</div>
  </a>
  {% endfor %}
</div>

<h4>Featured Company Coverage</h4>

<div class="card-grid">
  <a class="report-card" href="/sector-analysis/company-reports/dell/">
    <div class="report-card-top">
      <span class="report-card-name">Dell Technologies</span>
      <span class="ticker-chip">DELL</span>
    </div>
    <div class="report-card-body">AI server backlog, FY27 guidance, and valuation through the fastest growth since Dell's return to public markets.</div>
  </a>
  <a class="report-card" href="/sector-analysis/company-reports/amzn/">
    <div class="report-card-top">
      <span class="report-card-name">Amazon.com</span>
      <span class="ticker-chip">AMZN</span>
    </div>
    <div class="report-card-body">AWS reacceleration, retail re-margining, advertising scale, and the capex cycle behind the SOTP view.</div>
  </a>
  <a class="report-card" href="/sector-analysis/company-reports/cohr/">
    <div class="report-card-top">
      <span class="report-card-name">Coherent Corp.</span>
      <span class="ticker-chip">COHR</span>
    </div>
    <div class="report-card-body">Initiating coverage on the leading Western photonics pure-play at the center of the AI optical networking cycle.</div>
  </a>
</div>

</div>

<!-- ═══════════════ ORION ALPHA PREVIEW ═══════════════ -->
<div class="content-section content-section--dark" markdown="1">

<div class="section-head" markdown="1">
## *Orion Alpha Asset Management* {#orion-alpha}
<a class="view-all" href="/orion-alpha/">Firm Profile →</a>
</div>

<p style="font-family: var(--serif); font-style: italic; font-size: 1.3rem; color: var(--gold); margin-bottom: 0.8rem;">Where fundamental conviction meets quantitative discipline.</p>

Co-founder and Fund X Managing Partner of [Orion Alpha Asset Management](https://www.oa-am.com/){:target="_blank"} — a quantamental investment firm fusing deep fundamental business analysis with Bayesian data validation to eliminate narrative bias and capture market mispricing.

<a class="btn btn-gold" href="/orion-alpha/" style="margin-top: 0.4rem;">Strategy &amp; Research Focus</a>

</div>

<!-- ═══════════════ PROJECTS PREVIEW ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Projects* {#projects}
<a class="view-all" href="/projects/">All Projects →</a>
</div>

Selected quantitative and engineering work — from ML exit-timing models for private equity to statistical arbitrage pipelines and full-stack tools.

<div class="card-grid">
  <a class="report-card" href="/projects/#quant">
    <div class="report-card-top">
      <span class="report-card-name">PE Exit Prediction — MUFG</span>
      <span class="ticker-chip ticker-chip--gold">ML</span>
    </div>
    <div class="report-card-body">Applied Finance Project predicting exit timing and type for PE-backed firms using deal-level and macro data.</div>
  </a>
  <a class="report-card" href="/projects/#quant">
    <div class="report-card-top">
      <span class="report-card-name">Statistical Arbitrage Pipeline</span>
      <span class="ticker-chip ticker-chip--gold">QUANT</span>
    </div>
    <div class="report-card-body">Cointegration screening, Ornstein-Uhlenbeck spread modelling, and Bayesian-optimized pair trading on S&amp;P 500 equities.</div>
  </a>
  <a class="report-card" href="/projects/#quant">
    <div class="report-card-top">
      <span class="report-card-name">Regime-Based Factor Investing</span>
      <span class="ticker-chip ticker-chip--gold">QUANT</span>
    </div>
    <div class="report-card-body">Nine-regime long-short factor strategy with significant CAPM and FF3 alpha across bear-market episodes.</div>
  </a>
</div>

</div>

<!-- ═══════════════ WRITING PREVIEW ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Writing* {#writing}
<a class="view-all" href="/writing/">All Writing →</a>
</div>

Outside of markets I write analytical film reviews and occasional reports on emerging technology.

<div class="card-grid">
  <a class="report-card" href="/movie-reviews">
    <div class="report-card-top">
      <span class="report-card-name">Film Reviews</span>
      <span class="ticker-chip ticker-chip--gold">FILM</span>
    </div>
    <div class="report-card-body">Reviews of movies worth thinking about beyond the credits — more analysis than plot summary.</div>
    <div class="report-card-meta">{{ site.pages | where: "layout", "review" | size }} Reviews</div>
  </a>
  <a class="report-card" href="/tech-tidbits">
    <div class="report-card-top">
      <span class="report-card-name">Tech Tidbits</span>
      <span class="ticker-chip ticker-chip--gold">TECH</span>
    </div>
    <div class="report-card-body">Reports on the hottest things happening in technology — emerging tools, viral projects, AI agents.</div>
    <div class="report-card-meta">{{ site.pages | where: "layout", "tech-tidbit" | size }} Reports</div>
  </a>
</div>

</div>

<!-- ═══════════════ ABOUT PREVIEW ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *About* {#about}
<a class="view-all" href="/about/">Full Bio →</a>
</div>

I hold a Master of Financial Engineering from UCLA Anderson and dual degrees in Applied and Computational Mathematics and Computer Science &amp; Business Administration from USC. My background spans capital markets and M&amp;A in Beijing, Shanghai, and New York.

<div class="hero-ctas" style="margin-top: 1.4rem;">
  <a class="btn btn-dark" href="/about/">About &amp; Education</a>
  <a class="btn btn-quiet" href="/about/#coursework">Course Materials Archive</a>
  <a class="btn btn-quiet" href="mailto:ysxstevenpp123@gmail.com">ysxstevenpp123@gmail.com</a>
</div>

</div>

</main>
