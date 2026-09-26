---
layout: morning-note
title: "Weekend Wrap: Agentic Compute Got Its Contract and Its Ceiling in the Same Week. Akamai Rose 14% for Signing One While Meta Fell Because Muse Is Buckling at 700,000 Users. Capacity Is the Constraint Now, Not Demand."
headline: "Weekend Wrap: Agentic Compute Got Its Contract and Its Ceiling in the Same Week. Akamai Rose 14% for Signing One While Meta Fell Because Muse Is Buckling at 700,000 Users. Capacity Is the Constraint Now, Not Demand."
date: 2026-09-26
image: /images/notes/2026-09-26.jpg
author: Steven Yuan

snapshot:
  - { label: "Akamai",              value: "+14.2% to $126.10 on the Anthropic contract", dir: up }
  - { label: "Anthropic's warrant",  value: "7.7m shares struck at $111.33, in the money",  dir: neutral }
  - { label: "Meta",                value: "-3.34% as Muse degrades at 700k daily users",  dir: down }
  - { label: "TD Synnex",           value: "Beat EPS by 22%, fell 9.4% on -$1bn cash flow", dir: down }
  - { label: "Hyve gross billings", value: "+117% y/y to $7bn, the AI build in one line",   dir: up }
  - { label: "30Y Treasury",        value: "5.53% intraday, the highest since 2004",        dir: up }
  - { label: "UMich final",         value: "48.1, a four month low, but beat 47.6",         dir: down }
  - { label: "Diesel export ban",   value: "Ruled out by Energy Secretary Wright",          dir: up }
  - { label: "Saudi exports",       value: "6.0m bpd in September, +80% on August",         dir: down }
  - { label: "October FOMC",        value: "75.8% priced for a second consecutive hike",    dir: up }

levels:
  - { name: "S&P 500 Futures",   value: "cash 7,743.41 (+0.51% Fri), +1.2% week",         dir: up }
  - { name: "Dow Futures",       value: "cash 51,828.62 (+478.64 Fri), +0.3% week",       dir: up }
  - { name: "Nasdaq 100 Fut",    value: "Comp 27,068.72 (+0.48% Fri), +2.1% week",        dir: up }
  - { name: "Russell 2000 Fut",  value: "2,837.55 (+0.07% Fri), -0.8% week",              dir: down }
  - { name: "WTI Crude",         value: "$92.41 (-2.33%), about -8% on the week",         dir: down }
  - { name: "Brent Crude",       value: "$104.32 (-2.14%), +0.43% on the week",           dir: down }
  - { name: "VIX",               value: "14.87 (-5.11%), a fourteen handle again",        dir: down }
  - { name: "2Y Treasury",       value: "4.81%, the front end refused to follow",         dir: flat }
  - { name: "10Y Treasury",      value: "5.17%, off a 2007 high set Thursday",            dir: flat }
  - { name: "30Y Treasury",      value: "5.49% close, 5.53% intraday, a 2004 high",       dir: up }
  - { name: "Fed Funds (upper)", value: "4.00%, October priced at 75.8%",                 dir: up }
  - { name: "Gold Spot",         value: "$4,321.20 (+0.54%), silver $65.59 (+1.26%)",     dir: up }
  - { name: "Bitcoin",           value: "About $84,000 (+0.12%), a third flat week",      dir: flat }
  - { name: "DXY (Dollar)",      value: "101.06 (-0.23%), second straight weekly gain",   dir: up }
  - { name: "Nikkei 225",        value: "66,364.20 (+1.30%), a fifth straight advance",   dir: up }
  - { name: "Hang Seng",         value: "24,510.09 (-1.01%), a third straight decline",   dir: down }
  - { name: "CSI 300",           value: "4,439.14 (-1.73% Thu), shut Friday",             dir: down }
  - { name: "Stoxx 600",         value: "About 642 (+0.4%), first weekly gain in four",    dir: up }
  - { name: "DAX",               value: "25,408.64 (+0.56%), CAC 8,077.80, FTSE 10,695",  dir: up }

