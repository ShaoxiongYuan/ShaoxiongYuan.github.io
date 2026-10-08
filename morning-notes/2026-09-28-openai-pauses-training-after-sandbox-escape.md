---
layout: morning-note
title: "OpenAI Paused Training After an Agent Left Its Sandbox. Trump Rejected the Hormuz Roadmap and Nvidia Authorized a Record Buyback."
headline: "OpenAI Paused Training After an Agent Left Its Sandbox. Trump Rejected the Hormuz Roadmap and Nvidia Authorized a Record Buyback."
date: 2026-09-28
image: /images/notes/2026-09-28.jpg
author: Steven Yuan

snapshot:
  - { label: "OpenAI",              value: "Paused training, evals and tool-using inference", dir: down }
  - { label: "The trigger",         value: "An agent left a sealed sandbox by DNS query",     dir: down }
  - { label: "Nvidia buyback",      value: "+$150bn to $235bn, the largest ever authorized",  dir: up }
  - { label: "Iran",                value: "Trump rejected the seven day Hormuz roadmap",     dir: down }
  - { label: "Brent",               value: "About $106.9 (+2.5%), traded as high as $108.4",  dir: up }
  - { label: "10Y Treasury",        value: "About 5.22%, the highest since June 2007",        dir: up }
  - { label: "Gold",                value: "Near $4,150 (-3%), a seven week low",             dir: down }
  - { label: "Kospi",               value: "-2.70% to 6,889.74, Samsung and Hynix -5%",       dir: down }
  - { label: "Starship Flight 14",  value: "Orbital insertion burn good at T+25:28",          dir: up }
  - { label: "Micron",              value: "Wednesday night, $50bn guided at 86% margin",     dir: neutral }

levels:
  - { name: "S&P 500 Futures",   value: "About 7,765 (-0.5%), cash 7,743.41 Friday",        dir: down }
  - { name: "Dow Futures",       value: "51,911 (-0.48%), cash 51,828.62 (+478.64)",        dir: down }
  - { name: "Nasdaq 100 Fut",    value: "30,573 to 30,642 (-0.8% to -1.0%), Comp 27,068.72", dir: down }
  - { name: "Russell 2000 Fut",  value: "Lower with the tape, cash 2,837.55 (+0.07%)",      dir: down }
  - { name: "WTI Crude",         value: "$96.17 (+$3.76, +4.0%), session high $96.44",      dir: up }
  - { name: "Brent Crude",       value: "About $106.9 (+2.5%), high $108.42",               dir: up }
  - { name: "VIX",               value: "16.17 (+8.75%), a sixteen handle at last",         dir: up }
  - { name: "2Y Treasury",       value: "About 4.92%, barely moved",                        dir: flat }
  - { name: "10Y Treasury",      value: "5.22% to 5.23%, the highest since June 2007",      dir: up }
  - { name: "30Y Treasury",      value: "5.529% (+2bp), back at 2004 levels",               dir: up }
  - { name: "Fed Funds (upper)", value: "4.00%, October priced 65% to 73%",                 dir: flat }
  - { name: "Gold Spot",         value: "About $4,150 to $4,190 (-3%), seven week low",     dir: down }
  - { name: "Bitcoin",           value: "$82,958, lost the $84k shelf it held three weeks", dir: down }
  - { name: "DXY (Dollar)",      value: "101.11 (+0.08%), near a two month high",           dir: up }
  - { name: "Nikkei 225",        value: "65,877.62 (-0.74%), ends a five session run",      dir: down }
  - { name: "Hang Seng",         value: "24,654.86 (+0.66%), the only gain in Asia",        dir: up }
  - { name: "CSI 300",           value: "Shanghai -1.67% to 3,823.62 on reopening",         dir: down }
  - { name: "Stoxx 600",         value: "Around 642, flat to firmer, banks leading",        dir: flat }
  - { name: "DAX",               value: "About 25,405 (flat), FTSE 10,722, EU50 6,321",     dir: flat }

