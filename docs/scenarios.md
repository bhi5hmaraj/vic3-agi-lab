# Scenarios

Each scenario is a schedule of steps in `common/scripted_effects/agi_scenarios.txt`. A step says: from scenario month M, this group of countries is at AI level L. Month 0 is January 2026 in the source, mapped to the shock start year you pick in the game rules.

"S" means the source states it. "I" means it is our reading, needed to turn a story into a schedule. The sources are summarised in our own words, so read them for the full text.

## AI deployment levels

A level says how much of the work AI does, not how capable the AI is. Each level changes how many workers a sector needs and how much it produces.

| Level | Name | Services | Factories | Staple farms and ranches | Mines |
|---|---|---|---|---|---|
| 1 | AI Assistants | -5% jobs, +5% output | | | |
| 2 | AI Remote Workers | -15%, +15% | -5%, +5% | | |
| 3 | AI-Majority Knowledge Work | -35%, +35% | -15%, +15% | | |
| 4 | AI and Robots | -55%, +60% | -45%, +60% | -25%, +25% | -25%, +25% |
| 5 | AI-Run Economy | -75%, +120% | -70%, +120% | -50%, +60% | -40%, +60% |

Every number is a knob to calibrate (see the bottom of this page), not a sourced figure.

The output figures are throughput, so a sector's inputs rise by the same share. They add to a building's existing throughput bonuses, so the relative gain is smaller than the figure.

Level 4 is the robot level. A step earns it only when the source has robots doing the work, not when it has factories hiring people to build them.

## Income floor

Some steps add an income floor. It stands in for the scenarios' basic income, citizen's dividend and foreign aid.

| Floor | Welfare payments | Standard of living |
|---|---|---|
| 1 | pops earning under 25% of the normal wage are topped up | +1 |
| 2 | pops earning under 50% of the normal wage are topped up | +2 |

This is a wage floor, not a universal payment. Each country's own budget pays it. The sources fund it from AI permit fees, taxes on AI companies and donor aid, and none of that is modelled. So the rest of the world's "aid" is paid by the recipient.

## AI 2027: race ending