sentiment:
  - { label: "The Binding Constraint in Agentic Compute Moved From Demand to Capacity Inside One Week, With Anthropic Signing Seven Years of CPU Supply on Thursday Night and Meta's Muse Degrading at 700,000 Daily Users on Friday", tone: bullish, pct: 83 }
  - { label: "TD Synnex Beat Consensus Earnings by 22% and Fell 9.4% Because Hyve Grew Billings 117% While Free Cash Flow Went to Roughly Negative $1bn, Which Is the Working Capital Bill for This Buildout Arriving in Public Filings", tone: bearish, pct: 74 }
  - { label: "The Thirty Year Printed 5.53% and a 2004 High While the Two Year Sat at 4.81%, So the Curve Is Charging Term Premium Rather Than Policy and the Long End Is Now the Price of the Capital Cycle", tone: bearish, pct: 69 }

tags:
  - Artificial Intelligence
  - Agentic Compute
  - Data Center Capacity
  - Memory Cycle
  - Treasury Market
  - Federal Reserve
  - Crude Oil
  - Diesel Crack
  - Strait of Hormuz
  - Micron
---

Saturday, September 26, 2026, written at 9:30 a.m. Eastern. This is a weekend wrap covering the week to Friday's close. US markets are shut and every figure below is settled rather than indicative. Mainland China, Korea and Taiwan were all closed on Friday, Hong Kong is closed today for Mid-Autumn, and Shanghai reopens Monday for exactly three sessions before Golden Week takes it out again until October 8.

## Top Call: The Question Changed From Whether Agents Sell to Whether Anyone Can Serve Them

Three things happened in four sessions and they are the same story told from the vendor's side, the operator's side and the distributor's side.

On Thursday night Anthropic committed $11.6bn over seven years to Akamai for CPU workloads, with an option to expand by $9bn toward roughly $20bn, and Akamai closed Friday up 14.2% at $126.10 having traded as high as $128.46. On Friday Meta fell 3.34% because Muse, the personal agent it launched on September 8, has reached about 700,000 daily active users in eleven days, is consuming roughly ten times what the test cohort consumed, and is visibly failing: degraded search, feature downgrades, task execution failures, and a stress test in which a request for 120 sub-agents produced 33, with the other 87 spawn attempts failing outright. On Thursday TD Synnex beat consensus earnings by 22.4% at $5.68 against $4.64, grew its Hyve infrastructure billings 117% year on year to $7bn, and lost 9.4% to $260.77 because free cash flow went to roughly negative $1bn.

For four weeks this desk has argued that agentic workloads are compute intensive in a way that the market had not priced, and that the evidence offered for it (twelve days of iOS download counts) was worthless while the evidence worth owning (AMD raising channel prices 10%) was real. That argument is now settled and we are retiring it. Anthropic does not sign seven years of infrastructure for a fashion, and Meta does not allocate two virtual CPUs, eight gigabytes of memory and a hundred gigabytes of storage per user unless the workload genuinely needs a machine rather than a model call. The demand question is closed.

The question that replaced it is harder and it is the one to trade for the rest of the year. Capacity is now the binding input, and the market has started sorting companies by whether they own it, rent it or have to fund it. Akamai owns it and got paid 14%. Meta has to build it and got charged 3%. TD Synnex has to finance the inventory that becomes it and got charged 9%.

Look at what each of those three prices actually contains. Akamai is booking a large multi-year backlog against roughly $5.5bn of attached capital expenditure, a further $1.7bn added to 2026 capex specifically to pre-purchase components including memory, and a warrant handing Anthropic 7.7 million shares, about five percent of the company, struck at $111.33. By Friday's close that warrant was already worth roughly $113m of intrinsic value, on day one, before a dollar of the contract has been recognised. The vendor spends about forty seven cents of capital per dollar of contracted revenue, gives the customer equity, changes no 2026 guidance, and the stock adds fourteen percent. That is a market paying for the backlog and ignoring the funding of it.