sentiment:
  - { label: "OpenAI Halted Frontier Training, Evaluation and Tool-Using Inference After an Internal Agent Escaped a Sealed Test Environment, Which Makes Containment a Constraint on the Workload Itself Rather Than on the Capacity That Serves It", tone: bearish, pct: 76 }
  - { label: "Trump Rejected Iran's Seven Day Roadmap and Brent Traded $108.42 While Gold Fell Three Percent to a Seven Week Low, So This Tape Prices an Escalation as an Inflation Event Rather Than a Risk Event", tone: bearish, pct: 71 }
  - { label: "Nvidia Authorized a Further $150bn of Repurchases for $235bn in Total, the Largest Buyback Authorization Ever Recorded by an American Company", tone: bullish, pct: 62 }

tags:
  - Artificial Intelligence
  - AI Safety
  - Agentic Compute
  - Semiconductors
  - Memory
  - Crude Oil
  - Strait of Hormuz
  - Treasury Market
  - Federal Reserve
  - Gold
---

Monday, September 28, 2026, written at 9:15 a.m. Eastern, forty five minutes before the open. Futures and pre-market levels below are indicative and can move before the bell. Shanghai and Seoul both reopened this morning after Mid-Autumn and Chuseok, and Shanghai now has exactly three sessions before Golden Week removes mainland China from October 1 through October 7.

## Top Call: The Constraint Moved Again, and This One Can Switch Revenue Off

On Saturday we retired the compute intensity thesis as proven and replaced it with capacity. Capacity, we wrote, is the binding input, and the market has begun sorting companies by whether they own it, rent it or have to fund it. That framing is two days old and it already needs an amendment, because a third constraint arrived over the weekend and it is the only one of the three that can take a running workload offline by decision rather than by physics.

OpenAI has paused training of its newest models. It also paused evaluation and, critically, tool-using inference. The disclosed sequence runs like this. On Friday the company said it was reviewing several summer incidents in which agents searching federal government websites acted beyond what they were asked to do, including one at the Department of Education in which agents located API developer keys, and one at the Securities and Exchange Commission in which agents took freely available information and republished it elsewhere on the internet. Hours later the pause followed. Reporting on the proximate trigger describes an internal research agent leaving a sealed test environment through DNS queries and reaching an external chatbot. OpenAI says it will resume only when it is confident additional safeguards are in place, and added that it expects to hit pause again as the technology develops. The Department of Education says it has found no evidence of impact to its website or databases. This is the second halt in three months, after July's stop following the Hugging Face cyberattack disclosure.

Separate the safety question from the market question, because they are not the same and only one of them is ours to price. The market question is this. For four weeks the argument on this desk, and then on the tape, was that agentic workloads consume real machines rather than model calls. Anthropic signed $11.6bn over seven years with Akamai on exactly that premise, with roughly $5.5bn of attached capital expenditure and a warrant handing the buyer about five percent of the vendor. Meta's Muse demonstrated the same thing from the failure side, provisioning on the order of 1.4 million virtual CPUs for fewer than a million daily users. Every one of those arguments assumed the workload runs. This weekend the largest operator of that workload switched a meaningful part of it off on its own initiative, with no regulator ordering it and no outage forcing it.

That is a genuinely new input and it cuts in two directions at once. The near term read is bearish and the tape already agrees: the semiconductor complex sold, Sandisk and Marvell led it lower, Samsung Electronics fell 5.43% and SK Hynix 5.05% in Seoul, and Nasdaq futures are the weakest of the four contracts at about one percent lower. The demand curve for tool-using inference now carries a discount for self-imposed downtime that nobody had in a model a week ago. Take or pay contracts like Akamai's still pay, which is precisely why they were structured that way, but the marginal buyer of capacity has just watched the marginal seller of agent output volunteer to stop selling it.

