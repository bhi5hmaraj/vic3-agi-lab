# Extending: add any AGI scenario

Status: plan. Nothing in this file is built, and the mod itself has not run in the game. Written against v0.3 (commit `c1a0ec6`).

## 1. Summary

Each scenario becomes one YAML file. A Python generator of about 200 lines turns those files into the Paradox script, the game-rule options, the localisation and `docs/scenarios.md`. The generated files are committed, so players install the mod as they do today. Only authors run the generator.

The generator is step 1, not step 0. Step 0 is an evening in the game on v0.3, because a generator multiplies whatever the mechanism gets wrong. v1 stops once one new scenario (GATE) has run against a control. That is about three evenings.

A draft of the format was tested by encoding nine published AGI futures. Each test listed what the draft could not express. Most of those gaps are deferred until a scenario file needs them. Three of the nine are not Victoria 3 schedules at all (section 3).

The nine, with the short names used below:

- Timelines and visions: Situational Awareness (SA), What 2026 Looks Like (W2026), Machines of Loving Grace (MoLG).
- Models and worldviews: Epoch's GATE model (GATE), AI as Normal Technology (NT), Preparing for the Intelligence Explosion (IE).
- Risk analyses and strategies: Gradual Disempowerment (GD), AI-Enabled Coups (Coups), Superintelligence Strategy (MAIM).

What Simulacra can take from Victoria 3 and EU4 is a separate question, answered in [simulacra.md](simulacra.md).

### Options considered

| Option | A new scenario costs | Checked without the game | Verdict |
|---|---|---|---|
| A. Hand-written Paradox script copied from a template (today) | Six edits in five files, plus the docs table | Names and braces | Rejected. The script and the docs table drift apart. |
| B. Self-registering scenario files | One Paradox file, plus the shared game-rule file | Names and braces | Rejected. See below. |
| **C. YAML and a generator** | **One YAML file** | **Dates, names, levels, citations, a level matrix** | **Chosen** |
| D. C, with a model drafting the YAML from the source | One YAML file and a review | Same as C | Optional. No code and no prompt file. |

Option A's six edits are the schedule effect, the game-rule option, two dispatch branches in `agi_effects.txt`, the start event and the localisation.

Option B relies on Victoria 3 merging `on_actions` lists across files, which this mod already uses for its monthly hook. Each scenario file could register its own schedule. The game-rule options still sit in one `agi_scenario` block, so every scenario would still edit a shared file. CWE uses the `INJECT:` prefix for AI strategies and static modifiers, and whether it works on game rules is untested. The author would still write Paradox script by hand.

C wins for two reasons. The game cannot run in CI, so each mistake caught without it saves an evening. And the basis of a step (stated by the source, or inferred by us) becomes data, with the docs generated from it.

The cost is one dependency for authors. `build.py` names PyYAML in a PEP 723 header and runs as `uv run tools/build.py`. The owner's Python 3.14 has no PyYAML, and `uv` is installed.

## 2. Format v1

```
scenarios/_scale.yaml      the AI level table, shared by every scenario
scenarios/_policies.yaml   the policy library, shared by every scenario
scenarios/ai2027.yaml      one file per source, one YAML document per variant
bases/cwe.yaml             the base profile: facts that depend on the base mod
tools/build.py             the generator
```

### Shared scale

```yaml
# scenarios/_scale.yaml. Each cell is [jobs, output] for one sector at one level.
levels:
  1: {name: AI Assistants,              services: [-0.05, 0.05]}
  2: {name: AI Remote Workers,          services: [-0.15, 0.15], factories: [-0.05, 0.05]}
  3: {name: AI-Majority Knowledge Work, services: [-0.35, 0.35], factories: [-0.15, 0.15]}
  4: {name: AI and Robots,              services: [-0.55, 0.60], factories: [-0.45, 0.60], farms: [-0.25, 0.25], mines: [-0.25, 0.25]}
  5: {name: AI-Run Economy,             services: [-0.75, 1.20], factories: [-0.70, 1.20], farms: [-0.50, 0.60], mines: [-0.40, 0.60]}
```