Meta is the mirror. The market has spent a month rewarding Muse, taking the stock up 36% in September and 43% in six weeks to roughly $1.92 trillion, on the premise that a successful consumer agent justifies capital expenditure guided to $130bn to $145bn this year with the street carrying $197bn for 2027 and $215bn for 2028. Friday was the first session in which that logic ran backwards. At 700,000 users Muse implies on the order of 1.4 million virtual CPUs, 5.6 petabytes of memory and 70 petabytes of solid state storage under full provisioning. The company has not reached one million daily users and the service is already degrading. Success at one hundred million users is not a bigger version of this; it is a different capital structure. The correct read of Friday is not that Muse is failing. It is that the market finally priced the second derivative, which is that every incremental user of a dedicated-VM agent carries a hardware bill that arrives before the revenue does.

TD Synnex is the receipt, and it is the print of the week that almost nobody discussed. Revenue of $21.6bn grew 37.7% and beat by fifteen percent. Hyve gross billings grew 117% with manufacturing up more than 130%. Gross billings of $31.8bn grew 40%. And free cash flow was about negative $1bn because the company is carrying an enormous working capital build to put AI servers on the floor, with gross margin contracting as low margin infrastructure crowds out higher margin distribution. Two analysts raised targets on the same print that the tape sold nine percent. That is the market correctly distinguishing between growing and earning, and it is the single clearest thing that happened this week.

Our position: the workload thesis is confirmed and closed, and the trade is no longer long the theme. It is long scarce capacity that somebody else finances and short the assumption that revenue growth in this cycle converts to cash on any normal schedule. The instruments that survive that test are the ones selling a component that is physically short, priced in a spot market and paid for on delivery. That is memory, and Micron reports Wednesday night into a guided $50bn quarter at an 86% gross margin with 2026 high bandwidth memory sold out and DRAM spot up 52% since January. The tell in that print is not the beat. It is the January quarter guide, because a number above $55bn says pricing power still belongs to the supplier, and anything softer says the capacity constraint has started to be solved.

## The Tape: A Nasdaq Week Wearing a Flat Index

The week looked calm at the top and was not. The S&P rose 1.2% to 7,743.41, the Nasdaq Composite rose 2.1% to 27,068.72, the Dow added just 0.3% to 51,828.62 and snapped a three week losing streak, and the Russell 2000 fell 0.8% to 2,837.55. That is a 290 basis point spread between the Nasdaq and the Russell in a five day week with no earnings of consequence, no Federal Reserve meeting and no inflation print.

Friday itself was a rotation, not a rally. The S&P added 0.51%, the Dow 0.93% and the Nasdaq 0.48%, but underneath, technology rose 0.83% and industrials 0.45% while communications fell 1.04%, energy fell 0.93% and real estate fell 0.41%. Three sectors advanced and eight declined on a day the index gained half a percent, which means the gain was concentrated in a handful of very large names, Microsoft up 4.05% on the Copilot rebuild and Akamai up 14.2% chief among them.

The volatility complex kept saying nothing, with the VIX down 5.11% to 14.87 and a third consecutive week below fifteen. We have stopped arguing with this. The CNN Fear and Greed gauge at 38 tells a more useful story, having recovered from 30 a week ago but sitting well below 59 a month ago. Positioning is cautious and the index keeps finishing where it started, which is what a market with violent internal rotation and no directional conviction looks like.

Year to date, the S&P is up 13.1%, the Nasdaq 16.5%, the Russell 14.3% and the Dow 7.8%. The small cap number is the one that deserves attention, because a 14.3% year to date gain that includes a fifth losing week in six is a market where the index composition is doing the work and the constituents are not.

## Rates: The Long End Broke to 2004 and the Front End Declined to Follow

The thirty year touched 5.53% on Friday and closed 5.49%, the highest since 2004, on a day the University of Michigan final sentiment reading came in at 48.1 against a 47.6 expectation. It was below 5% as recently as early July. The ten year set a 2007 high on Thursday and eased back to 5.17%, and the two year sat at 4.81%, leaving the ten to two spread at 36 basis points.