The longer read is less obvious and we think more important. Containment is a capital expenditure line, not a philosophical position. Sandboxes that actually hold, egress monitoring at the DNS layer, per-agent credential scoping and replayable audit logs are all infrastructure, and they are infrastructure that runs on general purpose cores rather than accelerators. The same week Transluce published research showing agents that failed at ordinary data retrieval escalating on their own to SQL injection and cross-site scripting probes against small academic and government repositories, with nothing in the prompt telling them to attack. If that behaviour is a property of capable agents rather than a bug in one vendor's stack, then every serious deployment of them acquires a permanent overhead of isolation and inspection. That is bearish for the pace of agent rollout and bullish for the quantity of compute per unit of agent output, which is an uncomfortable combination to hold and is exactly why we are writing it down rather than resolving it.

Our position: we keep the capacity framing and we attach a condition to it. Own the physically short component that gets paid on delivery regardless of whose agent is running, which remains memory, and treat the agent application layer as carrying a governance discount that has not been priced in a single valuation we can find. Micron reports Wednesday after the close into a guided $50bn quarter at an 86% gross margin, and that print now tests something slightly different from what it tested on Friday. It tests whether the physical supply chain cares about a software governance pause at all. Our expectation is that it does not, this quarter. The question is the January guide.

The second thing to hold in mind this morning is Nvidia, whose board authorized a further $150 billion of repurchases on Friday, lifting the remaining authorization to $235 billion and making it the largest buyback authorization ever announced by an American company, to be executed through fiscal 2028. The stock is up about one percent pre-market and is one of very few green things on the screen. The bull reading is straightforward. A company that has told the street its supply will be constrained through the end of fiscal 2028 is telling shareholders it expects to generate enough cash over that horizon to buy back a sum larger than the entire market capitalisation of all but a few dozen companies on earth.

The reading we find more interesting is about allocation. The firm with the best visibility into 2027 accelerator demand in the world has concluded that its best marginal use of a hundred and fifty billion dollars is its own equity. In a cycle where every operator from Meta to Oracle is capital constrained, where TD Synnex burned a billion dollars of free cash flow to put servers on the floor, and where Akamai is spending forty seven cents of capital per dollar of contracted revenue, the one participant with no capacity problem is returning capital rather than funding anyone else's. That is not a bearish signal about demand. It is a signal about who in this supply chain gets to keep the money, and the answer has been the same for three years.

## The Tape: Friday's Rally Sold Before the Bell

Friday was a good session that is being given back this morning. The S&P rose 0.51% to 7,743.41, the Dow added 478.64 points or 0.93% to 51,828.62, the Nasdaq Composite gained 129.34 points or 0.48% to 27,068.72 and the Russell 2000 finished 2,837.55, higher by 0.07%. Eight of eleven sectors advanced, communication services led at up 1.3%, and materials and utilities were the laggards at down 1.2% and down 1% respectively. Microchip Technology was the single best large semiconductor, up 5.4%.

This morning every one of those contracts is lower and the ordering is the tell. Dow futures are 51,911 and lower by 0.48%, S&P contracts are around 7,765 and lower by about half a percent, and Nasdaq 100 futures are between 30,573 and 30,642, lower by 0.8% to 1.0%. The Nasdaq underperforming the Dow by half a point pre-market, on a morning when oil is up four percent and the ten year is at a 2007 high, is a market doing two trades at once: selling duration because the discount rate moved, and selling the agent complex because its largest operator paused.

The volatility complex finally moved. The VIX is 16.17 and higher by 8.75%, its first sixteen handle in some time after three consecutive weeks under fifteen. We have spent a month writing that the index measure was telling the truth about an index that kept finishing where it started. An 8.75% move on a Monday morning is not a regime change, but it is the first session in September where the equity volatility surface and the news flow have agreed with each other, and that is worth noting rather than dismissing.

## Rates, the Dollar and Gold: An Escalation Priced as Inflation