These are the current numbers. Every scenario uses the same scale, so level 3 means the same thing in each of them.

The generator writes one `agi_tier_N` modifier per level: `building_group_<group>_employee_mult` and `building_group_<group>_throughput_add` for each group the base profile lists under a sector. The format and the docs say "level". The script keeps today's names, `agi_tier_N` and `agi_set_tier_N`.

### Policy library

```yaml
# scenarios/_policies.yaml. One entry is one static modifier.
dividend_1: {slot: dividend, name: Income Floor,        modifier: {state_welfare_payments_add: 0.25, state_standard_of_living_add: 1}}
dividend_2: {slot: dividend, name: Higher Income Floor, modifier: {state_welfare_payments_add: 0.50, state_standard_of_living_add: 2}}
```

Entries that share a `slot` form a ladder in file order, and a country only moves up it. That is what today's two income-floor effects do by hand. Slots also cover tracks such as MoLG's `health_1` to `health_3`.

The library starts with these two entries. Each scenario adds what it needs, under one rule: an entry changes what a country pays, earns or can build.

An entry that instead sets a result the lab exists to observe, such as clout, radicals or legitimacy, must carry `mirror: true`. The docs flag every step that uses one. Design decision 1 calls this the mirror problem.

### Base profile

```yaml
# bases/cwe.yaml
sectors:                               # sector -> building groups
  services:  [bg_service]
  factories: [bg_manufacturing]
  farms:     [bg_staple_crops, bg_livestock_ranches]
  mines:     [bg_mining]
roles:                                 # role -> country tags
  usa:   [USA]
  china: [PRC, CHI]
define_types: [bg_staple_crops, bg_livestock_ranches]   # groups whose modifier types the base game lacks
```

Scenario files name roles, never tags, so they do not depend on the base.

The engine only knows a building-group modifier once its type is defined. `define_types` lists the groups the generator must define the two types for.

Only CWE output is committed, and `build.py` reads this one path. The end date and the shock start years stay hand-written, in the defines file and the clock. A second base such as Tech & Res would be a second file of this size plus a flag. Build neither until the study of that mod lands.

### The scenario file

```yaml
id: ai2027_race
title: "AI 2027: Race"
summary: "The US leads and China follows about two months behind."
source: {name: AI 2027, url: "https://ai-2027.com", authors: [AI Futures Project], year: 2025, kind: forecast}
end: 2030-01
steps:
  - {date: 2026-01, who: [usa], level: 1, basis: S, cite: "Early 2026: Coding Automation", note: "Agent-1 is released to the public"}
  - {date: 2026-01, who: [china], level: 1, basis: I, note: "the source has China about six months behind in mid-2026. The same date is ours"}
  - {date: 2027-01, who: [rest], level: 1, basis: I, note: "the cheap agents are public releases"}
  - {date: 2027-07, who: [usa], level: 2, basis: S, cite: "July 2027: The Cheap Remote Worker", note: "Agent-3-mini released to the public"}
  - {date: 2027-09, who: [china], level: 2, basis: I, note: "the source puts China about 2 months behind. Using that lag for deployment is ours"}
  - date: 2029-01
    who: [usa, china]
    level: 4
    policies: [dividend_1]
    basis: S
    date_basis: I                # the source gives the year, the month is ours
    cite: "2029: The Deal"
    note: "a million robots a month by the end of 2028, and a basic income"
expect:
  - "employment falls sooner than in ai2040_plan_a"
calibration:
  - {date: 2027-10, metric: us_unemployment_change_pp, value: 1, basis: S}
---
id: ai2027_slowdown
title: "AI 2027: Slowdown"
extends: ai2027_race
branch_at: 2027-10               # keep the parent's steps dated before this month
end: 2031-01
steps:
  - {date: 2028-01, who: [rest], level: 2, basis: I, note: "as in the race"}
  - {date: 2028-05, who: [usa, china], level: 3, basis: S, cite: "May 2028: Superhuman AI Released", note: "special economic zones on both sides of the Pacific"}
```

