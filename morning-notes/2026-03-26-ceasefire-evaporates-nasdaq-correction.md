---
layout: morning-note
title: 'Google Just Broke the Memory Trade. TurboQuant: 6x Compression, Zero Accuracy Loss. MU −7%. SK Hynix −6%. The AI Supply Chain Is Being Rewritten Overnight.'
headline: 'Google Just Broke the Memory Trade. TurboQuant: 6x Compression, Zero Accuracy Loss. MU −7%. SK Hynix −6%. The AI Supply Chain Is Being Rewritten Overnight.'
date: 2026-03-26
image: /images/notes/2026-03-26.jpg
author: Steven Yuan

snapshot:
  - { label: 'S&P 500', value: '5,580', dir: down }
  - { label: 'Nasdaq Composite', value: '19,600', dir: down }
  - { label: 'Dow Jones', value: '46,100', dir: down }
  - { label: 'Brent Crude', value: '$100.20', dir: up }
  - { label: 'VIX', value: '27.5', dir: up }

levels:
  - { name: 'S&P 500', value: '5,580', dir: down }
  - { name: 'Nasdaq Composite', value: '19,600', dir: down }
  - { name: 'Dow Jones', value: '46,100', dir: down }
  - { name: 'Russell 2000', value: '1,905', dir: flat }
  - { name: 'WTI Crude', value: '$96.50', dir: up }
  - { name: 'Brent Crude', value: '$100.20', dir: up }
  - { name: 'VIX', value: '27.5', dir: up }
  - { name: '10Y Treasury', value: '4.28%', dir: down }
  - { name: 'Gold Spot', value: '$3,230', dir: up }

sentiment:
  - { label: 'Diplomacy / Ceasefire Odds', tone: bullish, pct: 58 }
  - { label: 'Risk Assets', tone: bearish, pct: 44 }
  - { label: 'Oil Complex', tone: neutral, pct: 52 }
  - { label: 'Geopolitical Risk', tone: bearish, pct: 66 }
  - { label: 'Defense', tone: neutral, pct: 54 }
  - { label: 'AI Infrastructure', tone: bullish, pct: 76 }
  - { label: 'Consumer Macro', tone: bearish, pct: 74 }
---
THURSDAY, MARCH 26, 2026

## Google Just Broke the Memory Trade. TurboQuant: 6x Compression, Zero Accuracy Loss. MU −7%. SK Hynix −6%. The AI Supply Chain Is Being Rewritten Overnight.

Day 27 of the US-Iran War  |  Brent $99  |  S&P +0.5% yesterday  |  Pakistan Confirms Indirect Talks  |  Lululemon AMC  |  Core PCE Tomorrow

## TOP CALL — GOOGLE TURBOQUANT CHANGES THE AI MEMORY EQUATION

## WHAT TURBOQUANT ACTUALLY DOES — AND WHY THE MARKET IS WRONG TO PANIC

Let’s cut through the noise. The market reaction—MU −7%, SK Hynix −6%, Samsung −5%—is treating TurboQuant as a demand destroyer for memory chips. That is a misread. Here’s why:

What TurboQuant compresses:

KV-cache is the working memory that allows LLMs to retain context during inference. When you have a 128K-token context window, the KV-cache grows linearly with each token, consuming enormous amounts of HBM (High Bandwidth Memory). TurboQuant reduces this specific component by 6x by compressing each cached value from 16 bits to 3 bits. This means a model that previously needed 80GB of HBM for KV-cache now needs ~13GB.

What TurboQuant does NOT compress:

Model weights: The core parameters of the model (GPT-5, Claude, Gemini) are untouched. These are the dominant consumers of HBM. A 1-trillion-parameter model still needs 1T+ parameters stored in memory.

Training memory: TurboQuant only applies to inference, not training. Training requires full precision weights, gradients, and optimizer states. The $100B+ training cluster buildout is unaffected.

Batch processing: At datacenter scale, operators run hundreds of simultaneous inference requests. TurboQuant’s 6x compression on KV-cache means each GPU can serve more concurrent users—which actually increases throughput demand, requiring more compute and more memory bandwidth.

The market history is clear:

2020: INT8 quantization panic → SK Hynix fell 4%. Recovered in 2 weeks. Memory demand increased 35% the following year.

2023: Flash Attention 2 → Memory stocks dipped 3–5% on “GPU efficiency kills demand.” NVIDIA went from $400 to $900 in 6 months.

2024: Mixture of Experts → Panic that sparse models need less memory. HBM shipments doubled the following quarter.

2026: TurboQuant → MU −7%, Hynix −6%. We expect the same pattern: dip, recovery, demand acceleration.

Our view: TurboQuant is evolutionary, not revolutionary. It makes inference cheaper at the margin, which expands the addressable market for AI applications. The memory stocks are offering a gift. MU at $355 (from $471 ATH on March 18) with a $33.5B Q3 guide and 81% gross margins is a screaming buy.

## TURBOQUANT IMPLICATIONS ACROSS THE AI SUPPLY CHAIN

The second-order effects are where the real alpha lives. TurboQuant doesn’t just affect memory—it reshuffles the entire AI infrastructure stack:

NVIDIA (NVDA): BULLISH. If each GPU serves more concurrent users, the ROI per GPU improves. This makes the $40K+ H100 price tag easier to justify for cloud providers. Expect hyperscaler capex to hold or increase, not decrease. The Vera Rubin generation with more HBM becomes even more valuable as the efficiency multiplier.

Cloud providers (AMZN/MSFT/GOOGL): BULLISH. Inference is the cloud providers’ largest AI cost center. A 6–8x improvement in throughput means dramatically better unit economics on AI services. This accelerates the rollout of AI features to consumers and enterprise, growing the pie.

