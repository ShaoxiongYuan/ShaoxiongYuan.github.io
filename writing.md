---
title: "Writing — Shaoxiong (Steven) Yuan"
description: "Analytical film reviews and reports on emerging technology."
permalink: /writing/
---

{% assign reviews = site.pages | where: "layout", "review" | sort: "date" | reverse %}
{% assign tidbits = site.pages | where: "layout", "tech-tidbit" | sort: "date" | reverse %}

<!-- ═══════════════ HERO ═══════════════ -->
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="hero-eyebrow">Off the Desk</div>
    <h1 class="hero-title">Writing beyond <em>the tape</em>.</h1>
    <p class="hero-lede">Analytical film reviews for movies worth thinking about beyond the credits, and occasional reports on the hottest things happening in technology.</p>
    <div class="hero-ctas">
      <a class="btn btn-gold" href="/movie-reviews">Browse Film Reviews</a>
      <a class="btn btn-outline" href="/tech-tidbits">Browse Tech Tidbits</a>
    </div>
  </div>
</section>

<main class="main-content">

<!-- ═══════════════ FILM REVIEWS ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Film Reviews* {#film-reviews}
<a class="view-all" href="/movie-reviews">All {{ reviews.size }} Reviews →</a>
</div>

More analytical than plot summary — reviews of films that linger after the credits.

<div class="card-grid">
  {% for review in reviews limit:6 %}
  <a class="report-card" href="{{ review.url }}">
    <div class="report-card-top">
      <span class="report-card-name">{{ review.film_title }}</span>
      <span class="ticker-chip ticker-chip--gold">{{ review.rating }}</span>
    </div>
    <div class="report-card-body">{{ review.tagline }}</div>
    <div class="report-card-meta">{{ review.director }} · {{ review.year }}</div>
  </a>
  {% endfor %}
</div>

</div>

<!-- ═══════════════ TECH TIDBITS ═══════════════ -->
<div class="content-section" markdown="1">

<div class="section-head" markdown="1">
## *Tech Tidbits — Stay with the Trend* {#tech-tidbits}
<a class="view-all" href="/tech-tidbits">All {{ tidbits.size }} Reports →</a>
</div>

Reports and opinions on emerging tech, viral projects, and the tools reshaping how we work.

<div class="card-grid card-grid--wide">
  {% for post in tidbits %}
  <a class="report-card" href="{{ post.url }}">
    <div class="report-card-top">
      <span class="report-card-name">{{ post.headline | default: post.title }}</span>
      <span class="ticker-chip ticker-chip--gold">{{ post.category | upcase }}</span>
    </div>
    <div class="report-card-body">{{ post.summary | truncate: 160 }}</div>
    <div class="report-card-meta">{{ post.date | date: "%b %Y" }} · {{ post.read_time }}</div>
  </a>
  {% endfor %}
</div>

</div>

</main>
