---
title: "Projects — Shaoxiong (Steven) Yuan"
description: "Quantitative research, machine learning, and software engineering projects."
permalink: /projects/
---

<!-- ═══════════════ HERO ═══════════════ -->
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="hero-eyebrow">Selected Work</div>
    <h1 class="hero-title">Projects at the edge of <em>finance and software</em>.</h1>
    <p class="hero-lede">Quantitative research, machine learning, and engineering work — from ML exit-timing models for private equity to statistical arbitrage pipelines and full-stack tools.</p>
  </div>
</section>

<main class="main-content">

<!-- ═══════════════ QUANT & ML ═══════════════ -->
<div class="content-section" markdown="1">

## *Quantitative &amp; Machine Learning* {#quant}

<div class="project-grid">

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">PE Investments Exits Prediction — MUFG Americas</span>
      <span class="project-card-tag">AFP / ML</span>
    </div>
    <div class="project-card-body">
      UCLA MFE Applied Finance Project (Jun–Dec 2025). Developed an ML model to predict exit timing and type (IPO, M&amp;A, secondary sale) for PE-backed firms using historical, macroeconomic, and deal-level data to optimize holding periods and inform liquidity planning. Identified key exit drivers such as fund vintage, company performance, industry trends, and market cycles via Python-based statistical and ML methods.
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Statistical Arbitrage Pair Trading</span>
      <span class="project-card-tag">Quant</span>
    </div>
    <div class="project-card-body">
      End-to-end stat-arb pipeline on S&amp;P 500 equities: Engle-Granger cointegration screening, Ornstein-Uhlenbeck spread modelling, and Bayesian-optimized z-score trading with dollar-neutral sizing. Out-of-sample Sharpe of 1.69 on the primary pair.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/StatArb/Statistical_Arbitrage_Group_3.pdf" target="_blank" class="project-link">Paper</a>
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/StatArb/main.ipynb" target="_blank" class="project-link">Notebook</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Regime-Based Factor Investing</span>
      <span class="project-card-tag">Quant</span>
    </div>
    <div class="project-card-body">
      Regime-aware long-short factor strategy on CRSP data (1990–2023): a 3×3 matrix of macro and market-concentration regimes, each mapped to an optimal combination of six factor signals. Generates statistically significant CAPM and FF3 alpha and outperforms across major bear markets.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/QAM/QAM_FinalProject.pdf" target="_blank" class="project-link">Paper</a>
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/QAM/FinalProject_KM3.ipynb" target="_blank" class="project-link">Notebook</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Stock Return Prediction — XGBoost &amp; Random Forest</span>
      <span class="project-card-tag">ML</span>
    </div>
    <div class="project-card-body">
      Trained XGBoost and Random Forest models on CRSP/Compustat data (2012–2024) to forecast next-month stock returns, evaluated via decile portfolios and a winner-minus-loser long-short portfolio against a Fama-French 3-factor benchmark.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/ML/ML_Final_Project_Part1.pdf" target="_blank" class="project-link">Paper</a>
      <a href="https://ShaoxiongYuan.github.io/Files/UCLA/ML/final_project_code.ipynb" target="_blank" class="project-link">Notebook</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Market Behavior Prediction — Monte Carlo Simulation</span>
      <span class="project-card-tag">Quant / MATLAB</span>
    </div>
    <div class="project-card-body">
      Used MATLAB to model complex stochastic processes via Monte Carlo simulation, predicting market behaviors and improving probabilistic risk assessment. Applied advanced MATLAB toolboxes to translate theoretical finance models into practical scenario analysis.
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Lung Cancer Image Classification — GANs</span>
      <span class="project-card-tag">ML / CV</span>
    </div>
    <div class="project-card-body">
      Explored Generative Adversarial Networks (GANs) in Python to classify lung cancer images. Developed algorithms for processing and interpreting large-scale medical imaging datasets, enhancing data analysis capabilities in a clinical context.
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Pioneer Academics — Continued Fractions Research</span>
      <span class="project-card-tag">Math</span>
    </div>
    <div class="project-card-body">
      Independent research with Prof. Gregory Dresden (Washington &amp; Lee University) on continued fractions and integer sequences. Explored Fibonacci identities, Lucas numbers, and iterative number patterns, resulting in a published paper on ArXiv and an OEIS entry.
    </div>
    <div class="project-card-links">
      <a href="https://arxiv.org/abs/1907.12459" target="_blank" class="project-link">Final Paper ↗</a>
      <a href="https://oeis.org/A049669" target="_blank" class="project-link">OEIS Entry ↗</a>
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/Pioneer/textbook.pdf" target="_blank" class="project-link">Textbook</a>
      <a href="https://pioneeracademics.com/" target="_blank" class="project-link">Program ↗</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">GPT-2 — Generative Python Transformer</span>
      <span class="project-card-tag">ML / NLP</span>
    </div>
    <div class="project-card-body">
      Trained a GPT-2 model from scratch to predict next lines of Python code. Built on sentdex's tutorial using 80GB of Python source files. The trained model is hosted on Hugging Face as GPyT.
    </div>
    <div class="project-card-links">
      <a href="https://huggingface.co/Sentdex/GPyT" target="_blank" class="project-link">Hugging Face ↗</a>
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/gpt-2.zip" target="_blank" class="project-link">Source Code</a>
    </div>
  </div>

</div>

</div>

<!-- ═══════════════ SOFTWARE ═══════════════ -->
<div class="content-section" markdown="1">

## *Software &amp; Web* {#software}

<div class="project-grid">

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Online Shopping Website — Django + Nginx</span>
      <span class="project-card-tag">Web / Backend</span>
    </div>
    <div class="project-card-body">
      Full-stack e-commerce site built with Django and served via Nginx for static file handling (HTML, CSS, JS). Implements product listings, cart, and order management.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/dadashop/dadashop12.zip" target="_blank" class="project-link">Source Code</a>
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/dadashop/nginx.conf" target="_blank" class="project-link">Nginx Config</a>
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/dadashop/dadashop.zip" target="_blank" class="project-link">Static Files</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Micro Blog Site — Python / Flask</span>
      <span class="project-card-tag">Web / Flask</span>
    </div>
    <div class="project-card-body">
      A fully-featured microblogging platform built with Flask, implementing user authentication, post creation, and feed rendering. Follows Corey Schafer's Flask tutorial series.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/Flask_Blog.zip" target="_blank" class="project-link">Source Code</a>
      <a href="https://www.youtube.com/c/Coreyms" target="_blank" class="project-link">Tutorial ↗</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Comment System with Waterfall Loading — Flask</span>
      <span class="project-card-tag">Web / Flask</span>
    </div>
    <div class="project-card-body">
      A dynamic comment system featuring infinite scroll / waterfall loading built with Flask. Demonstrates lazy-loading patterns and real-time content rendering without page reloads.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/comment.zip" target="_blank" class="project-link">Source Code</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-header">
      <span class="project-card-title">Download All Microsoft Templates — Scrapy</span>
      <span class="project-card-tag">Web Scraping</span>
    </div>
    <div class="project-card-body">
      A Scrapy spider that bulk-downloads Microsoft Office templates from the official template gallery, automating the crawl, extraction, and file-saving pipeline.
    </div>
    <div class="project-card-links">
      <a href="https://ShaoxiongYuan.github.io/Files/Projects/Microsoft.zip" target="_blank" class="project-link">Source Code</a>
    </div>
  </div>

</div>

</div>

</main>
