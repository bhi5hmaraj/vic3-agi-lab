# Design

This mod turns Victoria 3 plus the Cold War Era mod (CWE) into a lab for AI economics. You pick a scenario from the AI Futures Project (AI 2027 race, AI 2027 slowdown, AI 2040: Plan A). The mod then applies that scenario's AI shock to a running economy, on the scenario's timetable. Victoria 3 works out what happens next: pops lose jobs, wages and living standards move, radicals and interest groups react, and countries diverge. Compare that against a control run with no shock.

The goal is intuition, not prediction. What you learn here should be ported back into the Simulacra game engine, not treated as a forecast.

## How it works

```
game rules --> monthly clock --> scenario schedule --> agi_set_tier_N --> agi_tier_N modifier
 (scenario,     (month 0 =        (month, who,         (country)          (each sector: fewer workers, more output)
  start year)    shock start)      level 1-5)                           + agi_dividend_N modifier (income floor)
                                                                        + player event (what to watch)
```

- `common/game_rules/agi_game_rules.txt`: two game rules, the scenario (or none, for the control) and the year the shock starts.
- `common/on_actions/agi_on_actions.txt`: adds one monthly hook to the game's monthly pulse.
- `common/scripted_effects/agi_effects.txt`: the mechanism. It holds the clock, the tier and dividend effects, and the notifications.
- `common/scripted_effects/agi_scenarios.txt`: the data. There is one schedule per scenario, and each step is a month, a group of countries and a level.
- `common/scripted_triggers/agi_triggers.txt`: `agi_is_china` and `agi_is_rest_of_world`.
- `common/static_modifiers/agi_modifiers.txt`: the five tier modifiers (jobs and output per sector) and two income-floor modifiers.
- `common/modifier_type_definitions/agi_modifier_types.txt`: defines the four farm and ranch modifier types the base game lacks.
- `events/agi_events.txt` and `localization/english/agi_l_english.yml`: the plain-language reports for players.
- `common/defines/zz_agi_defines.txt`: moves CWE's end date from 2092 to 2200, so long runs never stop.
- `tools/lint.py`: static checks, since the game can't run in CI.

Mechanism and data are kept apart on purpose. A new scenario needs six things. It needs one schedule effect in `agi_scenarios.txt`, ending with `agi_end_scenario`, and one game rule option. It needs one branch each in `agi_scenario_tick` and `agi_notify_players` (`agi_effects.txt`). And it needs one briefing event and four localisation lines. `docs/extending.md` will replace this with a data file per scenario.

## Decisions

Each decision lists the options considered and why the current one won.

### 1. Why a Victoria 3 mod at all

| Option | Verdict |
|---|---|
| Build the economy in Simulacra only | Rejected for now. Simulacra has no labour market, pops or politics yet, and building them is the expensive part. |
| EU4 plus the Extended Timeline mod | Rejected. EU4 has no pops, labour or production functions, so an AI shock has nothing to spread through. Every effect would have to be scripted, which only replays our own assumptions. |
| Stellaris | Rejected. It has good mechanics for regime shifts ("situations"), but no model of national economies. |
| **Victoria 3** | **Chosen.** The economy is simulated: jobs, wages, standard of living, radicals and interest groups respond by themselves. |

The main risk is the "mirror problem": a lab that only echoes what you put in. Victoria 3's economy and politics react on their own. Its diplomacy does not. So read results for what the economy did, and discount anything that hinges on AI diplomacy.

### 2. Base mod: Cold War Era

| Option | Tech after 2000 | AI / automation already modelled | Status (Sep 2026) | Verdict |
|---|---|---|---|---|
| Vanilla | none (ends 1936) | no | stable | too early, no modern economy |
| Tech & Res | about 29 techs, ends 2036 | datacenters, data economy | active, 1.13 | 1836 start; runs out by 2036 |
| UNIPOLAR (1992 start) | vanilla eras 1-5, compressed | AI service production methods (e.g. clerks -2835) | Steam build broken on 1.13.10+ | best realism, but broken and runs out of tech |
| New Millennium / vic3-modern-2000 | vanilla | none | stale / not playable | the only 2000 starts, and neither works |
| **CWE (1950 start)** | **about 130 techs in eras 6-10 (labelled 2000-2099)** | **automation production methods, tiers 0-10, each cutting jobs for a specific pop type** | **active; the 1.13 build is pinned** | **chosen** |