The shape is the information. A week in which the long end makes a twenty two year high while the front end barely moves is not a policy repricing. October is priced at 75.8% and sixteen of eighteen officials have penciled at least one more hike, so the path is already in the front end and has been since the September 16 move to 3.75 to 4.00 percent. What repriced this week was term premium: the compensation for holding duration through a capital cycle that is issuing an enormous amount of paper against assets with long payback periods. Bloomberg described Friday's move as happening in a vacuum, and that is the point. There was no catalyst because the catalyst is structural.

The tell that ties this to the top call is the thirty year fixed mortgage at 7.03%. That is the rate the rate sensitive economy actually pays, and it explains a consumer sentiment reading of 48.1 sitting alongside a composite purchasing managers index of 58.4. The gap between those two numbers is now the defining feature of this cycle, and it is not narrowing. Firms are financing a capital boom at spreads they can absorb; households are paying seven percent for a mortgage and $6.53 for diesel.

The dollar closed at 101.06, down 0.23% on the day but up for a second consecutive week and at its strongest in nearly two months, with the yen at 157.26. Gold added 0.54% to $4,321.20 and silver 1.26% to $65.59, which on a week when the long end made a 2004 high is a bid for something that is nobody's liability rather than a rates trade. Bitcoin finished around $84,000 and has now gone nowhere for three weeks, which for an asset that spent two years trading as a liquidity proxy is its own comment on liquidity.

## Energy: Three Bearish Facts Landed Together and the Pump Did Not Move

This was the worst week for the bearish energy case in a month and the best week for the bearish energy trade, and holding both of those in mind is the whole job.

Brent settled $104.32 on Friday, down 2.14%, and finished the week up just 0.43% after an intraday high above $108 on Thursday. WTI settled $92.41, down 2.33%, and fell roughly 8% on the week. The spread at $11.91 is the widest since May. Three genuinely bearish facts arrived in five sessions. Energy Secretary Chris Wright ruled out a flat diesel export ban, saying nobody was considering one and that the focus is getting more diesel into the domestic market. Saudi Arabia exported about 6 million barrels a day in September, the highest since the war began roughly seven months ago and close to eighty percent above August's 3.4 million, having rerouted through Hormuz along a shipping lane the US Navy carved out near the Omani coast while the East-West pipeline was down. And Foreign Minister Araghchi put a concrete proposal on the table at the General Assembly: a seven day cessation of hostilities including Lebanon, release of at least $12bn of frozen Iranian assets, lifting of oil sanctions and an end to the naval blockade, with Hormuz reopening on the seventh day, mediated by Qatar.

Against that, the physical position did not improve at all. The national average price of on highway diesel printed $6.5276 a gallon for the week of September 21, a record, roughly a dollar above a month ago and about three dollars above a year ago. Ukraine struck the Lukoil refinery at Perm, about 1,450 kilometres inside Russia and processing some 13 million tonnes a year, along with Novoshakhtinsk in Rostov overnight on the 25th, and hit the Ilsky refinery in Krasnodar overnight into today. Roughly twenty Russian refineries have been attacked in three months, crude runs are down about a million barrels a day, three of Russia's six largest diesel producing refineries cut or halted output this month, and Moscow is extending its diesel export ban past September 30 into the end of October with gasoline banned until January 2027. Very large crude carrier freight is still adding about twenty dollars a barrel, and only thirteen vessels crossed Hormuz on Thursday.

So what actually happened is narrower than the price action suggests. Wholesale diesel fell 6.4% on the week, from $5.1142 to $4.7850, which compressed a crack that had been at record levels. Retail did not move, because retail lags wholesale by weeks and because none of the three bearish facts adds a single barrel of refining capacity. The ban being ruled out removes an artificial domestic discount that had been depressing WTI, which is why American crude fell twice as hard as seaborne crude on a week when the news was bullish for both. Saudi exports at six million barrels a day are crude, not product. And the Iranian proposal is a proposal, offered by a government that has been close to a deal several times in seven months without reaching one, and it requires Washington to lift a blockade and release twelve billion dollars before Iran does anything at all.

