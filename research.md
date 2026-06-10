---
title: "Research — Shaoxiong (Steven) Yuan"
description: "Daily morning notes, sector analysis, and company reports covering technology, energy, financials, and healthcare."
permalink: /research/
---

{% assign all_notes = site.pages | where: "layout", "morning-note" | sort: "date" | reverse %}
{% assign featured = all_notes.first %}

<style>
  /* ── Featured note ── */
  .featured-note {
    display: block;
    background: #f7f5ee;
    border: 1px solid var(--rule-card);
    border-left: 3px solid var(--gold);
    border-radius: 8px;
    padding: 1.8rem 2rem;
    text-decoration: none;
    border-bottom: 1px solid var(--rule-card) !important;
    transition: border-color 0.25s var(--ease), transform 0.25s var(--ease), box-shadow 0.25s var(--ease);
    margin: 1.2rem 0 0.4rem;
  }
  .featured-note:hover {
    border-color: var(--gold) !important;
    transform: translateY(-3px);
    box-shadow: var(--shadow-hover);
  }
  .featured-kicker {
    font-family: var(--mono);
    font-size: 0.58rem;
    font-weight: 600;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: var(--gold-2);
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
  }
  .featured-kicker .live-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--gold);
    animation: pulse 2s ease-in-out infinite;
  }
  .featured-date {
    font-family: var(--mono);
    font-size: 0.66rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-3);
    margin-bottom: 0.6rem;
  }
  .featured-title {
    font-family: var(--serif);
    font-size: 1.25rem;
    font-weight: 500;
    line-height: 1.45;
    color: var(--ink);
    transition: color 0.2s;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .featured-note:hover .featured-title { color: var(--gold-2); }
  .featured-cta {
    font-family: var(--mono);
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--gold-2);
    margin-top: 1rem;
    transition: letter-spacing 0.25s var(--ease);
  }
  .featured-note:hover .featured-cta { letter-spacing: 0.22em; }

  /* ── Search + filters ── */
  .research-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    align-items: center;
    margin: 1.2rem 0 1.1rem;
  }
  .research-search {
    flex: 1;
    min-width: 220px;
    font-family: var(--mono);
    font-size: 0.78rem;
    color: var(--ink);
    background: #f7f5ee;
    border: 1px solid var(--rule-card);
    border-radius: 5px;
    padding: 0.6rem 0.9rem;
    outline: none;
    transition: border-color 0.18s, box-shadow 0.18s;
  }
  .research-search:focus { border-color: var(--gold); box-shadow: 0 0 0 3px rgba(176,138,62,0.18); }
  .research-search::placeholder { color: var(--ink-3); }

  .filter-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .filter-chip {
    font-family: var(--mono);
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-2);
    background: #f7f5ee;
    border: 1px solid var(--rule-card);
    border-radius: 4px;
    padding: 0.42rem 0.8rem;
    cursor: pointer;
    transition: background 0.2s var(--ease), color 0.2s var(--ease),
                border-color 0.2s var(--ease), transform 0.2s var(--ease);
  }
  .filter-chip:hover { border-color: var(--gold-2); color: var(--gold-2); transform: translateY(-1px); }
  .filter-chip.active { background: var(--navy); color: var(--card); border-color: var(--navy); }

  .results-count {
    font-family: var(--mono);
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-3);
    margin: 0.2rem 0 0.9rem;
  }
  .no-results {
    display: none;
    font-size: 0.85rem;
    font-weight: 300;
    color: var(--ink-3);
    padding: 1.5rem 0;
    text-align: center;
  }
</style>