Memory (MU/Samsung/SK Hynix): SHORT-TERM BEARISH, LONG-TERM BULLISH. The initial read (“less memory needed per query”) is correct at the micro level but wrong at the macro level. More efficient inference = more inference = more users = more GPUs = more HBM. Jevons’ Paradox. Buy the dip.

Photonics (COHR/LITE): BULLISH. More concurrent users per GPU means more data moving between GPUs and between servers. The optical interconnect bottleneck intensifies, not relaxes. This is why photonics was already the best-positioned AI sub-sector before TurboQuant.

AI software (PLTR/CRM/NOW): BULLISH. Cheaper inference means AI features can be offered at lower price points. The enterprise SaaS TAM for AI copilots expands. Margins improve for companies deploying AI at scale.

Edge AI (AAPL/QCOM): VERY BULLISH. 6x memory compression could make powerful LLMs viable on-device. A model that needed 80GB of KV-cache can now run in ~13GB. This opens up phone, tablet, and laptop inference at quality levels previously requiring cloud. The edge AI unlock is the sleeper implication.

## WAR UPDATE — DAY 3 OF THE NEGOTIATION WINDOW

The implications for oil and markets:

Oil holding $99–$100: The ceasefire premium continues to deflate (Brent down from $112 to $99 in 5 sessions), but Israeli strikes keep a floor under prices. The $95–$105 range is the new equilibrium while indirect talks continue.

Gold steady at $3,200–3,240: Down from the $3,290 record but finding support. Gold is now pricing two things simultaneously: ceasefire optimism (bearish for gold) and consumer confidence collapse / stagflation fears (bullish for gold). These roughly offset.

Defence names fading: LMT, RTX, NOC have given back 3–5% from war highs as ceasefire probability has risen from 30% to 45%. We’re trimming from overweight to market-weight but maintaining exposure as a hedge against talks failing.

## MARKET SNAPSHOT — 6:45 AM ET

## WAR SIGNAL TRACKER — THURSDAY ASSESSMENT

Assessment: 4 BULL / 2 BEAR / 4 NEUTRAL. Holding near yesterday’s 5/2/3 split. The Pakistan confirmation is the key upgrade. Israeli strikes prevent a BULL sweep. The ceasefire probability is now 45–50%—the highest of the war. The risk is that talks stall on the Israel dimension and the market re-prices lower.

## COMPANY HEADLINES

## EARNINGS PREVIEW — LULULEMON (LULU) Q4 FY25 AFTER CLOSE

Watch the guide: The Q4 results matter less than FY27 guidance. If LULU guides below $9.3B FY revenue and $25 EPS, shares sell off 5–10%. The consumer data supports caution.

DTC vs wholesale: Direct-to-consumer margins have been the margin expansion engine. Any deceleration in DTC growth signals the premium consumer is pulling back.

China exposure: The one bright spot. LULU’s China business is growing 25%+ and is not affected by the US-Iran war dynamic. If China strength offsets US weakness, the stock holds.

## TRADE IDEAS

## EVENT CALENDAR

Tomorrow is the most important trading day since FOMC: Core PCE at 8:30 AM tells us whether the inflation story is getting better or worse. If hot (>0.35% MoM), the Fed is vindicated and rate cuts are dead for 2026. If cool (<0.25%), there’s a path back to 2 cuts and risk assets rip. Simultaneously, Pakistan could announce face-to-face Islamabad talks—the first direct diplomatic contact of the war.

## BOTTOM LINE

Two Disruptions. Two Different Timelines.

The market is processing two disruptions simultaneously: a war that is slowly ending and a technology breakthrough that is reshaping the AI supply chain. They operate on completely different timelines, and the market is confusing the two.

The war trade is unwinding. Brent is $99. Ceasefire probability is 45–50%. Pakistan is mediating. The April 6 deadline gives talks room. This is constructive for equities, destructive for oil and defence, and already partially priced in.

The TurboQuant trade is just beginning. The market’s knee-jerk (“less memory needed = sell memory stocks”) is the same mistake it makes with every efficiency improvement in tech. Jevons’ Paradox will hold: cheaper inference means more inference means more GPUs means more HBM. MU at $355 with a $33.5B Q3 guide is a gift. GOOGL as the originator of the breakthrough is a gift. COHR/LITE as the interconnect beneficiaries are gifts.

Buy the disruption. Sell the panic. Tomorrow’s PCE will tell us which of these two stories dominates Q2.

## KEY LEVELS — 6:45 AM ET

| Asset | Level | Change | Context |
| --- | --- | --- | --- |
| S&P 500 | 5,580 | −1.2% | Futures softer on geopolitics + semis |
| Nasdaq Composite | 19,600 | −1.8% | Tech risk-off (futures proxy) |
| Dow Jones | 46,100 | −0.7% | Less tech-sensitive pullback (futures level) |
| Russell 2000 | 1,905 | flat | Small-cap reference level from prior session continuity |
| WTI Crude | $96.50 | +1.5% | War premium returning |
| Brent Crude | $100.20 | +1.1% | Back above $100 |
| VIX | 27.5 | +15% | Vol spike |
| 10Y Treasury | 4.28% | −2bp | Flight-to-safety bid |
| Gold Spot | $3,230 | +0.9% | Safe-haven support |

## SENTIMENT READINGS

- **Diplomacy / Ceasefire:** Negotiation channel is active, but credibility risk remains high.
- **Cross-Asset Positioning:** Risk-on/risk-off flips remain headline-driven; keep sizing disciplined.
- **Macro Backdrop:** Consumer and inflation expectations continue to pressure cyclical exposure.