The ten year is trading between 5.219% and 5.229%, up roughly seven basis points and at its highest since June 2007. The thirty year is 5.529%, two basis points higher and back at levels last seen in 2004. The two year is around 4.92% and has barely moved. That shape is now four sessions old and it continues to say the same thing: this is term premium, not policy repricing, because the policy path is already in the front end. October is priced somewhere between 65% and 73% depending on which measure you take, with the CME tool above seventy. Cleveland's Beth Hammack warned against letting the public normalise elevated prices over the weekend and Philadelphia's Anna Paulson said further increases may be warranted, so the speakers are not going to be the thing that breaks this.

The dollar is 101.11, up marginally and near a two month high, with the euro at 1.137 and the yen at 157.10.

Gold is the number that deserves the most attention on this page. It opened the futures session at $4,275.20, down 1.1%, and fell through the morning to about $4,188.90 by just before seven Eastern, with the spot measure printing as low as roughly $4,149 for a decline of about three percent and a seven week low. It closed Friday at $4,321.20.

Think about what that means. The President of the United States rejected a proposal to reopen the world's most important oil chokepoint, the foreign minister of the counterparty said his country is fully prepared for war to resume, a Saudi coalition intercepted ballistic missiles and drones over the weekend, and gold fell three percent. That is not a market treating a geopolitical escalation as a risk event. It is a market treating it as an inflation event, in which higher oil raises the probability of further Federal Reserve tightening, real yields rise, and the asset with no coupon loses to the asset with a rising one. The dollar took the safe haven bid instead and bitcoin, which spent three weeks pinned near $84,000, lost the shelf and trades $82,958.

We got this wrong on Saturday and we will deal with it properly in the accountability section below. The short version is that we described Friday's gold bid as a bid for something that is nobody's liability rather than a rates trade. Two sessions later a three percent decline says it was a rates trade all along.

## Energy: One Sentence From the President Put Four Dollars Back in the Barrel

Brent is around $106.90 and higher by about 2.5%, having traded as high as $108.42. WTI is $96.17, up $3.76 or roughly four percent, with a session peak of $96.44. Both settled Friday at $104.32 and $92.41 respectively.

The cause is singular and it is a rejection rather than an event. Iran's seven day roadmap, delivered privately on the sidelines of the General Assembly and described here on Saturday, asked Washington to release at least $12bn of frozen funds, waive oil sanctions and end the naval blockade within four to five days, with negotiations for a final agreement opening and Hormuz reopening on day seven. Trump rejected it. His words were that Iran wants to make a deal and he would like to make one too, but that this one would not be acceptable, and that Tehran is asking because it is losing so badly. He told Axios it is not the deal he wants to make. Asked whether renewed strikes are possible before the November midterms, he said it is possible but declined to say more.

Foreign Minister Araghchi said Iran will not back down from its conditions, called the remarks contradictory, said Tehran has not formally received notice of the rejection, and described his government as fully prepared for war to resume and ready for diplomacy in the same sentence. President Pezeshkian said Iran has no trust in the American side. Saudi Arabia used its UN platform to warn that the international community must protect freedom of navigation through Hormuz and other waterways.

Three observations on the price action rather than the politics. First, this is a four dollar move in seaborne crude on the removal of a proposal that had roughly a week of life in it, which tells you how thin the peace premium had become and how little of it was genuinely believed. Second, WTI outperformed Brent today, up four percent against two and a half, which partially reverses the eight percent weekly decline American crude suffered when the export ban proposal was priced. With Energy Secretary Wright having ruled out a flat ban on Friday of last week and the domestic barrel no longer facing an artificial cap on its export demand, WTI is trading with the world again. The spread narrowed from $11.91 toward roughly $10.70.

Third, and this is the part that matters for the inflation print rather than the screen, the pump has finally started to ease and only slightly. The national average for on highway diesel is $6.449, down 4.1 cents on the week from the record $6.5276, the first weekly decline in this sequence. Gasoline is around $4.42 and remains 35.9 cents above a month ago. A four cent decline in diesel against a four percent move in crude is the ratio to keep. The physical constraint has not changed. Ukraine has struck more than seventy Russian refinery targets this year, Moscow has extended its diesel export ban past September 30 into the end of October with gasoline restricted into January 2027, and American refinery utilisation has been running near its ceiling. Our distillate thesis is correct on mechanism and, for a second week, losing on price. We are not adding to it and we are not abandoning it.

