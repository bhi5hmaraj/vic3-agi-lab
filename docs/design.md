# Design

This mod turns Victoria 3 plus the Cold War Era mod (CWE) into a lab for AI economics. You pick a scenario from the AI Futures Project (AI 2027 race, AI 2027 slowdown, AI 2040: Plan A). The mod then applies that scenario's AI shock to a running economy, on the scenario's timetable. Victoria 3 works out what happens next: pops lose jobs, wages and living standards move, radicals and interest groups react, and countries diverge. Compare that against a control run with no shock.

The goal is intuition, not prediction. What you learn here should be ported back into the Simulacra game engine, not treated as a forecast.

## How it works

```
game rules --> monthly clock --> scenario schedule --> agi_set_tier_N --> CWE techs (automation cuts jobs)
 (scenario,     (month 0 =        (month, who,         (country)        + agi_tier_N modifier (output up)
  start year)    shock start)      level 1-5)                           + player event (what to watch)
```

- `common/game_rules/agi_game_rules.txt`: two game rules, the scenario (or none, for the control) and the year the shock starts.
- `common/on_actions/agi_on_actions.txt`: adds one monthly hook to the game's monthly pulse.
- `common/scripted_effects/agi_effects.txt`: the mechanism. It holds the clock, the tier effects, the tech grants and the notifications.
- `common/scripted_effects/agi_scenarios.txt`: the data. There is one schedule per scenario, and each step is a month, a group of countries and a level.
- `common/scripted_triggers/agi_triggers.txt`: `agi_is_rest_of_world`.
- `common/static_modifiers/agi_modifiers.txt`: the five tier modifiers (output) and two dividend modifiers.
- `events/agi_events.txt` and `localization/english/agi_l_english.yml`: the plain-language reports for players.
- `common/defines/zz_agi_defines.txt`: moves CWE's end date from 2092 to 2200, so long runs never stop.
- `tools/lint.py`: static checks, since the game can't run in CI.

Mechanism and data are kept apart on purpose. A new scenario means one new effect in `agi_scenarios.txt`, one game rule option and three localisation lines.

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

CWE already models the half of the AI shock that is hardest to build: which jobs disappear, for which pop types, at which tech tier. Its weaknesses are an early-stage mod, frequent patch churn and a 1950 start.

### 3. Time: a relative clock, not a start year

| Option | Cost | Verdict |
|---|---|---|
| Run observe mode 1950-2000, save, and start there | 2.5-5 h per run; alternate-history world | rejected: the calendar doesn't matter to the economics |
| Write a true 2000 start date | weeks (hundreds of history files) | rejected |
| Console `date 2000.1.1` | free, but CWE's date-windowed events never fire | rejected |
| **Scenario clock: month 0 = the shock start** | **none** | **chosen** |

The automation dynamics don't depend on the calendar. So each scenario's January 2026 is mapped to a start year you choose (1955, 1970 or 1985), and the schedule counts months from there.

The one real constraint is that the economy must be able to build computers, robots and software. A 1955 economy may not be able to switch to automation production methods yet.

The throughput modifier still applies either way. If automation doesn't take hold, use a later start. That's why the start year is a game rule and not a constant.

### 4. How the shock enters the economy

| Option | Verdict |
|---|---|
| `add_era_researched` (whole eras) | Rejected. It also grants every military and society tech, many of which have real modifiers, so the shock would be contaminated. |
| New tier-11 production methods injected into CWE's automation groups | Deferred to v2. It adds input-balancing work before we know it's needed. |
| Pure modifiers (output up, jobs down) | Rejected as the only lever. It throws away CWE's job cuts by pop type, which are the most valuable part. |
| **Targeted tech grants plus an output modifier** | **Chosen.** |

Level N grants CWE's `tech_electronics`, `tech_services` and `tech_manufacturing` up to tier 5+N. That unlocks CWE's own automation, which is where the job cuts come from. The `agi_tier_N` modifier adds output throughput to service and manufacturing buildings, plus agriculture and mining at levels 4-5 for robots. That is the half CWE lacks: in CWE, automation cuts jobs but never raises output per building.

