# MORNING NOTE

# Thursday, March 26, 2026  |  Pre-Market Briefing

Wednesday's Ceasefire Optimism Evaporates; Nasdaq Enters Correction Territory

# EXECUTIVE SUMMARY

Yesterday's risk-on rally has been completely unwound. The S&P 500 fell 1.74% to 6,477, the Nasdaq plunged 2.38% to 21,408 (officially entering correction territory at -10% from its October high), and the Dow shed 1.01% to 45,960. The reversal came on three catalysts: (1) Iran explicitly rejected the 15-point U.S. ceasefire plan and denied any direct negotiations, (2) ECB President Lagarde warned that markets are "maybe overly optimistic" and signaled willingness to hike rates even for a temporary inflation overshoot, and (3) Google's TurboQuant algorithm announcement crushed memory chip stocks, adding a sector-specific shock to the broader macro sell-off. Oil surged back -- Brent settled at $108/bbl (+5.7%), WTI at $94.48 (+4.6%). Pre-market this morning shows further risk-off: Asia sold off overnight and European indices are opening lower.

# U.S.-IRAN CONFLICT: DETAILED SITUATION REPORT (WEEK 4)

Diplomatic Status

15-Point Plan Rejected: Iran formally rejected the U.S. ceasefire proposal delivered through Pakistani intermediaries. FARS news agency quoted an informed source saying Iran "does not accept a ceasefire" under these terms. Iran's Foreign Minister Abbas Araghchi told state media that backchannel exchanges through mediators do not constitute "negotiations with the U.S."

Iran's Counter-Proposal: Tehran countered with its own five-point plan, notably including a demand to retain control over the Strait of Hormuz -- a non-starter for the U.S. and Gulf states. The divergence between U.S. and Iranian frameworks is wide and growing.

Trump's Posture: In a Cabinet meeting, Trump said he would not commit to an agreement, stated oil prices and market damage were "not as bad as I thought," and expressed confidence in the war effort. He extended a five-day pause on strikes against Iranian energy infrastructure (expires Saturday), leaving a narrow diplomatic window before potential escalation.

Congressional Pressure: AP-NORC polling shows most Americans believe military action has gone too far. Sen. Elizabeth Warren fired a letter to incoming Fed Chair nominee Kevin Warsh questioning his fitness. The conflict is becoming a political liability.

Military Developments

Strait of Hormuz: Remains effectively blockaded by Iran. Tehran is reportedly drafting legislation to impose transit fees on vessels in the strait, signaling it views control of the waterway as a long-term strategic asset, not a temporary war measure.

Ongoing Strikes: Despite ceasefire talk, Iran's bombardment of Gulf states has not relented. Kuwait and Bahrain were hit with damaging strikes Tuesday night into Wednesday. Israel continues parallel operations.

Munitions Concerns: A RUSI report estimates the U.S. and allies have expended over 11,000 munitions in 16 days at a cost of $26B. The U.S. may be a month away from exhausting critical weapons stocks (THAAD air defenses, ATACMs, PrSM missiles).

Troop Deployments: Pentagon deploying thousands of additional Marines to the Middle East. The U.S. warned Iran it needs to "get serious" about ending the war or face a potential "final blow."

Sentiment & Market Impact Assessment

# The conflict is now the single largest driver of global cross-asset price action. Since March 1: S&P 500 is down ~6%, WTI surged from $72 to a peak of $112, VIX doubled from 13 to 25, and 10Y Treasury yields have risen to 4.39% on inflation fears. The Nasdaq is officially in correction territory (-10% from peak). The STOXX Europe 600 has fared even worse, down ~8.1% over the past month. The tape is binary: any credible de-escalation headline triggers a 1-3% equity rally and $5-10 oil drop; any rejection or escalation headline reverses it within hours. Wednesday's session was a textbook example -- the morning rally on ceasefire hopes was fully reversed by close.

KEY RISK: Trump's five-day pause on strikes against Iranian energy infrastructure expires Saturday. A dramatic military escalation grows more likely if no diplomatic progress is made. Markets are pricing almost no probability of a deal this week.

# GLOBAL EQUITY INDICES -- MARCH 25 CLOSE & MARCH 26 OVERNIGHT

