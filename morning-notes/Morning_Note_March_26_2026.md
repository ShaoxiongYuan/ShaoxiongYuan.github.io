# MORNING NOTE — Equity Research
**Thursday, March 26, 2026 | 06:45 ET**

---

## Google Just Broke the Memory Trade. TurboQuant: 6x Compression, Zero Accuracy Loss. MU −7%. SK Hynix −6%. The AI Supply Chain Is Being Rewritten Overnight.

*Day 27 of the US-Iran War | Brent $99 | S&P +0.5% yesterday | Pakistan Confirms Indirect Talks | Lululemon AMC | Core PCE Tomorrow*

---

## TOP CALL — Google TurboQuant Changes the AI Memory Equation

> **BREAKING — Google TurboQuant: 6x Memory Compression, 8x Faster Inference, Zero Accuracy Loss**
>
> Google published a research paper overnight introducing TurboQuant, an algorithm that compresses key-value cache (KV-cache) in large language models from 16 bits to just 3 bits per value. The result: 6x reduction in memory consumption and up to 8x faster inference throughput on NVIDIA H100 GPUs — with no measurable loss in output quality. Open-source release expected Q2 2026, likely at ICLR (April 23–25). The internet is calling it "Pied Piper."

---

## WHAT TURBOQUANT ACTUALLY DOES — And Why the Market Is Wrong to Panic

Let's cut through the noise. The market reaction — MU −7%, SK Hynix −6%, Samsung −5% — is treating TurboQuant as a demand destroyer for memory chips. That is a misread. Here's why:

**What TurboQuant compresses:**

KV-cache is the working memory that allows LLMs to retain context during inference. When you have a 128K-token context window, the KV-cache grows linearly with each token, consuming enormous amounts of HBM (High Bandwidth Memory). TurboQuant reduces this specific component by 6x by compressing each cached value from 16 bits to 3 bits. This means a model that previously needed 80GB of HBM for KV-cache now needs ~13GB.

**What TurboQuant does NOT compress:**

- **Model weights:** The core parameters of the model (GPT-5, Claude, Gemini) are untouched. These are the dominant consumers of HBM. A 1-trillion-parameter model still needs 1T+ parameters stored in memory.
- **Training memory:** TurboQuant only applies to inference, not training. Training requires full precision weights, gradients, and optimizer states. The $100B+ training cluster buildout is unaffected.
- **Batch processing:** At datacenter scale, operators run hundreds of simultaneous inference requests. TurboQuant's 6x compression on KV-cache means each GPU can serve more concurrent users — which actually increases throughput demand, requiring more compute and more memory bandwidth.

> **KEY INSIGHT — This Is Jevons' Paradox in Real Time**
>
> When you make a resource more efficient, you don't use less of it — you use more. If TurboQuant lets a single H100 serve 6x more concurrent LLM users, the economics of inference improve dramatically. That accelerates AI adoption, which drives more model deployment, which requires more GPUs, which requires more HBM. The same logic applied when NVIDIA introduced tensor cores (GPU efficiency up, GPU demand up), when flash attention improved transformer throughput (more models deployed, not fewer), and when quantization went from FP32 to FP16 to INT8 (inference got cheaper, inference volume exploded).

**The market history is clear:**

- **2020: INT8 quantization panic →** SK Hynix fell 4%. Recovered in 2 weeks. Memory demand increased 35% the following year.
- **2023: Flash Attention 2 →** Memory stocks dipped 3–5% on "GPU efficiency kills demand." NVIDIA went from $400 to $900 in 6 months.
- **2024: Mixture of Experts →** Panic that sparse models need less memory. HBM shipments doubled the following quarter.
- **2026: TurboQuant →** MU −7%, Hynix −6%. We expect the same pattern: dip, recovery, demand acceleration.

**Our view:** TurboQuant is evolutionary, not revolutionary. It makes inference cheaper at the margin, which expands the addressable market for AI applications. The memory stocks are offering a gift. MU at $355 (from $471 ATH on March 18) with a $33.5B Q3 guide and 81% gross margins is a screaming buy.

---

## TURBOQUANT IMPLICATIONS ACROSS THE AI SUPPLY CHAIN

The second-order effects are where the real alpha lives. TurboQuant doesn't just affect memory — it reshuffles the entire AI infrastructure stack:

- **NVIDIA (NVDA): BULLISH.** If each GPU serves more concurrent users, the ROI per GPU improves. This makes the $40K+ H100 price tag easier to justify for cloud providers. Expect hyperscaler capex to hold or increase, not decrease. The Vera Rubin generation with more HBM becomes even more valuable as the efficiency multiplier.
- **Cloud providers (AMZN/MSFT/GOOGL): BULLISH.** Inference is the cloud providers' largest AI cost center. A 6–8x improvement in throughput means dramatically better unit economics on AI services. This accelerates the rollout of AI features to consumers and enterprise, growing the pie.
- **Memory (MU/Samsung/SK Hynix): SHORT-TERM BEARISH, LONG-TERM BULLISH.** The initial read ("less memory needed per query") is correct at the micro level but wrong at the macro level. More efficient inference = more inference = more users = more GPUs = more HBM. Jevons' Paradox. Buy the dip.
- **Photonics (COHR/LITE): BULLISH.** More concurrent users per GPU means more data moving between GPUs and between servers. The optical interconnect bottleneck intensifies, not relaxes. This is why photonics was already the best-positioned AI sub-sector before TurboQuant.
- **AI software (PLTR/CRM/NOW): BULLISH.** Cheaper inference means AI features can be offered at lower price points. The enterprise SaaS TAM for AI copilots expands. Margins improve for companies deploying AI at scale.
- **Edge AI (AAPL/QCOM): VERY BULLISH.** 6x memory compression could make powerful LLMs viable on-device. A model that needed 80GB of KV-cache can now run in ~13GB. This opens up phone, tablet, and laptop inference at quality levels previously requiring cloud. The edge AI unlock is the sleeper implication.

---

## WAR UPDATE — Day 3 of the Negotiation Window

> **DIPLOMACY — Pakistan Confirms: "US-Iran Indirect Talks Are Taking Place Through Messages Relayed by Pakistan"**
>
> For the first time, a mediator has officially confirmed active diplomatic engagement. Pakistan's statement that talks are occurring "through messages being relayed" confirms the back-channel is real, even as Iran publicly denies it. Egypt and Turkey are also backing the process. Envoys are pushing for face-to-face Islamabad talks as early as Friday.

> **ESCALATION — Israel Strikes Isfahan Overnight. Iran Fires Missiles at Central Israel.**
>
> While the US has paused strikes (extended to April 6), Israel continues its independent campaign. Overnight strikes hit Isfahan — a major industrial and nuclear research hub. Iran retaliated with two waves of missiles targeting central Israel. The parallel tracks — diplomacy via Pakistan and combat via Israel — create an unstable dynamic.

**The implications for oil and markets:**

- **Oil holding $99–$100:** The ceasefire premium continues to deflate (Brent down from $112 to $99 in 5 sessions), but Israeli strikes keep a floor under prices. The $95–$105 range is the new equilibrium while indirect talks continue.
- **Gold steady at $3,200–3,240:** Down from the $3,290 record but finding support. Gold is now pricing two things simultaneously: ceasefire optimism (bearish for gold) and consumer confidence collapse / stagflation fears (bullish for gold). These roughly offset.
- **Defence names fading:** LMT, RTX, NOC have given back 3–5% from war highs as ceasefire probability has risen from 30% to 45%. We're trimming from overweight to market-weight but maintaining exposure as a hedge against talks failing.

---

## MARKET SNAPSHOT — 6:45 AM ET

| Index / Asset | Level | Change | Note |
|---|---|---|---|
| S&P 500 (Tue Close) | 5,645 | +0.5% | Peace optimism held; 3 consecutive up days |
| S&P 500 Futs | 5,580 | −1.2% | TurboQuant + Israel strikes driving futures down |
| Nasdaq 100 Futs | 19,600 | −1.8% | Memory/semi selloff dragging tech lower |
| Dow Futs | 46,100 | −0.7% | Relatively better; less tech exposure |
| Brent Crude | $100.20 | +1.1% | Rebounding on Isfahan strikes; above $100 again |
| WTI Crude | $96.50 | +1.5% | Following Brent; war premium returning |
| Gold (Spot) | $3,230 | +0.9% | Safe haven bid on equity weakness + war escalation |
| VIX | 27.5 | +15% | Vol spiking on TurboQuant panic + geopolitical noise |
| 10Y UST | 4.28% | −2bp | Slight flight to safety; waiting for PCE tomorrow |
| DXY (Dollar) | 105.8 | −0.3% | Flat to lower on risk-off |
| Bitcoin | $67,500 | −2.5% | Tech selloff dragging crypto lower |