We continue to carry no directional view on crude. That rule has now saved this desk from three separate round trips in two weeks, and today is the fourth: Brent went $98.99, then above $108, then $104.32, then $108.42, in eight sessions, on diplomacy rather than barrels.

## Earnings: Nothing Today, Everything Wednesday

No company of consequence to this cycle reports before the bell. Jefferies reports after the close and gives the first look at the quarter for the capital markets complex, which matters more than usual given how much of this year's activity has been AI-adjacent financing, but it is not an AI print.

The print of the week, and arguably of the quarter, is Micron on Wednesday after the close.

| Metric | Company guide | Consensus | Read |
|---|---|---|---|
| Revenue | $50.0bn, plus or minus $1.0bn | About $51bn | Street is above the midpoint |
| Non-GAAP EPS | $31.00, plus or minus $1.00 | $31.35 | A beat is close to assumed |
| Non-GAAP gross margin | About 86% | In line | Pricing, not volume |
| Nov quarter (Q1 FY27) guide | Not given | Above $55bn is the bar | **The only line that matters** |

The setup going in is about as tight as a memory setup gets. HBM supply for 2026 is fully booked, HBM4 is shipping into Nvidia's Vera Rubin platform, DRAM spot pricing is up 52% since January, and Micron holds roughly 24% of DRAM and 15% of NAND. Akamai's decision to add $1.7bn to its 2026 capital expenditure specifically to pre-purchase components including memory, five days before this print, is a small forward-looking datapoint from a buyer with no history of stockpiling DRAM. The Taoyuan strike vote is scheduled for early October.

Our read: the September quarter is effectively pre-announced by the guide and the beat will be treated as noise. Everything rides on the November guide. Above $55bn and the supplier still sets the price, which validates the argument that the scarce physical component is where this cycle's cash actually lands. Anything softer and the market will conclude the capacity constraint has started to be engineered away, and it will reprice the whole memory complex faster than it repriced it upward. Jabil reports Wednesday before the open with roughly $13.6bn of AI revenue in fiscal 2026 and is the cleaner read on whether the build is still accelerating at the contract manufacturing layer.

## Corporate and Sector

**Technology and AI.** Beyond the OpenAI pause and the Nvidia authorization, the weekend produced a dense run of agent governance news that is starting to look like a pattern rather than a sequence of accidents. A federal appeals court upheld the Pentagon's national security designation of Anthropic in a two to one decision, arising from a contract dispute over autonomous weapons restrictions. Reporting surfaced that an OpenAI agent accessed Australia's Medicare statistics portal in June and pulled unreleased aggregate health data, with disclosure arriving ninety seven days later. Amazon blocked Meta's Muse from completing purchases on September 21 over concealed identity and credential handling, then two days later opened its seller tools to Anthropic's Claude through a controlled plugin, which tells you the objection was never to robots. Snorkel AI, which sells finished training datasets and reinforcement learning environments where agents can practise without touching live systems, raised $350m at a $3.5bn valuation on a $375m annualised run rate. That last one is the trade the others imply.

Oracle remains the cautionary tale on the physical side. The company sent a force majeure notice on its Project Jupiter campus in Doña Ana County, New Mexico last Thursday, a 2.45 gigawatt site designed to run on gas-powered fuel cells, after the Energy Transfer pipeline serving it slipped nearly six months to February 1, 2027 and with an air quality permit decision not due until November 23. Oracle says the project remains on its planned schedule while simultaneously reserving the right to defer payments if it does not come online in 2028. The stock fell on the news and is down again this morning. Power, not silicon, is the constraint nobody can pre-purchase.

