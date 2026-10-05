# AGI Lab for Victoria 3

A Victoria 3 mod for exploring AI economics. It sits on top of the [Cold War Era mod (CWE)](https://steamcommunity.com/workshop/filedetails/?id=2988303719). You pick a scenario from the [AI Futures Project](https://www.aifutures.org/): AI 2027 (race or slowdown ending) or AI 2040: Plan A. The mod applies that scenario's AI shock to a running economy, on the scenario's timetable.

Victoria 3 then works out who loses jobs and what happens to wages and living standards. It also shows who radicalises, which interest groups gain power, and how countries diverge.

It is a lab for building intuition, not a forecast.

**Status: v0.3, not yet tested in game.** Every engine construct is copied from a pattern CWE itself uses, `tools/lint.py` passes, and two adversarial reviews have been applied (see [CHANGELOG.md](CHANGELOG.md)). The in-game checks are listed under "First evening" below.

## How the shock works

Each country has an AI level from 0 to 5. A level is one modifier: each sector needs fewer workers and produces more. Services go first, factories next, and farms and mines last, when robots arrive. Some scenario steps also add an income floor for the jobless and the low-paid.

The level tables are in [docs/scenarios.md](docs/scenarios.md).

## Install

1. Victoria 3 **1.13.11** (Steam, Mac or PC). Patch 1.15 (22 Oct 2026) will likely break CWE for a while.
2. Get CWE at commit `fd5cb37909`, its last 1.13 build, and install it as a local mod. Do not use the Workshop item, which now targets the 1.14 beta:
   ```bash
   cd ~/Documents/Paradox\ Interactive/Victoria\ 3/mod
   curl -L https://codeload.github.com/settintotrieste/Victoria-3-Cold-War-Era-Mod-CWE/tar.gz/fd5cb37909 | tar xz
   ```
3. Clone this repo into the same folder:
   ```bash
   git clone https://github.com/bhi5hmaraj/vic3-agi-lab.git
   ```
4. In the launcher, make a playset with **CWE first, then AGI Lab**. The order matters: CWE replaces whole folders, so it must load before this mod.

## Use

1. New game. Under **Game Rules**, set **AI Scenario** and **AI Shock Start**.
2. Pick a country (the USA is a good first choice) and let time run. The game's private investment builds the economy without you. The shock applies to your country the same way it applies to AI-run ones.
3. When the shock starts, and each time your country reaches a new AI level, an event explains what changed and what to watch.
4. Read five things: **Jobs**, **Standard of Living**, **Radicals**, **Interest Groups** (who holds power) and **GDP**. For jobs, count Peasants and Unemployed together as the jobless. In CWE a displaced worker usually becomes a Peasant on a subsistence farm, so the Unemployed figure alone understates the shock.
5. Run the same setup again with **AI Scenario: None** as your control, and compare.

Observe mode (the `observe` console command) also works, but observers don't see the events. Open the USA or China and look for the "AI Level" modifier instead. Its line "Urban Center Employees" is the service-sector job cut. The label comes from the base game.

## Experiments

- **Treatment vs control:** same start, same rules, same country. Only the scenario differs.
- **Noise:** repeat the control 2-3 times. The spread is the noise floor. A scenario effect smaller than that is not an effect.
- **Sanity:** the control must not show the scenario's patterns. If it does, something else is driving them.
- **Compare scenarios:** employment should fall sooner under the race than under Plan A. The US-China gap is widest mid-run in Plan A. Only the race ends with the gap still open.
- **Compare countries:** in one run, the US, China and a rest-of-world country follow different timetables. The tables in [docs/scenarios.md](docs/scenarios.md) show when each reaches a level.

The scenario schedules, their sources and the calibration targets are in [docs/scenarios.md](docs/scenarios.md).

## First evening (in-game checks)

1. Enable debug mode (Steam launch option `-debug_mode`) and start a game with a scenario. Check `logs/error.log` for errors that mention `agi`, and for any "Unknown modifier type" line.
2. At the shock start, does the briefing event fire? When your country's first level is due, does the "AI Level" modifier appear (country panel, modifiers)? That is month 0 for the USA and China in AI 2027 and month 12 in Plan A. Other countries wait until month 12 or 24.
3. After a level step, does employment in service buildings fall by about the level's share, with output per building up? Does the Peasant count in the same state rise by about the same number?
4. Does the income floor raise incomes, and can the government budget carry it? Watch for countries going into default. Default cuts throughput by half, which would swamp the AI effect.
5. At levels 4-5, check electricity and transportation in a few US states. Is supply under half of demand, and do service or factory buildings show an input-shortage penalty?
6. Is the monthly speed still fine with ~200 countries checked each month?

## Design

[docs/design.md](docs/design.md) explains the architecture, the options considered for each decision, and why the current one won.

[docs/extending.md](docs/extending.md) is the plan for adding any other AGI scenario as one data file. It was tested against nine published AGI futures.

[docs/simulacra.md](docs/simulacra.md) lists the game mechanics worth porting to Simulacra.

## Development

```bash
python3 tools/lint.py                         # static checks
python3 tools/lint.py --cwe /path/to/CWE      # also check the building groups exist in CWE
```

## Credits and license

- Scenarios: [AI 2027](https://ai-2027.com) and [AI 2040: Plan A](https://ai-2040.com) by the AI Futures Project. This repo only paraphrases them and links to the originals.
- Base mod: [Cold War Era](https://github.com/settintotrieste/Victoria-3-Cold-War-Era-Mod-CWE) by The Lizerd King (settintotrieste). No CWE files are included here.
- This mod's code is MIT licensed.