The two `cite` strings from the shared timeline were checked against the site. The two from the endings were not, which is the case the citation check in section 4 exists for.

| Field | Meaning | Victoria 3 mechanism |
|---|---|---|
| `id`, `title`, `summary`, `source` | Identity and provenance. `kind` is forecast, recommendation, model, fiction or analysis. | A game-rule option, its text and a start event |
| `end` | The last month | `agi_end_scenario` |
| `extends`, `branch_at` | Reuse the parent's steps dated before the branch. The child writes every later step and inherits the fields it leaves out. | Generator only |
| `date` | `YYYY-MM`. Month 0 is January 2026 in every scenario. | `global_var:agi_month >= N` |
| `who` | Roles from the base profile, `all` or `rest` | `c:TAG`, or `every_country` with a `limit` |
| `level` | 1-5 on the shared scale | `agi_set_tier_N` |
| `policies` | Library ids | `agi_set_<policy>` |
| `basis`, `date_basis`, `cite`, `note` | S (stated) or I (inferred), a heading or short phrase copied from the source, and our paraphrase | A comment in the script and a row in the docs |
| `expect`, `calibration` | Orderings to check against the control run. Sourced numbers, as a value or a `[low, high]` range. | Docs. Checked by hand against the probe (section 4). |

One calendar anchor keeps runs comparable: month 18 is July 2027 in every scenario, as today. A scenario that starts later has empty months first, as AI 2040 does today. The docs print the month number beside each date.

`all` is every country that is not decentralised. `rest` is every such country outside every role in the base profile, and later outside every group the scenario declares. For the three shipped scenarios that equals today's `agi_is_rest_of_world`.

A role or group that gets no step therefore stays at level 0. That is how a scenario holds a bloc back, and the build warns when `rest` is used and a role has no step.

### Runtime: unchanged

v1 keeps today's semantics. Every due step re-runs each month, including after the scenario ends, and a level or a slot policy only rises. Three things follow:

- A missed month still applies, and a loaded save is safe.
- The schedule repairs itself. A country that forms late, changes tag or flips regime gets the right level the next month. Unemployment-driven revolutions are what this lab provokes, so this matters.
- A country that matches two names in `who` gets the higher level. The build cannot see that overlap, because membership is only known in game.

A per-country "last step applied" counter was considered for levels and rejected. It makes the last write win, and it drops the self-repair.

A setback is a timed negative policy (deferred below), never a lower level.

### Deferred

Build each one when a scenario file that needs it is ready to commit with it.

| Feature | YAML | Victoria 3 mechanism | First needed by |
|---|---|---|---|
| Groups | `groups: {free_world: [GBR, JAP, WGR], democracies: {is: democracy}}` | One scripted trigger per group. Predicates live in the base profile, for example `democracy: "is_a_democracy = yes is_subject = no"`. | SA |
| Raw effect | `vic3: "activate_law = law_type:law_defensive_espionage"` | Runs once in the scope of each `who` country | SA |
| Announce | `announce: {title, text}` | A country event sent to every player, once | SA |
| Timed or removable policy | `{id: ai_hype, months: 12}`, `remove: [dividend_1]` | `add_modifier` with `months =`, and `remove_modifier` | W2026 |
| Level per sector | `level: {services: 3, factories: 1}` | The generator composes one modifier per combination in use, from the same scale | NT, MoLG |
| Choice and chance | Section 6 | Event options, `ai_chance`, `random_list` | SA, MoLG, IE |
| Pace | A game rule: x1, x1.5, x2 | The clock adds 1/k to `agi_month` each month | SA, GATE, MoLG |

Notes on the first three, which arrive together with SA:

- A tag matches `[A-Z][A-Z0-9]{2}`. CWE has 100 tags with a digit, such as `D00`. A tag list goes stale in a 1950 alternate history, and a predicate group does not.
- The `democracy` predicate needs `is_subject = no`. CWE's `is_a_democracy` also matches elective colonial and mandate administrations.
- One-shot effects need a guard, because steps re-run monthly. Each country stores the number of the last one-shot step it ran in `agi_step`. Only raw effects and timed policies read it. Levels and slot policies never do.
- `announce` uses one global counter in the same way.
- `vic3` is the escape hatch. When one raw effect appears in three scenario files, give it a typed field.

Out of the format: wars, people inside a state (a lab CEO, a general), persuasion and media, digital minds. Victoria 3 has no system for them, or none that scripts reliably. They go in `note` text.

A frontier-capability dial and date-free rule overlays were considered and cut. Nothing in the economy would read the dial, and the two sources that wanted them are Simulacra scenarios (section 3).

## 3. Coverage

| Scenario | Verdict | Why |
|---|---|---|
| [AI 2027: Race](https://ai-2027.com) | v1 | |
| [AI 2027: Slowdown](https://ai-2027.com/slowdown) | v1 | `extends` with `branch_at: 2027-10` |
| [AI 2040: Plan A](https://ai-2040.com) | v1 | The China and rest-of-world lags are written as steps |
| [GATE](https://epoch.ai/gate), two presets | v1 | One world economy, so every step is `who: [all]`. The compute investment is a library entry to check in game. Mapping its share of tasks automated to a level is I. |
| [W2026](https://www.lesswrong.com/posts/6Xgy6CAf2jqHhynHL/what-2026-looks-like) | v1, partly | One level step in 2026. The hype cycle needs timed policies. Persuasion stays in text. |
| [SA](https://situational-awareness.ai) | Next after v1 | It brings groups, raw effects and the one-shot guard. Lab lockdown, export controls and relations are raw effects. A military edge that scales with the lead stays in text. |
| [MoLG](https://www.darioamodei.com/essay/machines-of-loving-grace) | After SA | Groups by condition and slots cover the coalition and the health tracks. Per-sector levels keep robots behind knowledge work. |
| [IE](https://www.forethought.org/research/preparing-for-the-intelligence-explosion) | Partly | Schedule and regime groups fit. Research speed has no clean lever: `country_weekly_innovation_mult` also speeds military research. The grand challenges are text. |
| [NT](https://knightcolumbia.org/content/ai-as-normal-technology) | Needs per-sector levels | Its claim is sector-by-sector timing. Its 2025 effect is below level 1, which a throughput-only policy covers. Diffusion that depends on a country's institutions has no lever here. |
| [GD](https://gradual-disempowerment.ai) | Not a schedule | It has no dates. It becomes `expect` rows on any timeline, such as "trade-union clout falls against the control". That tests its claim without scripting the outcome. |
| [MAIM](https://www.nationalsecurity.ai) | Simulacra, not this mod | It describes actors, choices and rules on the US-China frontier gap. Scripted sabotage here would only replay our assumptions. |
| [Coups](https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power) | Simulacra, not this mod | The risk is about who inside a state commands the AI. Victoria 3 has no such actor. |

v1 carries the three shipped scenarios and GATE. Five more fit once a deferred feature or a stated gap is accepted. GD is a test to run, and MAIM and Coups belong in Simulacra.

## 4. Generator

`uv run tools/build.py` reads `scenarios/*.yaml`, the two shared files and `bases/cwe.yaml`. It rewrites the files below.

| File | Generated content |
|---|---|
| `common/scripted_effects/agi_scenarios.txt` | One `agi_schedule_<id>` per scenario, one `agi_set_<policy>` per library entry, and the two dispatch effects the clock calls |
| `common/static_modifiers/agi_modifiers.txt` | `agi_tier_N` from the scale and the base's sectors, `agi_<policy>` from the library |
| `common/modifier_type_definitions/agi_modifier_types.txt` | The two modifier types for each group in `define_types`, and their localisation |
| `common/scripted_triggers/agi_triggers.txt` | `agi_is_<role>` for a role with several tags, and `agi_is_rest_of_world` |
| `events/agi_<id>.txt` | One file and one namespace per scenario, holding its start event |
| `common/game_rules/agi_game_rules.txt` | The scenario options, between two marker comments |
| `localization/english/agi_l_english.yml` | Scenario, level and policy text, between two marker comments |
| `docs/scenarios.md` | The level table, then per scenario: a step table with basis and citation, the level matrix, expectations, calibration and the source |

Everything else stays hand-written: the clock and the tier effects in `agi_effects.txt`, the monthly hook, the defines file, the shock-start rule, and the five level events with their text. No file is renamed.

Each scenario gets its own event file because 322 of CWE's 326 event files hold a single namespace.

`docs/scenarios.md` becomes fully generated. Its closing advice on calibration already lives in `design.md` decision 8.

### Baseline first

The first commit changes nothing a player can see. `build.py` must reproduce three current files from YAML: `agi_scenarios.txt`, `agi_modifiers.txt` and `agi_triggers.txt`. The comparison runs both sides through lint's `script()`, which strips comments, and ignores whitespace.

To match, the generator emits today's shapes: `c:USA` for a one-tag role, `every_country` with `agi_is_<role>` for the others, and one `if` per month.

The second commit moves the per-scenario registration into generated output: dispatch, game-rule options, start events, localisation and docs. From then on a new scenario is one YAML file, and `git diff` on the generated files is the regression check.

### Level matrix

For each scenario the docs print the level every name holds after each month that changes something:

| Month | Date | usa | china | rest |
|---|---|---|---|---|
| 0 | 2026-01 | 1 | 1 | 0 |
| 12 | 2027-01 | 1 | 1 | 1 |
| 18 | 2027-07 | 2 | 1 | 1 |
| 20 | 2027-09 | 2 | 2 | 1 |
| 23 | 2027-12 | 3 | 2 | 1 |

This is the cheapest check for lag and ordering errors, which both reviews of this mod found.

### Checks

The build fails on any of these:

- An unknown or missing field. A typo in a key is an error.
- A date that is not `YYYY-MM`, is before 2026-01, is out of file order, or is after `end`.
- A name in `who` that is not a role, `all` or `rest`.
- A level outside 1-5, a policy missing from the library, or a step with neither.
- A step that lowers the level of a name an earlier step raised. Levels only rise.
- An `extends` that names no scenario or forms a cycle. A `branch_at` outside the parent's dates. A child step dated before `branch_at`.
- An S step without `cite`, or an I step without a `note` that gives the reason.

With `--sources DIR` the build also looks for each `cite` in the saved source text, `DIR/<file name>.txt`, ignoring case and spacing. That catches an invented citation.

`tools/lint.py` stays free of dependencies and keeps its checks, including the one that every modifier key has a defined type. It gains two under `--cwe`, since the build never reads CWE:

- Every `c:TAG` in the script exists in CWE's `common/country_definitions`.
- Later, every identifier left of `=` in a `vic3` string occurs in CWE.

Its localisation check widens by one regex to cover the per-scenario namespaces.

One test file of about 40 lines covers `extends`, month arithmetic and one case per build error. It asserts on resolved steps, never on generated text.

CI is about 15 lines: run the build, fail if `git status --porcelain` prints anything, run `tools/lint.py`. The `--cwe` checks run locally, because the CWE checkout is 1.7 GB.

### Measuring a run

The probe is hand-written and goes in at step 0, before the generator. `expect` rows are worthless without it.

Once a year, `on_yearly_pulse_country` writes one `debug_log` line for each role country and each player: date, tag, AI level, `gdp`, `average_sol`, radicals, trade-union `ig_clout` and employment. Checking an `expect` row means reading those lines from a scenario run and a control run.

What CWE shows about each read:

- `gdp`, `average_sol` and `ig_clout` are read as values, for example `value = gdp`.
- `radical_fraction` appears only as a comparison. A numeric read needs finding.
- Employment is the lab's headline metric and has the weakest read. CWE uses `state_unemployment_rate` three times, as a state trigger, and nothing else.
- CWE's five `debug_log` calls print names and dates, never numbers. Printing a variable is the first thing to test.

If `debug_log` cannot print a number, show the same variables in a yearly event for the played country, with the `Var(...).GetValue` macro CWE's localisation uses.

## 5. Authoring a scenario

1. Read the source. Save a text copy outside the repo.
2. Optional: give a model section 2 of this file, `scenarios/ai2027.yaml` and the source text. Ask for `basis` on every step, `cite` for each S and a reason for each I. Ask for a separate list of gaps: what the source says that the format cannot express.
3. Run `uv run tools/build.py --sources DIR` and fix what it rejects.
4. Review by hand, with the source open beside the generated docs.
   - The level matrix first: are the lags and the ordering what the source says?
   - Each S row: find the cited passage and confirm it says that. If the effect is stated and the date is ours, set `date_basis: I`.
   - Each I row: would another reader accept the reason?
   - Each level: does the source's description match the level's name in the scale? This is the largest judgement in a file.
   - Each gap: a new library entry, a deferred feature, or text in `note`?
5. Commit the YAML and the generated files together.
6. Run the game to the first step in debug mode. Search `logs/error.log` for `agi`.
7. Run the scenario and the control, then compare the probe lines against `expect`.

A model must not approve its own draft. A second model can try to refute each S row, as the reviews of this mod did, but a person signs off.

## 6. Player choices at a branch

Deferred. Today a branch is two game-rule options, and those stay because an experiment needs fixed arms.

A choice would add a third option. At `branch_at` the `usa` player gets an event with one option per branch, and each option sets a global variable that selects the schedule from then on.

AI deciders and chance forks would use `ai_chance` and `random_list`. The weights are our assumption, so the docs would print them as I.

## 7. Build order

| Step | Work | Evenings |
|---|---|---|
| 0 | In game, on v0.3. Pin the game to 1.13.11 before patch 1.15 ships on 22 October 2026 (Steam: Properties, Betas, or switch off automatic updates). Run the README's six first-evening checks. Add the probe and find an employment read. | 1 |
| 1 | `build.py` with roles, `all`, `rest` and `extends`, the two shared files, `bases/cwe.yaml` and the three shipped scenarios as YAML. Commit 1 reproduces the current files. Commit 2 generates the registration, the docs and the level matrix, and adds the test file and CI. | 1 |
| 2 | GATE through section 5. Run it against a control and read both through the probe. | 1 |

Stop there. If check 3 of step 0 fails (jobs do not fall by the level's share), stop earlier: the scale assumes the modifier works.

Later, in the order scenarios ask: SA with groups, raw effects, `announce` and the one-shot guard. Then the rest of the deferred table. A Tech & Res profile follows the study of that mod.

## 8. Risks and open questions

Risks:

- Nothing has run in game. That is why step 0 comes first.
- Patch 1.15 will likely break CWE for a while. The pin in step 0 and a local CWE copy keep the lab running.
- The probe may not be able to print numbers or read employment. Without it, `expect` rows cannot be checked.
- The level judgement. Two authors can place one source a level apart. A written reason exposes the choice and does not settle it.
- A model draft can invent a citation. The `--sources` check catches a `cite` that is not in the text. Only the hand review can tell whether the passage supports the step.
- Scripted outcomes. Several tests asked for political modifiers, and each one makes the lab repeat our assumptions. The `mirror` flag makes that visible and does not stop it.
- One scale gives GATE and AI 2040 the same output boost at level 3, though their growth paths differ. That is the price of comparable runs.
- Raw `vic3` effects are checked for braces and known identifiers only.

Open questions:

- Can `debug_log` print a country variable, and can `state_unemployment_rate` be stored as a value?
- Tech & Res: its sectors, tags and shock years wait on the study of that mod.
- The scale holds one CWE fact: mines stop at -0.4 because CWE's oil concessions add -0.5. Does a second base need its own floor?
- How many scenario options fit in one game-rule list before it is hard to use?