# U.S. Close (March 25)

# March 26 Close (Thursday Session)

# Asia-Pacific (March 26 Overnight)

# Europe (Early Session March 26)

# INDUSTRY SENTIMENT TRACKER -- WAR & MACRO IMPACT

# A cross-sector sentiment assessment based on price action, analyst commentary, and positioning signals since the conflict began (March 1).

# TECH DEEP DIVE: GOOGLE TURBOQUANT & THE MEMORY DEMAND QUESTION

What Is TurboQuant?

Google Research unveiled TurboQuant on Tuesday -- a compression algorithm that reduces the KV (key-value) cache memory footprint of large language models by at least 6x with zero accuracy loss, and delivers up to 8x faster inference on NVIDIA H100 GPUs. The internet immediately dubbed it "the real Pied Piper" -- a reference to the HBO show Silicon Valley's fictional compression startup.

The algorithm works through a two-stage process: PolarQuant converts data vectors from Cartesian to polar coordinates (eliminating expensive normalization overhead), then QJL (Quantized Johnson-Lindenstrauss) applies a 1-bit error-correction pass. The result compresses each KV cache value from 16 bits to just 3 bits. Crucially, this requires no model retraining or fine-tuning -- it's a drop-in optimization for existing LLM inference pipelines.

Google tested against Gemma and Mistral models across five long-context benchmarks with zero measurable accuracy degradation. Open-source implementations were ported to MLX and llama.cpp within 24 hours. Official open-source release expected Q2 2026 alongside the ICLR presentation (April 23-25).

Market Impact: Memory Stocks Crushed

Implications for NVIDIA

# NVIDIA fell 3.83% on March 26 -- but the TurboQuant story is more nuanced for NVDA than for memory names. Analysts note that TurboQuant makes existing GPUs more efficient per dollar, which could accelerate GPU adoption in cost-sensitive use cases. The compression runs on NVIDIA hardware (H100s showed 8x attention speedups with 4-bit TurboQuant). The winners are Google (direct cost advantage), Google Cloud customers, and AI startups who can now run larger models on smaller hardware budgets.

# NVIDIA's own efficiency roadmap aligns with this trend. At GTC 2026 (March 16-18), Jensen Huang unveiled the Vera Rubin platform -- six new chips delivering a 10x reduction in inference token cost and 4x reduction in GPUs needed to train MoE models vs. Blackwell. The new NVIDIA Inference Context Memory Storage Platform with BlueField-4 is specifically designed to accelerate agentic AI reasoning with better memory management. NVIDIA also showcased NVFP4/FP8 quantization formats enabling 60% and 40% VRAM savings respectively.

ANALYST VIEW: Wells Fargo's Andrew Rocha: TurboQuant "raises the question of how much memory capacity the industry actually needs." But CNBC commentary described it as "evolutionary, not revolutionary" -- software efficiency gains don't reduce absolute hardware demand when AI workloads continue scaling exponentially. The real risk is to memory chip names; for GPU makers, efficiency gains expand the addressable market.

# COMMODITIES

Oil

Wednesday's ceasefire-driven decline was completely erased. Iran's rejection of the proposal and continued Strait blockage sent crude surging back above key levels. Gas at the pump has hit $8.29/gal in parts of Los Angeles. EIA forecasts Brent remaining above $95/bbl for the next two months, falling below $80 only if transit resumes. The adverse scenario (Hormuz closed through April) sees Brent peaking at $200/bbl in Q2.

Gold

Gold reversed sharply lower after Wednesday's bounce. Down from the $4,565 level, gold is suffering from a bizarre dynamic: it rallied on "war safe-haven" flows but is selling off on rising real yields and dollar strength. Gold is now down ~20% from its January all-time high of $5,589, though still up ~19% YTD. Miners are squeezed between falling gold and rising oil input costs.

# FIXED INCOME, FX & VOLATILITY

# For the first time since the conflict began, futures markets are pricing a greater-than-50% probability of a Fed rate INCREASE by year-end 2026, reflecting the inflation threat from sustained oil above $100. This is a dramatic shift from the easing expectations that prevailed pre-war. A lackluster U.S. Treasury note auction on Thursday added to bond market pressure.