<!-- ═══════════════ HERO ═══════════════ -->
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="hero-eyebrow">Research Desk</div>
    <h1 class="hero-title">Equity research, written <em>daily</em>.</h1>
    <p class="hero-lede">Morning notes on market structure, macro, and trade ideas — alongside sector deep dives and single-name company reports across technology, energy, financials, and healthcare.</p>
    <div class="hero-proofs">
      <div class="hero-proof">
        <div class="hero-proof-title">{{ all_notes.size }}</div>
        <div class="hero-proof-sub">Morning Notes</div>
      </div>
      <div class="hero-proof">
        <div class="hero-proof-title">4</div>
        <div class="hero-proof-sub">Sectors Covered</div>
      </div>
      <div class="hero-proof">
        <div class="hero-proof-title">3</div>
        <div class="hero-proof-sub">Company Reports</div>
      </div>
      <div class="hero-proof">
        <div class="hero-proof-title">{{ featured.date | date: "%b %-d" }}</div>
        <div class="hero-proof-sub">Latest Note</div>
      </div>
    </div>
  </div>
</section>

<main class="main-content">

<!-- ═══════════════ FEATURED NOTE ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Featured — Latest Morning Note* {#featured}
<a class="view-all" href="/morning-notes">Calendar View →</a>
</div>

<a class="featured-note" href="{{ featured.url }}">
  <div class="featured-kicker"><span class="live-dot"></span> Latest Note</div>
  <div class="featured-date">{{ featured.date | date: "%A, %B %-d, %Y" }}</div>
  <div class="featured-title">{{ featured.headline | default: featured.title }}</div>
  <div class="featured-cta">Read the Full Note →</div>
</a>

</div>

<!-- ═══════════════ COVERAGE LIBRARY ═══════════════ -->
<div class="content-section" markdown="1">

## *Sector &amp; Company Coverage* {#coverage}

Filter the research library by sector. Sector reports cover market structure, competitive dynamics, and valuations; company reports add single-name fundamental work with scenario-based reference targets.

<div class="filter-chips" id="sectorChips">
  <button class="filter-chip active" data-sector="all">All</button>
  <button class="filter-chip" data-sector="tech">Technology</button>
  <button class="filter-chip" data-sector="energy">Energy</button>
  <button class="filter-chip" data-sector="financials">Financials</button>
  <button class="filter-chip" data-sector="healthcare">Healthcare</button>
</div>

<div class="card-grid" id="coverageGrid" style="margin-top: 1.1rem;">
  <a class="report-card coverage-item" data-sector="tech" href="/sector-analysis/technology-software/">
    <div class="report-card-top">
      <span class="report-card-name">Technology &amp; Software</span>
      <span class="ticker-chip ticker-chip--gold">SECTOR</span>
    </div>
    <div class="report-card-body">Semiconductors, AI infrastructure, cloud, SaaS repricing, cybersecurity, and Mag 7 platform economics.</div>
    <div class="report-card-meta">Sector Analysis</div>
  </a>
  <a class="report-card coverage-item" data-sector="energy" href="/sector-analysis/energy/">
    <div class="report-card-top">
      <span class="report-card-name">Energy</span>
      <span class="ticker-chip ticker-chip--gold">SECTOR</span>
    </div>
    <div class="report-card-body">Oil &amp; gas, the Hormuz crisis, renewables, LNG, the nuclear renaissance, and AI power demand.</div>
    <div class="report-card-meta">Sector Analysis</div>
  </a>
  <a class="report-card coverage-item" data-sector="financials" href="/sector-analysis/financial-services/">
    <div class="report-card-top">
      <span class="report-card-name">Financial Services</span>
      <span class="ticker-chip ticker-chip--gold">SECTOR</span>
    </div>
    <div class="report-card-body">Banking, private credit systemic risk, asset management, insurance, and fintech.</div>
    <div class="report-card-meta">Sector Analysis</div>
  </a>
  <a class="report-card coverage-item" data-sector="healthcare" href="/sector-analysis/healthcare/">
    <div class="report-card-top">
      <span class="report-card-name">Healthcare</span>
      <span class="ticker-chip ticker-chip--gold">SECTOR</span>
    </div>
    <div class="report-card-body">Pharmaceuticals, GLP-1 markets, medical devices, payers, and healthcare services.</div>
    <div class="report-card-meta">Sector Analysis</div>
  </a>
  <a class="report-card coverage-item" data-sector="tech" href="/sector-analysis/company-reports/dell/">
    <div class="report-card-top">
      <span class="report-card-name">Dell Technologies</span>
      <span class="ticker-chip">DELL</span>
    </div>
    <div class="report-card-body">AI server momentum, record backlog, FY27 guidance, and valuation notes on the largest pure-play IT-infrastructure vendor.</div>
    <div class="report-card-meta">Company Report · May 2026</div>
  </a>
  <a class="report-card coverage-item" data-sector="tech" href="/sector-analysis/company-reports/amzn/">
    <div class="report-card-top">
      <span class="report-card-name">Amazon.com</span>
      <span class="ticker-chip">AMZN</span>
    </div>
    <div class="report-card-body">AWS reacceleration, retail re-margining, advertising scale, the capex cycle, and a sum-of-the-parts framework.</div>
    <div class="report-card-meta">Company Report · May 2026</div>
  </a>
  <a class="report-card coverage-item" data-sector="tech" href="/sector-analysis/company-reports/cohr/">
    <div class="report-card-top">
      <span class="report-card-name">Coherent Corp.</span>
      <span class="ticker-chip">COHR</span>
    </div>
    <div class="report-card-body">Initiating coverage on the leading Western photonics and optical networking pure-play in the AI capex cycle.</div>
    <div class="report-card-meta">Initiating Coverage · June 2026</div>
  </a>
</div>

<p class="no-results" id="coverageEmpty">No coverage in this sector yet.</p>

</div>

<!-- ═══════════════ MORNING NOTES ARCHIVE ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Morning Notes Archive* {#morning-notes}
<a class="view-all" href="/morning-notes">Calendar View →</a>
</div>

Daily equity research notes covering market structure, macro developments, and trade ideas. Search by ticker, theme, or keyword.

<div class="research-controls">
  <input type="search" class="research-search" id="noteSearch" placeholder="Search notes — e.g. CPI, NVDA, Brent, FOMC…" aria-label="Search morning notes">
</div>

<div class="results-count" id="noteCount">{{ all_notes.size }} notes</div>

<div class="card-grid card-grid--wide" id="notesGrid">
  {% for note in all_notes %}
  <a class="note-card note-item" href="{{ note.url }}" data-search="{{ note.date | date: '%B %Y %b %-d' }} {{ note.headline | default: note.title | downcase | escape }}">
    <div class="note-card-date">{{ note.date | date: "%b %-d, %Y" }}</div>
    <div class="note-card-title">{{ note.headline | default: note.title }}</div>
  </a>
  {% endfor %}
</div>

<p class="no-results" id="notesEmpty">No notes match that search.</p>

</div>

</main>

<script>
  // ── Sector filter ──────────────────────────────────────
  (function () {
    const chips = document.querySelectorAll('#sectorChips .filter-chip');
    const items = document.querySelectorAll('.coverage-item');
    const empty = document.getElementById('coverageEmpty');

    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const sector = chip.dataset.sector;
        let shown = 0;
        items.forEach(item => {
          const show = sector === 'all' || item.dataset.sector === sector;
          item.style.display = show ? '' : 'none';
          if (show) shown++;
        });
        empty.style.display = shown ? 'none' : 'block';
      });
    });
  })();

  // ── Notes search ───────────────────────────────────────
  (function () {
    const input = document.getElementById('noteSearch');
    const items = document.querySelectorAll('.note-item');
    const count = document.getElementById('noteCount');
    const empty = document.getElementById('notesEmpty');
    const total = items.length;

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      items.forEach(item => {
        const hay = (item.dataset.search || '').toLowerCase();
        const show = !q || hay.includes(q);
        item.style.display = show ? '' : 'none';
        if (show) shown++;
      });
      count.textContent = q ? shown + ' of ' + total + ' notes' : total + ' notes';
      empty.style.display = shown ? 'none' : 'block';
    });
  })();
</script>
