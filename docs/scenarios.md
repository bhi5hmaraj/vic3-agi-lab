# Scenarios

Each scenario is a schedule of steps in `common/scripted_effects/agi_scenarios.txt`. A step says: from scenario month M, this group of countries is at AI level L. Month 0 is January 2026 in the source, mapped to the shock start year you pick in the game rules.

"S" means the source states it. "I" means it is our reading, needed to turn a story into a schedule. The sources are summarised in our own words, so read them for the full text.

## AI deployment levels

| Level | Meaning | CWE techs granted | Output modifier (throughput) |
|---|---|---|---|
| 1 | unreliable AI agents | electronics, services, manufacturing tiers 1-6 | +5% services and manufacturing |
| 2 | cheap AI remote workers | tiers 1-7 | +15% |
| 3 | superhuman coders and researchers | tiers 1-8 | +35% |
| 4 | top-expert AI plus robots | tiers 1-9 | +75%, and +25% agriculture and mining |
| 5 | superintelligence economy | tiers 1-10 | +150%, and +75% agriculture and mining |

The throughput numbers are knobs to calibrate (see the bottom of this page), not sourced figures.

## AI 2027: race ending

Source: [ai-2027.com](https://ai-2027.com), race ending. AI Futures Project, 2025.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0 | Jan 2026 | US and PRC to level 1 | S: Agent-1 released early 2026, agents at the leading labs |
| 18 | Jul 2027 | US to level 2 | S: Agent-3-mini released to the public as a cheap remote worker |
| 20 | Sep 2027 | PRC to level 2 | I: China is about 2 months behind in capability, so we assume the same lag for deployment |
| 24 | Jan 2028 | rest of world to level 2 | I: public release spreads with a lag |
| 30 | Jul 2028 | US to level 5, PRC to level 4 | S: Agent-5 released publicly mid-2028, with special economic zones and a robot build-out. China's level is I |
| 36 | Jan 2029 | rest of world to level 3 | I |
| 42 | Jul 2029 | scenario ends | We stop here. The source's mid-2030 ending (human extinction) is outside what an economic model can say anything about |

## AI 2027: slowdown ending

Source: [ai-2027.com/slowdown](https://ai-2027.com/slowdown). This is the same as the race until the October 2027 branch point, when the Oversight Committee votes 6-4 to slow down.

| Month | Source date | Step | Basis |
|---|---|---|---|
| 0-24 | Jan 2026 - Jan 2028 | as in the race | S/I as above |
| 28 | May 2028 | US to level 5 | S: superhuman AI released to the public |
| 30 | Jul 2028 | PRC to level 4 | S: the US-China deal (Consensus-1 and a chip swap). The level is I |
| 36 | Jan 2029 | rest of world to level 4 | I: transformation under a US-led order |
| 48 | Jan 2030 | PRC and rest of world to level 5 | I |
| 60 | Jan 2031 | scenario ends | |

## AI 2040: Plan A

Source: [ai-2040.com](https://ai-2040.com), with the [announcement](https://blog.aifutures.org/p/ai-2040-plan-a) of 9 July 2026. It is a recommendation for what should happen, not a prediction.

In the scenario, a 2029 US-China deal pauses training, declares and verifies compute, and makes research transparent. From 2032 it caps compute and robots with cap-and-trade. It holds AI at top-expert level from 2035 and reaches superintelligence in 2040 instead of about 2030. The deal is global (the "Consortium"), so the rest of the world moves with the leaders (I).

| Month | Source date | Step | Basis |
|---|---|---|---|
| 12 | 2027 | US and PRC to level 1 | S: millions of AI agents in the US economy |
| 24 | 2028 | rest of world to level 1 | I |
| 36-59 | 2029-2030 | no change | S: training pause and verification |
| 60 | 2031 | all to level 2 | S: first regulated models released. AI does a third of cognitive labour |
| 72 | 2032 | all to level 3, plus the dividend | S: GDP up about 50%, cap-and-trade on compute and robots, the dividend and foreign aid begin |
| 108 | 2035 | all to level 4, plus a larger dividend | S: pause at top-expert AI. AI and robots do about 85% of value-weighted labour. The dividend is about $1M |
| 168 | 2040 | all to level 5 | S: scaling to superintelligence resumes |
| 180 | 2041 | scenario ends | |

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
- employment falls more under the race than under Plan A, and falls late under Plan A;
- income per head rises with the dividend;
- the US-China gap widens more in the race than in the slowdown or Plan A;
- the control run (scenario "none") shows none of it.

Tune the throughput values in `common/static_modifiers/agi_modifiers.txt` until those orderings hold across a few seeds.