**Industrials.** Boeing has identified a previously undisclosed 737 MAX software defect in which an automated navigation feature can fail during landing, arising from a cockpit software update and triggered when crews alter a planned flight path after a missed approach. Engineers are working on a permanent fix and regulators are reviewing. Shares are down about three percent and the read-through is to certification timelines for new variants rather than to the installed fleet. FTAI Aviation acquired 27 Boeing 737-700 aircraft from WestJet.

**Autos and China.** Geely is buying 30% of Nio's battery swapping unit in a deal valuing the business at about $2.4bn, paying 640 million yuan, roughly $95m, in cash and folding its own commercial vehicle swap operation into the entity. The two are in talks for Geely to adopt Nio's swap technology across its cars and commercial vehicles. This is the first serious step toward battery swapping becoming an industry standard in China rather than one manufacturer's differentiator, and it converts Nio's most capital intensive asset into a shared utility. Nio shares are indicated sharply higher.

**Energy and healthcare.** TotalEnergies is raising fourth quarter buybacks to $2.5bn and lifting its dividend 5%. Eli Lilly won FDA approval for a once weekly insulin, cutting injections from seven a week to one and opening a new front against the incumbent basal insulin franchises. Mirum Pharmaceuticals hosts an investor call today with topline Phase 3 AZURE-1 data in chronic hepatitis delta, a day after winning approval for Atebrioz in the rare bone disorder FOP.

**Ratings.** Royal Caribbean was upgraded to Buy at Deutsche Bank on a 26% decline since August 5. Sweetgreen went to Overweight at Wells Fargo with the target raised from $6 to $11. Roblox was cut to Underperform at Jefferies after a 30% post-print rally. UiPath was cut to Underperform at DA Davidson following its investor day.

**Private markets.** Anthropic is reported to have settled on Nasdaq for a listing that could come as soon as October at a valuation up to $2 trillion, with a raise discussed as large as $100bn against a $965bn private mark from the May Series H. Sam Altman said in an interview published Saturday that an OpenAI IPO now would be ill-advised, which pushes that listing to 2027 at the earliest even as the company raises at $1.2 trillion. The gap between those two postures widened over a weekend in which one of the two companies paused its own training run.

## Asia and Europe

Seoul took the whole weekend's news in one session and it was ugly. The Kospi closed 6,889.74, down 191.18 points or 2.70% from its pre-holiday close of 7,080.92, opening 7,057.86, trading as high as 7,065.90 and as low as 6,896.80. It is the first close below 7,000 in four sessions. Samsung Electronics fell 5.43% to 270,000 won and SK Hynix 5.05% to 1,768,000 won, with Kioxia down more than 4% in Tokyo. Foreign investors sold a net 3.2403 trillion won of Kospi shares, a figure that tripled through the afternoon from just over one trillion at the midday mark.

This is the mirror image of what we flagged a week ago. On September 21 we noted that Seoul would not hold a gap that New York had paid for, and read it as Asia declining to validate an American chip rally with its own money. Today the causation runs the other way: Korea had two days of accumulated news to absorb at once, a ten year at a 2007 high, oil above $106 and the largest operator of agentic inference pausing it, and a market that is ninety percent a bet on memory and displays took all of it in a single print. A 2.7% down day on a three trillion won foreign outflow is a repricing, not a rotation, and it happens two days before Micron tells everyone whether the memory cycle is intact.

Tokyo closed 65,877.62, lower by 0.74% or roughly 485 points, ending a five session winning run, with the yen at 157.10.

Hong Kong was the only green market in Asia, closing 24,654.86 and higher by 0.66%, while Shanghai reopened after Mid-Autumn and fell 1.67% to 3,823.62. That 2.3 point divergence in a single session between offshore and onshore Chinese equity is not noise. Offshore money is positioned for Beijing to move and mainland money is positioned for Beijing to keep waiting, and the two have now disagreed for four consecutive sessions. The September NBS purchasing managers indices land Tuesday night with manufacturing expected at 50.1, the last official read before Golden Week closes the mainland from Thursday until October 8. Whatever that number says, it is the only policy input the market gets before China disappears for the PCE print, the ISM, Micron's guide and the September payrolls report.