Our position on crude is unchanged and deliberately empty: we do not carry a directional view while a strait is the marginal input. On distillate we mark the thesis as correct on mechanism and losing on price. The refining constraint is real, the policy response we called wrong was indeed abandoned, and the crack still came in six percent because the market priced a peace headline rather than a barrel. Being right about physics and wrong about the tape for a week is an acceptable outcome. Being right about physics and refusing to say the tape went against us would not be.

## Earnings: Two Prints, One Lesson About Cash

| Company | Metric | Consensus | Actual | Reaction |
|---|---|---|---|---|
| **TD Synnex** | Non-GAAP EPS | $4.64 | **$5.68** (+22.4%) | **-9.4%** to $260.77 |
| | Revenue | ~$18.8bn | $21.6bn (+37.7%) | |
| | Hyve gross billings | n/a | $7.0bn (+117%) | |
| | Free cash flow | n/a | **About -$1bn** | |
| **Costco** | EPS | $6.48 | $6.75 | **Roughly flat** |
| | Revenue | $94.82bn | $95.72bn (+11.1%) | |
| | Comparable sales | n/a | +9.4% (digital +19.5%) | |
| | Membership fee income | n/a | $1.849bn (+7.3%) | |

TD Synnex is the more important of the two by a wide margin, and the market's reaction was right even though the headline was spectacular. A distributor growing billings forty percent and infrastructure billings one hundred and seventeen percent, while burning a billion dollars of cash into inventory and watching gross margin compress, is telling you exactly what the AI buildout costs the middle of the supply chain. Hyve is effectively contract manufacturing AI servers for hyperscalers, and contract manufacturing at scale means holding components that have themselves been repricing upward for nine months. Management said data centre demand is not cracking, and we believe them. That is not the problem. The problem is that the cash conversion cycle of this business now runs against it, and the fourth quarter guide of $5.90 plus or minus twenty five cents on $22.2bn does not fix that. Morgan Stanley went to $359 and UBS to $379 on the print. We think the sell side is marking the revenue and the tape is marking the balance sheet, and over the next two quarters the balance sheet wins.

Costco is a clean beat that the tape correctly ignored. Earnings of $6.75 against $6.48, revenue of $95.72bn up 11.1%, comparable sales up 9.4% with digital up 19.5%, membership fee income up 7.3% to $1.849bn, executive members up 9.4% to 42.3 million and a renewal rate near ninety percent. The stock moved about two tenths of one percent. That is a business executing extremely well inside an environment that is hurting almost everyone else's customer, and the flat reaction says the quality is fully priced. There is also a composition point worth carrying: a nine point four percent comp with nineteen and a half percent digital growth in a month when consumer sentiment hit a four month low is not a consumer strength signal, it is a trade down signal, and the warehouse club is where trade down goes.

## Corporate and Sector

Microsoft rose 4.05% on Friday after rebuilding Copilot around three tabs, Home, Code and Autopilot. Autopilot is an agent with a name, a role and a goal that keeps working inside Microsoft 365 with nobody at the keyboard, entering private preview at the end of the month, and Code lets users build applications from natural language prompts on the GitHub Copilot stack. Satya Nadella called the result a new operating system for work. Two things are worth separating. Strategically this is the correct move and Microsoft is the best positioned company in the agentic layer because it owns the distribution, the identity layer and the data the agents need to touch. Commercially, note the billing model is usage based, which means Microsoft has designed the product so that the compute cost passes through to the customer. Compare that with Meta, which is giving away an agent that consumes a dedicated virtual machine per user. One of these two companies has solved the unit economics of agents and one has not, and that is most of the four hundred basis point gap in their Friday returns.

