# Scenarios

Each scenario is a schedule of steps in `common/scripted_effects/agi_scenarios.txt`. A step says: from scenario month M, this group of countries is at AI level L. Month 0 is January 2026 in the source, mapped to the shock start year you pick in the game rules.

"S" means the source states it. "I" means it is our reading, needed to turn a story into a schedule. The sources are summarised in our own words, so read them for the full text.

## AI deployment levels

A level says how much of the work AI does, not how capable the AI is. Each level changes how many workers a sector needs and how much it produces.

| Level | Name | Services | Factories | Farms and ranches | Mines |
|---|---|---|---|---|---|
| 1 | AI Assistants | -5% jobs, +5% output | | | |
| 2 | AI Remote Workers | -15%, +15% | -5%, +5% | | |
| 3 | AI-Majority Knowledge Work | -30%, +30% | -15%, +15% | | |
| 4 | AI and Robots | -55%, +60% | -45%, +60% | -25%, +25% | -25%, +25% |
| 5 | AI-Run Economy | -75%, +120% | -70%, +120% | -50%, +60% | -40%, +60% |

Every number is a knob to calibrate (see the bottom of this page), not a sourced figure.

An AI dividend adds income support: welfare payments of 0.25 and +1 standard of living at level 1, then 0.5 and +2 at level 2.

## AI 2027: race ending

Source: [ai-2027.com](https://ai-2027.com), race ending. AI Futures Project, 2025.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0 | Jan 2026 | US and China to level 1 | S: Agent-1 era agents at the leading labs |
| 18 | Jul 2027 | US to level 2 | S: Agent-3-mini released to the public as a cheap remote worker |
| 20 | Sep 2027 | China to level 2 | S: China is about 2 months behind. Same lag for deployment is I |
| 23 | Dec 2027 | US to level 3 | S: AI-designed software spreads through US business and GDP balloons |
| 24 | Jan 2028 | rest of world to level 2 | I: public release spreads with a lag |
| 30 | Jul 2028 | US to level 4, China to level 3 | S: Agent-5 released publicly, special economic zones, a robot build-out. China's level is I |
| 36 | Jan 2029 | US to level 5, China to level 4, both get a dividend | S: a universal basic income in 2029. The month and the levels are I |
| 45 | Oct 2029 | rest of world to level 3 | S: special economic zones spread around the world by late 2029 |
| 48 | Jan 2030 | scenario ends | We stop before the source's early-2030 takeover and mid-2030 extinction. An economic model has nothing to say about them |

## AI 2027: slowdown ending

Source: [ai-2027.com/slowdown](https://ai-2027.com/slowdown). This is the same as the race until the October 2027 branch point, when the Oversight Committee votes 6-4 to slow down.

The name is about AI research. In the source, the economy changes as fast as in the race, and the change spreads further.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0-24 | Jan 2026 - Jan 2028 | as in the race, without the Dec 2027 step | S/I as above |
| 28 | May 2028 | US and China to level 4 | S: superhuman AI released to the public. Special economic zones run on both sides of the Pacific |
| 29 | Jun 2028 | rest of world to level 3 | S: factories around the world run round the clock. The level is I |
| 36 | Jan 2029 | US to level 5, rest of world to level 4, everyone gets a dividend | S: robots commonplace. A basic income and foreign aid end poverty, even in developing countries |
| 48 | Jan 2030 | everyone to level 5 | I |
| 60 | Jan 2031 | scenario ends | |

## AI 2040: Plan A

Source: [ai-2040.com](https://ai-2040.com), with the [announcement](https://blog.aifutures.org/p/ai-2040-plan-a) of 9 July 2026. It is a recommendation for what should happen, not a prediction.

In the scenario, a 2029 US-China deal pauses training, declares and verifies compute, and makes research transparent. From 2032 it caps robot and compute growth with cap-and-trade. It holds AI at top-expert level from 2035. Scaling to superintelligence resumes in 2040 instead of about 2030.

The site's per-bloc data puts China about two years behind the US in AI labour, and the rest of the world about three. Each step below applies to the US on its date. China follows 24 months later and the rest of the world 36 months later (I).

| Month | Source date | Step (US) | Basis |
|---|---|---|---|
| 12 | 2027 | level 1. China on the same date, rest of world at month 24 | S: millions of AI agents in the US economy |
| 36-59 | 2029-2030 | no change | S: training pause and verification |
| 60 | 2031 | level 2 | S: first regulated models. AI does a third of US cognitive labour |
| 72 | 2032 | level 3, dividend | S: US GDP up about 50%, cap-and-trade on robots and compute, a $45K citizen's dividend |
| 108 | 2035 | level 4, large dividend | S: pause at top-expert AI. AI and robots do about 85% of US labour. The dividend is about $1M |
| 120 | 2036 | level 5 | S: top-expert AI at full scale, 2 billion robots, a quarter of Americans employed |
| 180 | 2041 | scenario ends | |

Dividends: China gets the same dividend on the same dates as the US (I: the source says China has its own boom). The rest of the world gets the smaller dividend from 2035, when foreign aid reaches about $10K per adult (S). The 2032 aid of about $1.2K per adult is too small to model.

Level 5 is not superintelligence here. In the source, 2040 tightens the caps on Earth, and superintelligence arrives only at the end of that year.

## Calibration targets

AI 2027 is precise about timing and almost silent on economics. By October 2027 (month 21), AI does 25% of 2024's remote jobs and unemployment is up 1 point. That is all it gives.

AI 2040 publishes a per-year dashboard:

| Year | US employment rate | Median income (real 2025 $) |
|---|---|---|
| 2029 | 62% | $50K |
| 2032 | 62% | $104K |
| 2035 | 32% | $1.1M |
| 2040 | 12% | $13M |

Victoria 3 will not reproduce these values. Calibrate the shape instead:
- employment barely moves at levels 1-3 and falls steeply at levels 4-5;
- the US-China gap widens more in the race than in the slowdown or Plan A;
- radicals rise less where a dividend is paid;
- the control run (scenario "none") shows none of it.

Tune the values in `common/static_modifiers/agi_modifiers.txt` until those orderings hold across a few runs.