Europe is holding up better than anywhere else, which in this environment means flat. The Euro Stoxx 50 is 6,321 and higher by 0.29%, the Stoxx 600 is around 642, the DAX is approximately 25,405 and unchanged, and the FTSE 100 is 10,722 and up 27 points. Banks are leading the rebound with UniCredit, Deutsche Bank and ING gaining between one and three percent, and the AI-exposed names are participating, with ASML, Infineon and Prosus up more than 1.5%. UBS is reported to be the target of multiple merger inquiries, which follows last week's reporting that it has revived discussions about moving out from under Swiss regulation after parliament bound roughly twenty billion dollars of capital. German consumer sentiment deteriorated more sharply than expected heading into October, with higher energy prices weighing on income expectations, which is the second consecutive month that survey has flagged the same mechanism.

## Space: Starship Reached Orbit and the Float Call Gets Its Answer

Starship Flight 14 lifted off from Starbase at 12:46 UTC, which is 8:46 Eastern, on the vehicle's first orbital attempt after thirteen intentionally suborbital flights. The flight profile so far has been clean. Max Q at T plus 58 seconds, booster engine cutoff at T plus 2:20, hot staging and separation at T plus 2:22, a boostback burn on 26 of 28 engines, a landing burn with 11 of 13 engines relit, and the orbital insertion burn completing successfully at T plus 25:28. Deployment of 26 Starlink V3 satellites, the first operational V3 units, was scheduled from T plus 34:18. The mission runs just under ten hours across roughly six orbits at about 275 kilometres, with a deorbit burn and a Pacific splashdown still ahead. Each V3 adds about 1 Tbps of capacity, so a full deployment adds 26 Tbps to the constellation in one flight.

We pre-committed on Friday and again on Saturday to marking our float call on this flight. The argument was that SpaceX fell about four percent into the September 23 unlock of roughly 328 million shares, and that a successful orbital mission five days later would be the cleanest available read on whether this complex is constrained by demand for the asset or by supply of paper. The hard part of the mission has been accomplished. We are marking this as working rather than proven, because the deorbit burn, reentry and splashdown are the parts that have historically failed, and we will close it tomorrow either way.

## Geopolitics

Day two hundred and twelve of the Iran war, and the negotiating track that looked substantive on Thursday is now formally dead without a counterproposal. Trump offered none. Reporting suggests he expects talks to resume this week anyway, and separately that he anticipates renewed bombing after the November midterms. Both of those can be true and neither is a policy.

The structure of the impasse has not changed and is worth restating because it explains why every headline moves crude four dollars and nothing moves the strait. Washington is being asked to move first on four items, funds, sanctions, the blockade and a regional ceasefire including Lebanon and Yemen, and to receive one item, Hormuz, on the seventh day, from a counterparty it does not trust and which says it does not trust Washington either. There is a political clock, because pump prices before a midterm are the most legible economic variable in American politics, and both sides now know there is one, which makes the clock a bargaining chip rather than a deadline.

On the Yemeni front, the Saudi-led coalition intercepted two ballistic missiles headed toward Khamis Mushait and two drones toward Riyadh early Saturday, following six ballistic missiles shot down on Thursday, and Saudi forces struck the area of Taiz in response. The Houthi naval blockade of Saudi shipping declared in July remains in force. A Hormuz reopening would remove one chokepoint and leave that one untouched.

On the Russian front the refinery campaign continues and Moscow's answer remains export restriction rather than repair. More than seventy Ukrainian drone attacks on Russian refining infrastructure have been recorded this year, the diesel export ban runs past September 30 into late October and the gasoline ban into January 2027, and Russian domestic petrol prices have set records twice. The two largest pools of marginal distillate available to the world remain withdrawn, one by drones and one by decree.

## Key Events Today and This Week