CWE gives the lab a modern economy to shock: a large service sector split into basic, middle and advanced services, modern industry, welfare laws and a 1950 world. Its weaknesses are an early-stage mod, frequent patch churn and a 1950 start.

v0.1 also leaned on CWE's automation production methods for the job cuts. The review showed that was a mistake (see decision 4).

### 3. Time: a relative clock, not a start year

| Option | Cost | Verdict |
|---|---|---|
| Run observe mode 1950-2000, save, and start there | 2.5-5 h per run; alternate-history world | rejected: the calendar doesn't matter to the economics |
| Write a true 2000 start date | weeks (hundreds of history files) | rejected |
| Console `date 2000.1.1` | free, but CWE's date-windowed events never fire | rejected |
| **Scenario clock: month 0 = the shock start** | **none** | **chosen** |

The automation dynamics don't depend on the calendar. So each scenario's January 2026 is mapped to a start year you choose (1955, 1970 or 1985), and the schedule counts months from there.

The shock itself works at any start year, because it needs no technology (decision 4). What changes with the start year is the economy being shocked. In 1955 most people work on farms and in factories, so the first, office-only AI level moves less. By 1985 the service sector is larger and the result is closer to today's. That is why the start year is a game rule and not a constant.

### 4. How the shock enters the economy

| Option | Verdict |
|---|---|
| `add_era_researched` (whole eras) | Rejected. It also grants every military and society tech, so the shock would be contaminated. |
| Grant CWE's electronics, services and manufacturing techs so its automation production methods cut the jobs (v0.1) | Rejected after review. See below. |
| New tier-11 production methods injected into CWE's automation groups | Rejected for the same reasons as the tech grants. |
| **One modifier per level: each sector needs fewer workers and produces more** | **Chosen.** |

A level is one `agi_tier_N` modifier. For each sector it sets `building_group_<group>_employee_mult` (fewer workers per building) and `building_group_<group>_throughput_add` (more output). CWE pairs the same two keys in its own `oil_industry_concessions` modifier, so the pattern is known to work on this engine.

A building-group modifier only exists once its type is defined. The base game defines the two keys for services, manufacturing and mining. It does not define them for staple crops or livestock ranches, so this mod does, the way CWE defines one for urban centres.

Sectors move in the order the scenarios describe. Services (knowledge work) go first. Factories follow from level 2. Staple-crop farms, ranches and mines follow from level 4, when robots arrive. Subsistence farms are left out, because that is where the jobless end up: in CWE a displaced worker usually becomes a Peasant there.

v0.1 granted CWE's techs instead. An adversarial review found that this would not work:

- **Catch-up, not AI.** Level 1 granted tier 6 (CWE's 2000-2019 era) to a 1955 country at tier 2. The first step measured 60 years of ordinary automation, given to two countries only.
- **Stalled automation.** The higher automation methods need software and computers as inputs. In 1955 nothing makes them, so the AI would not switch.
- **Half the jobs untouched.** Half of each factory's jobs, and all farm and mine jobs, are set by a second production-method group gated by a tech we did not grant.
- **Confounds.** The same techs double bureaucracy and tax capacity, unlock new industries, and trigger a CWE oil discovery for each tech a player gains.
- **Players left out.** Only AI countries switch production methods by themselves, so the player's own economy never automated.

The modifier has none of these problems. It is pure AI delta at any start year, it applies to player and AI countries alike, and the control run differs by exactly the modifier.

The cost is detail. CWE's automation cuts specific jobs (machinists, clerks, engineers). The modifier cuts every job in a sector by the same share. Sector-level detail is enough for the questions this lab asks.

### 5. One dial per country, not two

Earlier designs had a "lab level" (who leads the frontier) and a "deploy level" (what the economy uses). Only deployment moves an economy, so there is one dial, the deployment level (0-5). The frontier race is described in the event text instead.

The level names describe deployment, not capability: AI Assistants, AI Remote Workers, AI-Majority Knowledge Work, AI and Robots, AI-Run Economy. A capability name such as "superhuman coder" fits AI 2027 but contradicts AI 2040, which holds AI below top-expert level until 2035.

Add a second dial only if a scenario needs frontier capability to change economics directly.

### 6. How scenarios are encoded

| Option | Works in observe mode | Newcomer-friendly | Verdict |
|---|---|---|---|
| Console commands per step | yes | no | v0 testing only |
| Journal entry buttons | no (needs a played country) | yes | v2 "policymaker" panel |
| Dated events | yes | yes | brittle when the start year varies |
| **Game rules plus a monthly clock** | **yes** | **yes** | **chosen** |

With game rules, a newcomer never touches the console, and the control run is the same game with the scenario set to "none".

Steps use `month >= M` and levels only ever go up. So a step re-running every month is a no-op, a missed month still applies, and loading a save mid-scenario is safe. The schedule keeps running after the scenario ends, so a country CWE creates later still gets its group's final level.

Countries are grouped into the US, China and everyone else. Everyone else is every country that is not decentralised, so CWE's unrecognised countries are included. China is matched by either tag, PRC or CHI, because CWE can change one into the other. The scenarios are US-China stories, and everyone else follows with a lag.

### 7. Newcomer layer

| Option | Verdict |
|---|---|
| A full lab panel (journal entry with levers and meters) | v2. It needs a played country, and most of its content should wait until v1 shows which numbers matter. |
| **Events at each milestone that say what to watch, plus a README reading guide** | **Chosen.** |
| Observe only | Allowed, but observers see no events. Read the `agi_tier_N` modifier on the USA and China instead. |

Newcomers only need to read five things: Employment, Standard of Living, Radicals, Interest Groups and GDP. The events point to them.

### 8. Calibration: timing from AI 2027, magnitudes from AI 2040

AI 2027 is precise about timing and almost silent on economics. Its only labour figures are that by October 2027 AI does 25% of 2024's remote jobs and unemployment is up 1 point.

AI 2040: Plan A publishes a per-year dashboard. US employment goes 62% (2029), 32% (2035), 12% (2040). Median income goes $47K (2027), about $1.1M (2035), about $13M (2040). GDP grows about 50% in 2032.

The tier and income-floor values are knobs, not sourced numbers. Tune them until the Victoria 3 run matches the *shape* of those curves: direction and ordering. Don't aim for the absolute values. The engine won't reproduce a 99% income-per-capita jump, and trying would break it.

### 9. Verifying without the game

Victoria 3 can't run in CI, so the repo checks what it can statically:
- `tools/lint.py` checks balanced braces, and that every scripted effect, modifier, event and game-rule option is defined. It also checks every localisation key, the UTF-8 byte-order mark the engine requires, and that no job cut goes below the -0.8 floor. It checks that every modifier key has a defined type, against a short list verified in the base game plus the types this mod defines. With `--cwe PATH`, it checks that every building group a modifier names exists in CWE.
- Every engine construct used here was copied from a pattern CWE itself uses in the same scope.
- Two adversarial reviews checked engine semantics, fidelity to the scenarios, economic logic and the docs. A skeptic tried to refute each finding. `CHANGELOG.md` lists what changed.
- The in-game checks that remain are listed in the README under "First evening".

### 10. Pinning

Game 1.13.11 plus CWE commit `fd5cb37909` (2026-08-30, the last 1.13 build). CWE master now targets the 1.14 beta, and patch 1.15 ships on 2026-10-22. Keep a local copy of CWE and unsubscribe from the Workshop item, so an auto-update can't change the base under your saves.

### 11. Out of scope for now

- Cuts by job type inside a sector (see decision 4).
- Government jobs. No level cuts bureaucrats.
- Plantations, logging and fishing. Level 4 and 5 cover staple crops, livestock ranches and mines only.
- CWE's infrastructure: power plants, railways, ports, communications, construction and real estate. It is neither automated nor boosted, and it feeds the boosted sectors, so its goods may run short at levels 4-5.
- Funding for the income floor. Each country pays its own from its budget.
- The policymaker panel and a UBI law with interest-group reactions.
- AI 2040's other plans (B, C, D). Its Plans C and D map onto AI 2027's endings anyway.
- AI 2027's race ending after January 2030. The takeover and extinction are outside what an economic model can say anything about, so the scenario stops there.
- Shipping the AI Futures Project's text or data. The repo links to the sources and paraphrases them.