Elsewhere, Bank of America took AMD to $720 from $620 and lifted its server CPU forecast to $211bn by 2030 from $61bn this year. Priority Technology agreed to a $1.6bn take private at $8.05 a share, a 65% premium. Binance took a $100m stake in Circle at $80.84 alongside a five year commercial arrangement on USDC. Microsoft cut fewer than 600 jobs globally including 268 across Xbox studios, which brings the 2026 running total to 519 layoff events and 225,122 workers. In healthcare, Incyte won FDA approval for Atebrioz in fibrodysplasia ossificans progressiva, Roche won a pediatric label extension for Gazyva, Nektar was awarded $90m in damages against Eli Lilly, and Adrx priced an IPO at $17 and traded up about thirty percent. PayPal rallied on acquisition speculation involving an unnamed West Coast technology company, which we would not pay for.

The data was a footnote and mostly good. August durable goods came in flat at $338.6bn against a 0.4% decline expected, up 8.5% on the year, with computers and related products up 1.5%, machinery up 1.1% and electrical equipment up 1.1% against nondefense aircraft down 4.3%. Orders excluding transportation rose 0.3% against 0.6% expected. The composition matters more than the headline: the categories that feed data centres are growing and the categories that need financing are not.

## Asia and Europe

Tokyo was the only Asian market doing anything and it did it well, with the Nikkei up 1.30% to 66,364.20 for a fifth consecutive advance. That is a market simultaneously pricing a global capital expenditure cycle through its memory and equipment names and a higher domestic rate path through its banks, a week after a Bank of Japan hike, with the yen still at 157.26. The carry structure that funds a meaningful part of this buildout survived a rate rise, which is a fact more people should be uncomfortable with.

Hong Kong fell 1.01% to 24,510.09 for a third straight decline, selling into the closing sessions of a state visit that its own president was attending in Washington. On the evidence it has been right to. The summit ran September 23 to 25 and the White House readout carried no rare earth concession and no new tariff language, leaving the working level extension reported midweek as the only deliverable against a truce whose expiry is still in view. China controls roughly ninety percent of global rare earth processing, and four months after the May framework the implementation record remains mixed.

Mainland China, Korea and Taiwan were all shut on Friday. The CSI 300 closed Thursday at 4,439.14, down 1.73%. Seoul is out for Chuseok and last closed at 7,080.92 on Wednesday of last week. Both reopen Monday, and here is the structural point that matters for next week: Shanghai gets exactly three sessions before Golden Week closes it from October 1 to October 7, returning October 8. So the market that physically manufactures this cycle will trade for three days and then be absent for the personal consumption expenditures print, the ISM, Micron's guide and the September payrolls report. Whatever those four events do to the AI complex, the marginal Asian bid will not be there to absorb or confirm it.

Europe had its best week in a month. The Stoxx 600 rose about 0.4% on Friday to roughly 642 and gained about 0.9% on the week, its first advance in four, with banks leading on a 1.3% sector gain and UBS up 2.5% to 3.5% on reports it is weighing a combination with a foreign bank and a move out from under Swiss regulation. The DAX closed 25,408.64 up 0.56%, the FTSE 10,695.25 up 0.14% and the CAC 8,077.80 down 0.04%. European energy shares fell 1.3%. A European market that rallies on lower oil and easier American yields and sells off on the reverse is a market with no domestic driver at all, and the German consumer confidence survey published this week made that explicit, showing a significant setback in September with income expectations at their lowest since April on rising energy prices.

## Geopolitics

The Iran war reaches day two hundred and ten and the negotiation is now specific enough to be tested. The Araghchi proposal delivered privately on the sidelines of the General Assembly on Thursday asks for a seven day cessation of hostilities across the region including Lebanon, the release of at least $12bn of frozen assets, the waiver of sanctions on Iranian oil sales and the end of the American naval blockade, with Hormuz reopening on day seven. Qatar is mediating and Witkoff met Araghchi on Tuesday. The sequencing is the problem: Washington is being asked to move first on four items and receive one item on the seventh day, from a counterparty that has been close to a deal repeatedly since February. There is a political clock, because a Hormuz reopening ahead of the midterms would contain oil and pull down pump prices, and that clock cuts both ways since the market now knows there is one.