Source: [ai-2027.com](https://ai-2027.com), race ending. AI Futures Project, 2025.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0 | Jan 2026 | US and China to level 1 | S: Agent-1 is released to the public in early 2026. China on the same date is I |
| 12 | Jan 2027 | rest of world to level 1 | I: the cheap agents are public releases |
| 18 | Jul 2027 | US to level 2 | S: Agent-3-mini released to the public as a cheap remote worker |
| 20 | Sep 2027 | China to level 2 | S: China is about 2 months behind. The same lag for deployment is I |
| 23 | Dec 2027 | US to level 3 | S: AI-designed software spreads through US business and GDP balloons. The level is I |
| 24 | Jan 2028 | rest of world to level 2 | I: public release spreads with a six-month lag |
| 30 | Jul 2028 | China to level 3 | S: Agent-5 released publicly. Both powers open special economic zones, staffed by people. China's level is I |
| 36 | Jan 2029 | US and China to level 4 and floor 1, rest of world to level 3 | S: a million robots a month by the end of 2028, and a basic income in 2029. Paying the US and China first is I. Rest of world is I: the same six-month lag |
| 45 | Oct 2029 | US to level 5, rest of world to level 4 and floor 1 | S: by late 2029 people are no longer needed, zones full of robots spread around the world, and the basic income is described for people in general. The levels are I |
| 48 | Jan 2030 | scenario ends | We stop before the source's early-2030 takeover and mid-2030 extinction. An economic model has nothing to say about them |

China ends one level behind the US.

## AI 2027: slowdown ending

Source: [ai-2027.com/slowdown](https://ai-2027.com/slowdown). This is the same as the race until the October 2027 branch point, when the Oversight Committee votes 6-4 to slow down.

The name is about AI research. Our reading (I) is that the economy changes about as fast as in the race, and the change spreads further.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0-24 | Jan 2026 - Jan 2028 | as in the race, without the Dec 2027 step | S/I as above |
| 28 | May 2028 | US and China to level 3 | S: superhuman AI released to the public. The special economic zones run on human workers, and robots are still few |
| 36 | Jan 2029 | US and China to level 4, rest of world to level 3, everyone gets floor 1 | S: robots commonplace. A basic income and foreign aid end poverty, even in developing countries. Rest of world's level is I |
| 48 | Jan 2030 | US and China to level 5, rest of world to level 4 | I: in 2029 the source still puts an AI-run economy a few years away |
| 60 | Jan 2031 | scenario ends | |

## AI 2040: Plan A

Source: [ai-2040.com](https://ai-2040.com), with the [announcement](https://blog.aifutures.org/p/ai-2040-plan-a) of 9 July 2026. It is a recommendation for what should happen, not a prediction.

In the scenario, a 2029 US-China deal pauses training, declares and verifies compute, and makes research transparent. From 2032 it caps robot and compute growth with cap-and-trade. It holds AI at top-expert level from 2035. Scaling to superintelligence resumes during 2040 instead of about 2030.

The site's per-bloc data puts China about two years behind the US in AI cognitive labour, and the rest of the world about three. In robot labour the same data has China close to the US. So levels 2, 3 and 5 reach China 24 months after the US, and level 4 (robots) reaches it 12 months after. The rest of the world follows 36 months after the US (I).

| Month | Source date | Step (US) | Basis |
|---|---|---|---|
| 12 | 2027 | level 1 | S: millions of AI agents in the US economy. China on the same date and the rest of the world at month 24 are I, and are exceptions to the lag rule |
| 36-59 | 2029-2030 | no change | S: training pauses while verification is built. AI use keeps spreading, but employment stays at 62-61%, so no step (I) |
| 60 | 2031 | level 2 | S: first regulated models. AI does a third of cognitive labour by mid-2031 |
| 72 | 2032 | level 3, floor 1 | S: US GDP up about 50%, cap-and-trade on robots and compute, a $45K citizen's dividend. The month is I |
| 108 | 2035 | level 4, floor 2 | S: pause at top-expert AI. AI and robots do about 85% of US labour. The dividend is about $1M |
| 120 | 2036 | level 5 | S: top-expert AI at full scale, 2 billion robots, a quarter of Americans employed |
| 180 | 2041 | scenario ends | |

China reaches level 2 at month 84, level 3 at 96, level 4 at 120 and level 5 at 144. The rest of the world reaches level 2 at month 96, level 3 at 108, level 4 at 144 and level 5 at 156.

Income floors: China gets the same floor on the same dates as the US (I: the source says China has its own boom). The rest of the world gets floor 1 from 2035, when foreign aid reaches about $10K per adult (S). It gets floor 2 from 2039, when even the poorest people outside the US receive about $1M (S). The 2032 aid of about $1.2K per adult is too small to model.

Level 5 is not superintelligence here. In the source, 2040 tightens the caps on Earth, and scaling to superintelligence only resumes during that year.

## Calibration targets

AI 2027 is precise about timing and almost silent on economics. By October 2027 (month 21), AI does 25% of 2024's remote jobs and unemployment is up 1 point. That is all it gives.

AI 2040 publishes a per-year dashboard:

| Year | US employment rate | Median income (real 2025 $) |
|---|---|---|
| 2029 | 62% | $50K |
| 2032 | 62% | $104K |
| 2033 | 52% | $193K |
| 2034 | 44% | $429K |
| 2035 | 32% | $1.1M |
| 2040 | 12% | $13M |

Victoria 3 will not reproduce these values. Calibrate the shape instead:
- gainful employment (working adults who are neither Peasants nor Unemployed) barely moves at levels 1-2, has lost about a third of its total fall by the end of level 3, and falls steeply at levels 4-5;
- radicals rise less where an income floor is paid;
- the control run (scenario "none") shows none of it.

Tune the values in `common/static_modifiers/agi_modifiers.txt` until the first two orderings hold across a few runs. The third is a sanity check.

The schedules, not the knobs, set who leads. The US-China gap is widest in Plan A: two levels in months 72-83. Only the race ends with the gap still open, at level 5 against 4.