# CENTRAL BANK WATCH: ECB PIVOT MOMENT

# LAGARDE BOMBSHELL: ECB President Christine Lagarde told an audience at "The ECB and Its Watchers" conference that the Iran conflict represents a "real shock" and that markets are "maybe overly optimistic." She warned that even a "not-too-persistent" inflation overshoot could warrant a "measured adjustment" (i.e., rate hike). The ECB held at 2.0% in mid-March and had been expected to CUT -- markets are now rapidly repricing for 25bp HIKES. ~35bp of ECB tightening is priced for 2026.

# The Lagarde comments triggered the sharpest leg down in Thursday's session, hitting growth-sensitive sectors especially hard. MUFG Research notes the ECB has already brought rates back to neutral, which makes it harder to stand pat vs. other central banks with more restrictive starting points. MUFG's adverse inflation scenario: headline HICP above 5% in both eurozone and UK if oil sustains $120/bbl and natural gas hits 100 EUR/MWh.

# DATA RELEASES & EARNINGS (MARCH 26)

Economic Data

Initial Jobless Claims: Fell to 210K (est. 211K). Continuing claims dropped to 1.819M, lowest since May 2024. Labor market remains tight despite macro headwinds.

# UMich Consumer Sentiment (Final March): 53.3, down 5.8% from Feb and 6.5% from a year ago (est. 54.0). Inflation expectations ticking higher on Iran war concerns.

Notable Earnings & Corporate Headlines

H&M Group Q1: Sales -1% in local currencies on 163 store closures (-4% footprint). Operating profit up 26% to SEK 1,512M; margin improved to 3.0% from 2.2%. Stock fell nearly 6% as investors focused on top-line weakness.

Meta Platforms (META) -7%: California jury found Meta and Alphabet negligent in a social media addiction case. Both companies plan to appeal.

Netflix (NFLX) +1.1%: Raised subscription prices across all tiers. Investors see pricing power as positive.

Henkel / Olaplex: Henkel agreed to acquire Olaplex for $1.4B ($2.06/share all-cash). OLPX surged 51%. Olaplex has fallen 92% since its 2021 IPO.

Brown-Forman +14.5%: Pernod Ricard reportedly evaluating a takeout of the Jack Daniel's maker.

Goldman Sachs: Reiterated Buy on Apple and Dell as beneficiaries of autonomous AI agents (OpenClaw). "High-end PC portfolios well positioned."

Robinhood: Authorized $1.5B stock buyback. Piper Sandler called it a beneficiary of "$100T generational wealth transfer."

SpaceX IPO: Rumors intensifying -- The Information reports it could raise $75B+, making it one of the largest IPOs in history.

# THE BOTTOM LINE

REGIME SHIFT IN PROGRESS. Three forces are converging to create a toxic mix for risk assets: (1) The U.S.-Iran war is grinding toward either escalation or a prolonged stalemate, with Trump's strike pause expiring Saturday and no credible diplomatic offramp in sight. (2) Central banks are pivoting from easing to tightening -- Lagarde's "real shock" warning is the clearest signal yet that the post-pandemic rate-cutting cycle is over, and the CME FedWatch showing >50% probability of a Fed HIKE is a watershed moment. (3) The TurboQuant shock is a microcosm of a broader AI narrative shift from "bigger models = more hardware" to "smarter algorithms = less hardware," which threatens the capex cycle thesis that has underpinned semiconductor valuations.

POSITIONING: The Nasdaq is in correction territory. The Dow is approaching it. The VIX is at 30. Brent is above $108 with no credible supply relief. The S&P has now posted its longest streak of weekly losses since 2022. This is not a market to be a hero in. Key levels: S&P 6,450 (September support), Brent $110 (acceleration point), VIX 30 (volatility regime boundary), 10Y UST 4.50% (next resistance). Watch Saturday's strike pause expiration -- it is the single most important near-term catalyst. Any escalation headline over the weekend could gap equities lower Monday. Defensive sectors (energy, utilities, pharma) continue to outperform; tech and consumer discretionary are the pain trades.