---

## WAR SIGNAL TRACKER — Thursday Assessment

| Signal | Detail | Bias |
|---|---|---|
| Pakistan mediation | Officially confirmed indirect talks. Pushing for Islamabad face-to-face Friday. | **BULL** |
| US proposal | 15-point plan on the table. Deadline extended to April 6. Genuine effort. | **BULL** |
| Iran counter-offer | 5 counter-demands issued. Engagement through proposals = active negotiation. | **BULL** |
| Trump rhetoric | "Get serious" to Iran. Frustrated but still engaged. No escalation signals. | **NEUTRAL** |
| Israel / IDF | Isfahan strikes overnight. Missiles in central Israel. Not party to any pause. | **BEAR** |
| Oil price | Brent $99–$100. Ceasefire premium deflating but Israeli strikes keeping floor. | **NEUTRAL** |
| Hormuz status | No new incidents this week. Iran hasn't threatened closure during talks. | **BULL** |
| Consumer damage | CB Confidence 92.2. Expectations 65.2. Inflation expectations 6.2%. Already baked in. | **BEAR** |
| Nuclear demands | Hardest gap. But both sides referencing JCPOA precedent. Template exists. | **NEUTRAL** |
| Casualty toll | 1,500+ killed in Iran. Public pressure building on both sides for resolution. | **NEUTRAL** |

**Assessment: 4 BULL / 2 BEAR / 4 NEUTRAL.** Holding near yesterday's 5/2/3 split. The Pakistan confirmation is the key upgrade. Israeli strikes prevent a BULL sweep. The ceasefire probability is now 45–50% — the highest of the war. The risk is that talks stall on the Israel dimension and the market re-prices lower.

---

## COMPANY HEADLINES

| Ticker | Company | Pre-Mkt | Catalyst |
|---|---|---|---|
| MU | Micron | −7% | TurboQuant panic. Down $90 from ATH in 8 days. We say BUY THE DIP. |
| 005930.KS | Samsung | −5% | Same TurboQuant fear. DRAM/NAND demand outlook unchanged. |
| 000660.KS | SK Hynix | −6% | HBM3E demand still insatiable. Knee-jerk sell on efficiency scare. |
| NVDA | NVIDIA | −2–3% | Sympathy with memory names. But TurboQuant is BULLISH for GPU demand. |
| COHR | Coherent | +1–2% | Photonics immune to TurboQuant. More inference = more interconnects. |
| LITE | Lumentum | +1% | Same dynamic. Optical demand increases with inference throughput. |
| GOOGL | Alphabet | +2–3% | TurboQuant originator. Inference cost advantage. Cloud margins expand. |
| LULU | Lululemon | Flat | Reports tonight AMC. Consumer confidence collapse = guidance risk. |
| DAL | Delta Air Lines | Flat | Jet fuel bounce. Brent back above $100 on Isfahan strikes. |
| LMT | Lockheed Martin | +1% | Defence re-bid on Israeli escalation overnight. |

---

## EARNINGS PREVIEW — Lululemon (LULU) Q4 FY25 After Close

> **EARNINGS — LULU Reports Tonight AMC | EPS Est $6.00 | Rev Est $3.61B**
>
> Lululemon enters this print in a precarious position. Consumer confidence just collapsed to recession-level readings (CB 92.2, Expectations 65.2). Inflation expectations are at 6.2%. Gasoline is $4.15. The consumer spending environment is the worst since early 2023 — and LULU is a $100+ legging company. Revenue growth has been decelerating for three straight quarters. International is the bright spot (China, Europe) but FX headwinds are real with DXY at 106.

- **Watch the guide:** The Q4 results matter less than FY27 guidance. If LULU guides below $9.3B FY revenue and $25 EPS, shares sell off 5–10%. The consumer data supports caution.
- **DTC vs wholesale:** Direct-to-consumer margins have been the margin expansion engine. Any deceleration in DTC growth signals the premium consumer is pulling back.
- **China exposure:** The one bright spot. LULU's China business is growing 25%+ and is not affected by the US-Iran war dynamic. If China strength offsets US weakness, the stock holds.

---

## TRADE IDEAS