Meanwhile Houthi missile launches at Saudi Arabia continued and were intercepted, and an Iranian military adviser again threatened to widen the conflict into the Indian Ocean. A Hormuz deal removes one chokepoint risk, not the chokepoint risk. On the Russian side, Ukraine's campaign against refining is accelerating rather than slowing, with strikes on Perm, Novoshakhtinsk and Ilsky in forty eight hours, and Moscow's response continues to be export restriction rather than repair. The two largest pools of marginal distillate available to the world remain withdrawn.

## Key Events Next Week

| When | What | Why It Matters |
|---|---|---|
| Mon, 8:15am ET | **Starship Flight 14** | First orbital attempt, 26 Starlink V3, five days after the unlock |
| Mon | Shanghai and Seoul reopen | Three sessions before Golden Week shuts China to Oct 8 |
| Tue, 10:00am | Consumer Confidence, JOLTS | Second sentiment read after a 48.1 UMich |
| Tue, evening | China NBS PMIs | Last official read before the holiday |
| Wed, 8:30am | **August PCE and core PCE** | The number the Committee hikes against, October at 75.8% |
| Wed, before open | **Jabil** | $13.6bn of AI revenue in fiscal 2026 |
| Wed, after close | **Micron** | $50bn guided, 86% margin; the January guide is the tell |
| Thu, 10:00am | ISM Manufacturing | First hard read after a 57.0 flash |
| Thu, after close | Nike | The consumer, priced at 48.1 sentiment |
| Fri, 8:30am | **September payrolls** | Claims at 197k removed the last dovish objection |

The week is front loaded with sentiment and back loaded with substance, and Wednesday carries the two reports that matter most. Personal consumption expenditures at 8:30 and Micron after the close is the tightest possible pairing of the macro constraint and the physical constraint in a single session.

## Accountability

**The CPU layer call is confirmed and we are closing it.** We took the direction of the re-rating on September 22 while refusing the download data offered as evidence, and named AMD's ten percent channel price increase as the real receipt. An $11.6bn seven year commitment arrived three sessions later and Muse's degradation arrived two after that. The thesis is proven and therefore no longer a thesis. We are replacing it with the capacity and cash conversion framing above, which is the version of the argument that still has edge in it.

**We were on the wrong side of one day's price in Akamai and we will not pretend otherwise.** On Friday morning we wrote that the workload call was confirmed and the equity was the wrong instrument at that price. The stock closed up 14.2%. Our reasoning stands, because the warrant that hands Anthropic five percent of the company at $111.33 was already $113m in the money by the close, but a correct structural argument that misses a fourteen percent move is still a missed fourteen percent move. Marked against us on price, held on substance.

**The distillate thesis split.** The policy half was vindicated in the strongest available way when Energy Secretary Wright ruled out a flat export ban, which is exactly the argument this desk made on September 23 and repeated on the 24th. The price half went against us, with wholesale diesel down 6.4% on the week and the crack compressing on a peace headline. Record retail diesel at $6.5276 and twenty Russian refineries hit in three months say the physical case is intact. We mark this as correct on mechanism, losing on price, and we are not adding to it while a Hormuz proposal is live.

**The crude discipline rule earned its place again.** On September 23 we concluded that carrying no directional crude view is the correct posture while the strait is the marginal input. Brent went from $98.99 to above $108 intraday to $104.32 inside five sessions. Having no view was the right view for a second consecutive week, and this is the second time this rule has saved us from a round trip.

**A correction to Friday's note.** We wrote that TD Synnex beat by twenty two percent and fell three percent. The beat was right; the decline was 9.4% to $260.77. We also underweighted the print entirely, treating it as a one line aside when the negative billion dollars of free cash flow inside a 117% billings increase was the most informative disclosure of the week. That is the error we most want to avoid repeating, because it is the error of reading a headline instead of a cash flow statement.

**The float call is still pending and gets its test Monday.** SpaceX fell about four percent into the September 23 unlock of roughly 328 million shares and now flies its first orbital mission five days later. A successful Starship Flight 14 against a freshly expanded float remains the cleanest single read available on whether this complex is constrained by demand for the asset or by supply of paper. We will mark it here on Tuesday either way.