Tech grants always include every lower tier. That avoids any question of whether a tech needs its prerequisites.

### 5. One dial per country, not two

Earlier designs had a "lab level" (who leads the frontier) and a "deploy level" (what the economy uses). Only deployment moves an economy, so v1 keeps one dial, the deployment level (0-5). The frontier race is described in the event text instead. Add a second dial only if a scenario needs frontier capability to change economics directly.

### 6. How scenarios are encoded

| Option | Works in observe mode | Newcomer-friendly | Verdict |
|---|---|---|---|
| Console commands per step | yes | no | v0 testing only |
| Journal entry buttons | no (needs a played country) | yes | v2 "policymaker" panel |
| Dated events | yes | yes | brittle when the start year varies |
| **Game rules plus a monthly clock** | **yes** | **yes** | **chosen** |

With game rules, a newcomer never touches the console, and the control run is the same game with the scenario set to "none".

Steps use `month >= M` and levels only ever go up. So a step re-running every month is a no-op, a missed month still applies, and loading a save mid-scenario is safe.

Countries are grouped into the US, the PRC and everyone else (recognised countries only). The scenarios are US-China stories, and everyone else follows with a lag.

### 7. Newcomer layer

| Option | Verdict |
|---|---|
| A full lab panel (journal entry with levers and meters) | v2. It needs a played country, and most of its content should wait until v1 shows which numbers matter. |
| **Events at each milestone that say what to watch, plus a README reading guide** | **Chosen.** |
| Observe only | Allowed, but observers see no events. The README says to play a country and let time run. |

Newcomers only need to read five things: Employment, Standard of Living, Radicals, Interest Groups and GDP. The events point to them.

### 8. Calibration: timing from AI 2027, magnitudes from AI 2040

AI 2027 is precise about timing and almost silent on economics. Its only labour figures are that by October 2027 AI does 25% of 2024's remote jobs and unemployment is up 1 point.

AI 2040: Plan A publishes a per-year dashboard. US employment goes 62% (2029), 32% (2035), 12% (2040). Median income goes $47K (2027), about $1.1M (2035), about $13M (2040). GDP grows about 50% in 2032.

The tier modifier values are knobs, not sourced numbers. Tune them until the Victoria 3 run matches the *shape* of those curves: direction and ordering. Don't aim for the absolute values. The engine won't reproduce a 99% income-per-capita jump, and trying would break it.

### 9. Verifying without the game

Victoria 3 can't run in CI, so the repo checks what it can statically:
- `tools/lint.py` checks balanced braces, and that every scripted effect, modifier, event and game-rule option is defined. It also checks every localisation key and the UTF-8 byte-order mark the engine requires. With `--cwe PATH`, it checks that every granted tech exists in CWE.
- Every engine construct used here was copied from a pattern CWE itself uses in the same scope.
- An adversarial review checked engine semantics, fidelity to the scenarios, and economic logic (see `scenarios.md` and the changelog).
- The in-game checks that remain are listed in the README under "First evening".

### 10. Pinning

Game 1.13.11 plus CWE commit `fd5cb37909` (2026-08-30, the last 1.13 build). CWE master now targets the 1.14 beta, and patch 1.15 ships on 2026-10-22. Keep a local copy of CWE and unsubscribe from the Workshop item, so an auto-update can't change the base under your saves.

### 11. Out of scope for v1

- Tier-11 automation production methods (see decision 4).
- The policymaker panel and a UBI law with interest-group reactions.
- Automating agriculture, mining and government jobs. CWE has these production methods commented out, so v1 only adds output to those sectors.
- AI 2040's other plans (B, C, D). Its Plans C and D map onto AI 2027's endings anyway.
- AI 2027's race ending after mid-2029. Human extinction is outside what an economic model can say anything about, so the scenario stops there.
- Shipping the AI Futures Project's text or data. The repo links to the sources and paraphrases them.