> **BUY — MU — Micron at $355: The Jevons' Paradox Trade**
>
> MU has dropped $90 (19%) in 8 days from its ATH — $25 of which came today on TurboQuant. But the Q3 guide is still $33.5B revenue, 81% GM, $19.15 EPS. None of that changed. TurboQuant compresses KV-cache (inference working memory), not model weights (the dominant HBM consumer) or training memory. Every efficiency breakthrough in AI history has led to MORE memory demand, not less. Barclays still at $670. This is the best entry point since November.
>
> *Risk: TurboQuant is the start of a broader compression wave that structurally reduces HBM demand; DRAM pricing cycle turns.*

> **BUY — GOOGL — Alphabet: The TurboQuant Originator**
>
> Google developed TurboQuant. They will deploy it first. Their inference costs drop 6–8x before anyone else's. This gives Google Cloud a massive competitive advantage in AI services pricing. GCP's AI margins were already improving — TurboQuant accelerates this by potentially 12–18 months. Buy the innovator, not the panic.
>
> *Risk: Cloud spending slowdown; antitrust ruling forces structural changes; competitors replicate quickly.*

> **HOLD — COHR / LITE — Photonics: The TurboQuant Winners Nobody Is Talking About**
>
> More concurrent inference users per GPU = more data flowing between GPUs = more optical interconnects needed. TurboQuant is structurally bullish for photonics even as it's (wrongly) bearish for memory. The market hasn't figured this out yet. COHR and LITE are up while MU is down — the smart money is rotating from memory to interconnect. Hold and add on dips.
>
> *Risk: Broader tech selloff overwhelms sector dynamics; NVIDIA capex slowdown.*

> **WATCH — LULU — Don't Touch Before Earnings**
>
> Consumer confidence is at 12-year lows. Inflation expectations are 6.2%. Gas is $4.15. LULU is a $100-legging-company reporting into the worst consumer backdrop since 2023. The risk/reward is skewed to the downside on guidance. Wait for the print. If they guide above $25 EPS for FY27, buy. If below, short.
>
> *Risk: China strength saves the quarter; premium consumer proves resilient; stock gaps higher.*

---

## EVENT CALENDAR

| Day | Time | Event | Impact |
|---|---|---|---|
| Thu 3/26 | 8:30 AM | GDP Final Revision (Q4) | LOW |
| Thu 3/26 | 8:30 AM | Initial Jobless Claims | MED |
| Thu 3/26 | All Day | Google TurboQuant Paper — Market Digestion Day | **HIGH** |
| Thu 3/26 | AMC | Lululemon (LULU) Q4 Earnings | MED |
| Fri 3/27 | 8:30 AM | Core PCE Inflation (Feb) — THE MACRO EVENT | **HIGH** |
| Fri 3/27 | 10:00 AM | UMich Consumer Sentiment Final (Mar) | MED |
| Fri 3/27 | TBD | Pakistan Islamabad Talks — Possible Face-to-Face | **HIGH** |
| Apr 6 | 8 PM ET | Extended US Strike Deadline on Iran | **HIGH** |
| Apr 23–25 | | ICLR 2026 — TurboQuant Open-Source Release Expected | **HIGH** |

*Tomorrow is the most important trading day since FOMC: Core PCE at 8:30 AM tells us whether the inflation story is getting better or worse. If hot (>0.35% MoM), the Fed is vindicated and rate cuts are dead for 2026. If cool (<0.25%), there's a path back to 2 cuts and risk assets rip. Simultaneously, Pakistan could announce face-to-face Islamabad talks — the first direct diplomatic contact of the war.*

---

## BOTTOM LINE

### Two Disruptions. Two Different Timelines.

The market is processing two disruptions simultaneously: a war that is slowly ending and a technology breakthrough that is reshaping the AI supply chain. They operate on completely different timelines, and the market is confusing the two.

The war trade is unwinding. Brent is $99. Ceasefire probability is 45–50%. Pakistan is mediating. The April 6 deadline gives talks room. This is constructive for equities, destructive for oil and defence, and already partially priced in.

The TurboQuant trade is just beginning. The market's knee-jerk ("less memory needed = sell memory stocks") is the same mistake it makes with every efficiency improvement in tech. Jevons' Paradox will hold: cheaper inference means more inference means more GPUs means more HBM. MU at $355 with a $33.5B Q3 guide is a gift. GOOGL as the originator of the breakthrough is a gift. COHR/LITE as the interconnect beneficiaries are gifts.

**Buy the disruption. Sell the panic. Tomorrow's PCE will tell us which of these two stories dominates Q2.**

---

*For internal use only. Not investment advice.*