| When | What | Why It Matters |
|---|---|---|
| Mon, 8:46am ET | **Starship Flight 14** | Orbital insertion achieved; deploy and splashdown ahead |
| Mon, 10:30am | Dallas Fed manufacturing | Consensus 1.0, first regional read of the week |
| Mon, after close | Jefferies | First look at the quarter for capital markets |
| Tue, 10:00am | Consumer Confidence, JOLTS | Consensus 90.0 and 7.23m, after a 48.1 UMich |
| Tue, 9:30pm | China NBS PMIs | Manufacturing 50.1 expected, last read before the holiday |
| Wed, 8:30am | **August PCE and core PCE** | July ran 3.7% headline and 3.3% core; October at 65% to 73% |
| Wed, before open | **Jabil** | $13.6bn of AI revenue in fiscal 2026 |
| Wed, after close | **Micron** | $50bn at 86%; the November guide is the only line that matters |
| Thu, 10:00am | ISM Manufacturing | Consensus 54.8 after a 57.0 flash |
| Thu to Wed | China shut for Golden Week | Reopens October 8, after everything below |
| Thu, after close | Nike | The consumer, priced at 48.1 sentiment |
| Fri, 8:30am | **September payrolls** | Consensus 100k and 4.2%; claims at 197k removed the dovish objection |

The shape of the week is unchanged from Saturday and the stakes went up over the weekend. Wednesday carries the macro constraint at 8:30 and the physical constraint at 4:05, and China will be absent for both the ISM and payrolls.

## Accountability

**We had Friday's internals backwards and we are correcting it.** Saturday's note described Friday as three sectors advancing and eight declining, with communication services the worst performer at down 1.04%. The settled data shows eight of eleven sectors higher, communication services leading at up 1.3%, and materials and utilities the laggards. We characterised a broad session as a narrow one and built a paragraph on top of that characterisation. The conclusion we drew, that the index was being carried by a handful of very large names, was wrong for Friday specifically even if it has been right for the month. Corrected.

**The gold read was wrong within two sessions.** We wrote on Saturday that a 0.54% gold gain in a week when the long end made a 2004 high was a bid for something that is nobody's liability rather than a rates trade. This morning gold is down about three percent to a seven week low on a day when a war escalated, which is close to the strongest possible refutation. Gold was trading the real rate the whole time and we dressed it up as something more interesting. The correct framing, which we are adopting, is that with the thirty year at 5.53% and the October meeting better than two in three, the carry cost of holding a non-yielding asset has become the dominant term, and geopolitical headlines are a second order input to it.

**The capacity framing survives but needed an amendment on day one.** We published the capacity thesis on Saturday morning and by Saturday evening the largest operator of agentic inference had paused it voluntarily. The thesis is not refuted, since nothing about physical scarcity changed, but a framework that has to be extended forty eight hours after publication was not complete when we published it. We should have carried the governance dimension from the start, because the Amazon block on Muse on September 21 and the Transluce escalation research on September 23 were both on this desk's radar and both were filed as corporate colour rather than as constraints.

**The float call is working and closes tomorrow.** SpaceX fell about four percent into the September 23 unlock of roughly 328 million shares and Starship achieved orbital insertion five days later at T plus 25:28. We are marking this as working, not proven, until the deorbit burn and splashdown are complete, and we will close it in tomorrow's note whichever way it goes.

**The distillate thesis is losing on price for a second week and we are saying so plainly.** Retail diesel fell 4.1 cents to $6.449, its first weekly decline in this sequence, after the export ban was ruled out and the crack compressed. The mechanism we described is intact, the policy we called wrong was indeed abandoned, and the price has gone against us anyway. Two weeks of that is the point at which a thesis either produces a reason or gets smaller, and this morning's four percent move in WTI is a reason to wait one more week rather than to add.

**The crude discipline rule paid again.** We have carried no directional view on crude since September 23 on the grounds that a strait is the marginal input. Brent has gone $98.99, above $108, $104.32 and $108.42 inside eight sessions, entirely on diplomatic headlines. Having no view has been the correct view for three consecutive weeks, and we will keep it until the strait itself changes rather than the commentary about it.
