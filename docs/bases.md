# Base mods

AGI Lab runs on the Cold War Era mod (CWE). This page answers one question: should it also run on Tech & Res (T&R), and how.

Nothing on this page ran in the game. Every claim comes from files and web pages read on 2026-10-05. Nothing it proposes is built.

| What | Version read |
|---|---|
| AGI Lab | v0.3, commit `c1a0ec6` |
| CWE | commit `fd5cb37909`, its last 1.13 build |
| T&R | commit `4a432e3`, GitHub `main`, version 1.7, pushed 2026-09-27 |
| Vanilla | 1.13.10, from [V3-Vanilla-Extract](https://github.com/settintotrieste/V3-Vanilla-Extract) at `eba06b7e4c`. No public copy of 1.13.11 was found |

File paths are relative to each mod's root. "(unverified)" marks a claim that had one reading and no second check.

## 1. Summary and recommendation

Keep CWE as the default base, and add T&R later as a second base with its own playset, never in one playset with CWE. v0.3 names only building groups, tags and modifier keys that exist on T&R, so it should load there unchanged. A proper build then costs one base profile of 12 lines plus about 45 lines of tooling. The cost is run time, because T&R starts in 1836 and the shock waits 119 to 149 game years (5 to 35 on CWE). T&R also files offices and software houses under heavy industry, so the "services first" levels reach urban centres alone. Read T&R's AI goods as markets, and build nothing before the first two checks in section 8 pass.

| Way to use T&R | Verdict | Why |
|---|---|---|
| Alternative base, own playset | Yes, later | Small in code and slow per run. It gives a second economy to check CWE results against. |
| One playset with CWE | No | CWE replaces the folders T&R builds on (section 3). |
| Ideas only | For Simulacra | T&R prices AI as a good. AGI Lab on CWE needs no goods, so it has nothing to borrow. |

## 2. CWE, Tech & Res and Modern World Economy

Modern World Economy (MWE) is Steam item 3797062600. No public source was found, so its column repeats the Steam page.

| | CWE | T&R | MWE |
|---|---|---|---|
| Start | 1950. `common/defines/cwe_defines.txt:2`: `START_DATE = "1950.1.1"` | 1836. `common/defines/ztr_defines.txt` sets no start date, so vanilla's applies | 1836 |
| Game years before the shock | 5, 20 or 35, for the start years 1955, 1970, 1985 | 119, 134 or 149 with the same start years | unknown |
| End date | 2092 (`cwe_defines.txt:3`) | 2036. `ztr_defines.txt:2`: `END_DATE = "2036.1.1"` | 2050 |
| Tech runway | 26 techs per era. Eras 6-10 carry the comments 2000 to 2100 | Era 10 (2012-2031) has 21 techs. Era 11 (2032-2051) has 8 | unknown |
| AI, compute and data goods | `software`, `computers`, `industrial_robots`. No AI or data good | `ai_systems`, `processors`, `computer`, `robotics`, `softwares`, `raw_data`, `organized_data`, `business_data` | data centres, robotics, AI, semiconductors |
| Job loss from automation | 132 automation production methods in tiers 0-10, each cutting a named pop type | Robot tiers in eras 6, 8 and 10. AI cuts a few hundred jobs per building level (section 4) | unknown |
| Where knowledge work sits | `bg_service`: 7 building types in three child groups | `bg_heavy_industry`, beside the steel mills. `bg_service` holds the urban centre alone | unknown |
| World at shock time | Real 1950 history plus 5 to 35 years of drift | 119 or more years of alternate history | as T&R |
| Maturity | 38,574 subscribers. Steam item updated 2026-10-04 | 65,148 subscribers. Steam has 1.6 from May 2026. GitHub has 1.7, marked "NOT SAVE COMPATIBLE" | 0.5.0-alpha, created 2026-09-06, 383 subscribers |
| Other mods needed | none | Kuromi's AI (KAI) and Community Mod Framework (CMF) | unknown |
| Game version | 1.13.11 at the locked commit. `master` targets the 1.14 beta | `1.13.*`. The 1.7 changelog says "No 1.14 Beta support" | 1.13.11 |
| After patch 1.15 (22 Oct 2026) | one mod to wait for | three mods to wait for | unknown |
| Source and licence | GitHub, no licence | GitHub, no licence | Steam only |

KAI is a script dependency: `common/script_values/ztr_ai_script_values.txt:58` reads `kai_country_income_normalized`, which T&R never defines. CMF is on the Steam required list, and no T&R script names a CMF symbol.

### How long until T&R has an economy to shock

| Building | Unlock tech | Era, with T&R's date comment |
|---|---|---|
| Urban centre | vanilla | from 1836 |
| Office | `market_studies` | era 6, 1932-1951 |
| Software house, computer plant | `software_tech`, `computer` | era 7, 1952-1971 |
| Data centre | `digital_infrastructure` | era 8, 1972-1991 |
| E-commerce, first `ai_systems` | `on_demand_delivery`, `machine_learning` | era 9, 1992-2011 |
| Generative AI | `artificial_intelligence` | era 10, 2012-2031 |
| Agentic AI and AGI | `agentic_ai`, `artificial_general_intelligence` | era 11, 2032-2051 |

The dates are comments in `common/technology/eras/00_eras.txt`. The game does not enforce them, and no run has measured T&R's research pace. The author's Steam text dates offices "From 50s" and data centres "The 80s".

The shock needs none of these buildings. It needs urban centres and factories with many workers. By T&R's era dates, a 1985 start meets an economy with offices and software houses. A start before about 1950 would move little, because most pops still work subsistence farms, which the shock skips.

### End date and scenario length

AI 2040 runs 180 months. `common/defines/zz_agi_defines.txt` sets the end date to 2200 and sorts after `ztr_defines.txt`, as it does after `cwe_defines.txt`. So 2036 should not stop a run. That is untested on T&R. From a 1985 start the scenario ends in 2000, inside T&R's content.

### The US and China in an 1836 start

`USA` and `CHI` both exist in 1836. `CHI` is Qing China, an unrecognised country. T&R scripts a Chinese civil war: the communist side takes the tag `CHI` (`common/scripted_effects/ztr_china_scripts.txt:1185`: `change_tag = CHI`) and the nationalist side is `ZFC`. So `CHI` stays the mainland.

The US-China framing means nothing in the 19th century, and the earliest start year (1955) keeps the shock out of it. By 1985 both tags exist in most runs (unverified), but that run's history decides which countries lead. Check GDP ranks at month 0. If the tags name the wrong countries, choose the two largest economies in their place. Build that after a run shows the need.

## 3. Can CWE and T&R share a playset

No, in either load order. This is a reading of the files. Nobody loaded the two together.

- **CWE replaces the folders T&R edits.** CWE's `.metadata/metadata.json` lists these under `replace_paths`: `common/technology`, `common/buildings`, `common/building_groups`, `common/production_methods`, `common/production_method_groups`, `common/laws`, `common/country_definitions`, `events`. T&R has no `replace_paths`.
- **The tech trees share no key.** T&R's techs name 35 to 57 vanilla techs as prerequisites, by how the blocks are counted. None exists under CWE.
- **The era files collide.** Both ship `common/technology/eras/00_eras.txt`. CWE has `era_1 = { #1900-1920`. T&R's `era_1` carries the comment `#Pre-1836`.
- **T&R's patches lose their targets.** T&R edits vanilla objects with `INJECT:` and `REPLACE:`. Under CWE the target is missing for 103 of 110 production-method groups, 68 of 86 production methods and 19 of 48 buildings.
- **Keys are defined twice.** Examples: goods `pharmaceuticals`, `plastics`, `telecommunications`, the building `building_software_industry`, the group `bg_nuclear_weapons`.
- **The worlds differ.** T&R assumes 1836 states. CWE replaces the history folders with 1950.

No patch was found. T&R's Steam page lists 11 compatibility patches and none is for CWE. The "Compatches" item (Steam 3585473709) pairs T&R with six other mods, and CWE is absent. Other authors publish one item per base: "OGAS for CWE" (3770300244) and "OGAS for tech&res" (3700945740).

A patch would rebuild one mod's economy on the other's tech tree. That is far outside this lab.

## 4. T&R's AI economy

### The chain

1. Industries emit `raw_data` from their data-optimization production methods.
2. Data centres turn `raw_data` into `organized_data`.
3. Offices turn `organized_data` into `business_data`, which the industries buy back.
4. Data centres train `ai_systems` in three tiers.

| Training tier | Tech and era | `organized_data` used | `ai_systems` made |
|---|---|---|---|
| `pm_neural_model_training` | `machine_learning`, era 9 | 60 | 15 |
| `pm_generative_ai_models` | `artificial_intelligence`, shown in game as "Generative AI", era 10 | 90 | 35 |
| `pm_artificial_general_intelligence` | `artificial_general_intelligence`, era 11 | 250 | 80 |

Source: `common/production_methods/ztr_data_production_methods.txt:596`, `:618`, `:643`.

**Buyers.** 29 production methods make or use `ai_systems`. The widest buyer is the AI tier of the data-optimization group, on 36 buildings. That tier takes 2 to 6 `ai_systems`. In return building throughput goes to +150% (light industry) or +180% (heavy), about 60 points above the internet tier (`:1398`, `:1599`, `:1668`). The largest single buyers are fusion plasma control and the advanced research centre at 100 each.

**Price.** The good costs 30 (`common/goods/ztr_new_goods.txt:397`) and no pop buys it. The author's break-even comments price it at 60, so training may lose money at the base price. The good `androids` is defined, and nothing makes or uses it.

**Techs.** No T&R event, journal entry or static modifier names them.

| Tech | Era | Its own modifier |
|---|---|---|
| `machine_learning` | 9 | research speed +5% |
| `artificial_intelligence` | 10 | tax capacity +25, building throughput +5% |
| `agentic_ai` | 11 | `ai_systems` output +5%. Office, software and e-commerce throughput +5% |
| `artificial_general_intelligence` | 11 | building throughput +5% |
| `autonomous_road_vehicles` | 11 | `ai_systems` output +5% |

Source: `common/technology/technologies/ztr_new_society.txt:824`, `:1225`, `:1391`, `:1411` and `ztr_new_production.txt:1885`.

**Laws.** The `data_policy` group is T&R's brake on compute (`common/laws/ztr_data_policy.txt`).

| Law | Needs | Effect |
|---|---|---|
| `law_data_free_harvest` | default | none |
| `law_data_privacy_basic` | `data_processing` | `raw_data` -25%, `ai_systems` -25% |
| `law_data_biometric_ban` | `digital_governance` | `raw_data` -50%, `ai_systems` -75%, research speed -5% |

**The dial.** `goods_output_ai_systems_mult` is declared at `common/modifier_type_definitions/ztr_new_goods_modifier_types.txt:899`. Two techs, two laws and one company set it.

### What it does to jobs

T&R's job cuts come from robots in factories. Nothing in it removes knowledge work at scale.

- Training AI cuts no jobs. All three training tiers add 125 academics and remove 125 engineers per level (`ztr_data_production_methods.txt:658-661`).
- The AGI tech adds 5% building throughput and nothing else (`ztr_new_society.txt:1421-1423`).
- The cuts that depend on AI are a few hundred jobs per building level. Vibe coding removes 250 engineers. Office cloud analysis removes 250 clerks and 250 engineers. Autonomous trucks remove 250 machinists beyond ordinary trucks. Precision agriculture removes 750 to 1,500 farmers.
- Robots cut more, and they arrive early. In the steel mill the machinist cut is 750 at the era 6 tier, 1,000 at era 8 and 1,250 at era 10 (`common/production_methods/ztr_new_production_methods.txt:796`, `:1757`, `:1788`). Each tier also lists 2,000 fewer laborers, a cut inherited from vanilla's older tiers.

So in a leading economy T&R's own automation is mostly spent by 2026.

### AGI Lab levels on T&R

The middle column is what the v0.3 modifier moves. The right column is T&R's nearest content, for reference. AGI Lab grants none of it (`docs/design.md`, decision 4).

| Level | What the modifier reaches on T&R | Nearest T&R content |
|---|---|---|
| 1 AI Assistants | Urban centres: 5% fewer jobs | `machine_learning` and `artificial_intelligence`: the first two training tiers, and the AI data tier on 36 buildings |
| 2 AI Remote Workers | Urban centres -15%. Every `bg_manufacturing` building -5%: factories, offices, software, interactive media, data centres, e-commerce, hydroponic farms | `agentic_ai`: vibe coding, +5% office and software throughput |
| 3 AI-Majority Knowledge Work | Urban centres -35%, `bg_manufacturing` -15% | `artificial_general_intelligence`: the 80-unit training tier, +5% throughput, no job change |
| 4 AI and Robots | Urban centres -55%, `bg_manufacturing` -45%. Adds staple-crop farms and mines at -25%. Ranches get nothing. Oil rigs join once the profile names `bg_oil_extraction` | IoT factory tiers, `precision_agriculture`, `autonomous_and_remote_ops_mining`, `cobots`, `smart_energy_grid` |
| 5 AI-Run Economy | The same groups at -40% to -75% | `autonomous_road_vehicles`. T&R has nothing past it |

Two things to know when you read a T&R run:

- T&R's own AI data tier already gives +150% to +180% building throughput. AGI Lab's level 5 adds +120% to that, so it is the smaller of the two.
- From era 10 the control run has T&R's AI techs too. The two arms still differ by the modifier alone.

### What to use

| T&R content | Verdict | Why |
|---|---|---|
| Markets for `ai_systems`, `robotics`, `softwares`, `business_data` | Use now | Reading prices and output needs no code. |
| `goods_output_ai_systems_mult` | Later, T&R only | One line maps AI 2040's compute cap (negative) or the race (positive) onto T&R's own dial. It acts only where a data centre runs a training tier, and a player must switch that tier on by hand. |
| `building_office_throughput_add`, `building_software_industry_throughput_add`, `building_datacenter_industry_throughput_add` | Later, if levels 1-3 look flat | T&R declares them (`common/modifier_type_definitions/ztr_building_modifier_types.txt:159`, `:175`, `:191`). They raise knowledge-work output ahead of factories. They cut no jobs, and they stack with the factory bonus. |
| Tech grants per level | No | Decision 4 rejected them on CWE, and the same faults apply here. |
| A new production method for office job cuts | No | Eight existing methods are gated on the methods now in that slot (`pmg_data_transportation_building_office`). A building that switched would lose them. |
| Forcing a data-policy law | No | A law change moves politics, which the lab is there to observe. Untested. |
| `androids` | No | Nothing makes or uses it. |

For Simulacra: T&R treats AI as a priced good, made from data in data centres and bought by other sectors for more output. That idea moves to Simulacra without any T&R file.

## 5. Base-profile design

### What depends on the base

| Item | Where today | CWE | T&R | Needed for a first T&R build |
|---|---|---|---|---|
| Sector building groups | `common/static_modifiers/agi_modifiers.txt` | `bg_service`, `bg_manufacturing`, `bg_staple_crops`, `bg_livestock_ranches`, `bg_mining` | `bg_service`, `bg_manufacturing`, `bg_staple_crops`, `bg_mining`, `bg_oil_extraction` | yes |
| China tags | `common/scripted_triggers/agi_triggers.txt:3-8` | `PRC`, `CHI` | `CHI` | yes |
| Mod name and id | `.metadata/metadata.json` | "AGI Lab (for Cold War Era)" | "AGI Lab (for Tech & Res)" | yes |
| Lint lookup path | `tools/lint.py --cwe` | the CWE folder | the T&R folder plus vanilla | yes |
| Shock start years | game rules, `agi_effects.txt:131-133`, 6 localisation lines | 1955, 1970, 1985 | the same three work. 2005 and 2026 would suit T&R better | no |
| Event image key | `events/agi_events.txt`, 9 lines | `texture =` | `video =` | test first |
| Income-floor size | `agi_modifiers.txt` | CWE's welfare laws add 0.01 to 0.05 | vanilla's welfare institution adds 0.2 per level | no, calibrate later |

The rest is the same on both bases: the clock, the level and floor effects, the schedules, the monthly hook, the modifier-type file and the end-date define.

Why the T&R values differ:

- **T&R layers on vanilla.** It has no `replace_paths` and replaces two vanilla files by name. So vanilla's building groups, tags and modifier types stay in force.
- **Services.** No T&R building is in `bg_service`. The group holds vanilla's `building_urban_center` alone. On CWE it holds 7 service building types.
- **Knowledge work.** `common/buildings/ztr_digital_buildings.txt:3`, `:23`, `:44`, `:108`, `:129` put the office, software, interactive media, data centre and e-commerce buildings in `bg_heavy_industry`. Vanilla's `bg_heavy_industry` has `parent_group = bg_manufacturing`.
- **Ranches.** Vanilla lists `bg_livestock_ranches` under "LEGACY BUILDING GROUPS ... not actually used" (`common/building_groups/00_building_groups.txt:753`, `:767`). The ranch sits in `bg_ranching`, which also holds subsistence pastures and has no declared job key. So T&R leaves ranches out.
- **Oil.** CWE files `bg_oil_extraction` under `bg_mining`. Vanilla files it under `bg_extraction` (`:353-354`), so the T&R profile names it. Vanilla declares both keys for it.
- **China.** In vanilla `PRC` is the Paris Commune: French culture, capital in Ile-de-France (`common/country_definitions/00_countries.txt:3964`). China is `CHI` (`:1818`). T&R scripts name `c:CHI` 112 times and `c:PRC` never. Today's trigger would count a Paris Commune as China.
- **Modifier keys.** Vanilla 1.13.10 declares `_employee_mult` and `_throughput_add` for `bg_service`, `bg_manufacturing`, `bg_mining` and `bg_oil_extraction`. AGI Lab's own `common/modifier_type_definitions/agi_modifier_types.txt` declares them for staple crops and livestock ranches. That file should serve both bases, because the legacy ranch group still exists on T&R (unverified in game).
- **Income floor.** `state_welfare_payments_add` and `state_standard_of_living_add` are vanilla types (`common/modifier_type_definitions/00_modifier_types.txt:1531`, `:1549`). T&R does not touch welfare payments.

### Options

| Option | Verdict | Why |
|---|---|---|
| **(a) A profile per base, one built folder per base** | **Chosen** | The base items are static data. `docs/extending.md` already plans `bases/cwe.yaml`, so a second base is one more file and a flag. |
| (b) One mod with a "base" game rule | Rejected | A static modifier cannot branch. Both bases' level sets would load on every base, and a player could choose the wrong one. |
| (c) Detect the base at run time | Rejected | It has the limit of (b). Detection reaches effects and triggers, and the differences are in modifiers and metadata. |
| (d) One git branch per base | Rejected | Every scenario fix needs a cherry-pick. |
| (e) One hand-written folder for both | Smoke test only | v0.3 should load on both, but the China trigger is wrong on T&R and oil rigs are missed. |
| (f) Cut jobs by profession on every base | Deferred | The engine pattern `building_employment_<pop type>_mult` would let clerks go before machinists and drop the group mapping. Vanilla declares no such type, and nobody has tested one. |

### Profiles

`docs/extending.md` defines `sectors` and `roles`. This design adds `name`.

```yaml
# bases/cwe.yaml
# settintotrieste/Victoria-3-Cold-War-Era-Mod-CWE@fd5cb37909, game 1.13.11
name: Cold War Era
sectors:
  services:  [bg_service]
  factories: [bg_manufacturing]
  farms:     [bg_staple_crops, bg_livestock_ranches]
  mines:     [bg_mining]                 # CWE files oil extraction under mining
roles:
  usa:   [USA]
  china: [PRC, CHI]                      # CWE can turn PRC into CHI
```

```yaml
# bases/tr.yaml
# mattia2110/tech-and-res@4a432e3, version 1.7, game 1.13.*
name: Tech & Res
sectors:
  services:  [bg_service]                # urban centres
  factories: [bg_manufacturing]          # includes offices, software, data centres
  farms:     [bg_staple_crops]           # bg_ranching also holds subsistence pastures
  mines:     [bg_mining, bg_oil_extraction]
roles:
  usa:   [USA]
  china: [CHI]                           # PRC is the Paris Commune here
```

A check script ran an earlier draft of both profiles against the base files: every group exists, every key is declared, every tag exists. The script tests that each name exists. Whether a group holds any building is outside it.

### What gets generated

The plan in `docs/extending.md` stays as it is. `uv run tools/build.py` writes the CWE files into the repo root and they are committed, so a CWE player installs the mod as today.

T&R adds one flag:

```bash
uv run tools/build.py --base tr --out "<Victoria 3 mod folder>/agi_lab_tr"
```

It copies the hand-written files, writes the generated ones from `bases/tr.yaml`, and leaves the result outside git. Three files differ from the CWE build:

1. `common/static_modifiers/agi_modifiers.txt`: no ranch lines, and oil extraction at levels 4 and 5.
2. `common/scripted_triggers/agi_triggers.txt`: `agi_is_china` matches `CHI` alone.
3. `.metadata/metadata.json`: name, id `vic3_agi_lab_tr`, description.

Scenario files name roles and never tags, so one schedule serves both bases. The level table in `scenarios/_scale.yaml` is shared too.

Build these when a T&R run shows the need:

| Profile field | What it adds | Trigger to build it |
|---|---|---|
| `start_years` | Generated start-year options, plus one generated trigger that replaces the three dated lines in the clock | 1985 proves too early on T&R, or you want game dates to equal scenario dates (2026) |
| `event_image` | The build swaps `texture` for `video` in 9 event lines | The events show no picture on T&R |
| `levels` or `floor` values per base | A per-base copy of the numbers | Calibration shows one base needs different numbers |

## 6. Changes in this repo

Step 0 changes nothing: run v0.3 on T&R as it is (section 8).

Step 1 assumes the generator from `docs/extending.md` exists.

| File | Change | Lines |
|---|---|---|
| `bases/tr.yaml` | new | 12 |
| `bases/cwe.yaml` | add `name` | +1 |
| `tools/build.py` | `--base` and `--out`, copy the hand-written files, write the metadata | +30 |
| `tools/lint.py` | Take the mod folder as an argument. `--cwe` becomes `--base`, with `--vanilla` for a base that layers on vanilla. Add the two oil keys to `VANILLA_MODIFIER_TYPES` | +15 |
| `README.md` | T&R install, load order (CMF, KAI, T&R, AGI Lab), the wait before the shock | +15 |
| `docs/design.md` | Decision 2: correct the T&R row and link here | 3 |
| Paradox script in the repo root | none | 0 |

That is about 75 lines, and none of it is Paradox script.

The deferred items are extra: `start_years` about 40 lines, `event_image` about 5, the office output keys about 15, the `ai_systems` dial about 5.

Without the generator, the same T&R build is a hand edit of 10 lines in a copy of the repo: one tag in `agi_triggers.txt`, four ranch lines out and four oil lines in `agi_modifiers.txt`, and the name in `metadata.json`. Do that for a test and no longer, because a hand copy drifts.

One fact about today's lint: `python3 tools/lint.py --cwe <T&R>` prints five "building group not in CWE" lines. All five groups are vanilla's, and the lint reads the base folder alone.

## 7. Licences

Neither GitHub repo has a licence file. The GitHub API returns `license: null` for both. Default copyright applies, so the authors keep all rights. This is a lay reading of the terms.

| Allowed | Needs the author's permission |
|---|---|
| Name their keys in our script and profiles: building groups, modifier types, tags | Copy their files, or large parts of one, into this repo |
| List the mod as a dependency and link to it | Publish their content under our MIT licence |
| Tell users to get the mod from Steam or the author's GitHub | Put a `REPLACE:` block in our mod that repeats their definition with small edits |
| Point `tools/lint.py` at a user's local copy | Commit a snapshot of their files as test data |
| Describe how the mod works in our own words | |

A Steam subscriber gets personal, non-commercial use under the Steam Subscriber Agreement (sections 2.A and 6.B). Section 2.G bars copying and derivative works. T&R's Steam page also says parts of the mod belong to other authors, so the T&R author's permission would not cover every file.

If AGI Lab ever has to change a base object, use `INJECT:`. It adds our lines and repeats none of theirs. Paradox's own mod policy was not checked.

## 8. Risks, open questions and first tests

### Test first, in this order

1. **Can a game rule change in a loaded save?** The Victoria 3 wiki says rules change through the Switch Country menu (its page is marked for game 1.10). On CWE, start with AI Scenario: None, save, reload, set a scenario, and look for the "AI Level" modifier a month later. The clock reads the rule every month (`common/scripted_effects/agi_effects.txt:129-133`), so it needs no new script. If this works, control and treatment branch from one save on either base, and T&R's wait is paid once.
2. **Does v0.3 load on T&R?** Playset: CMF, KAI, T&R from GitHub at `4a432e3`, AGI Lab last. Read `error.log` and `debug.log` for `agi` and for "Unknown modifier type".
3. **Does the modifier bite?** In the same game, apply `agi_set_tier_4` to the USA from the debug console (exact command unverified). Urban centres, factories, staple farms and mines should lose workers. Ranches and oil rigs should not. Check whether the event shows a picture.
4. **How long is the wait?** Run observe mode from 1836 and time it to 1955 and to 1985. At each date note the GDP ranks of `USA` and `CHI` and the count of office buildings in the USA.

Stop here if step 4 costs more than you will pay per experiment.

### Risks

- **Run time.** CWE's FAQ gives 5 min 26 s at 1951 and 7 min 19 s at 1975, against 4 min for vanilla's 1900 benchmark save. It states no unit. If the unit is one game year, 119 to 149 years take 8 to 10 hours at the vanilla rate. T&R with KAI is likely slower.
- **Noise.** Treatment and control drift apart from game start. On CWE that is 5 to 35 years. On T&R it is 119 or more, and alternate history would swamp the shock. T&R needs test 1 to pass.
- **Coarse sectors.** Levels 1 to 3 cut urban-centre jobs first. Offices follow with the factories from level 2. The office output keys in section 4 fix output and leave jobs alone.
- **T&R's own AI.** From era 10 T&R adds its own throughput (section 4). A 2026 start measures AGI Lab's modifier on top of it.
- **China.** T&R's civil war splits China after 1940. A monthly hook keeps radical-dampening modifiers on `CHI` and `ZFC` until reunification (`common/on_actions/ztr_on_actions.txt:433`). Radicals in China are confounded for those years.
- **Version drift.** GitHub is one version ahead of Steam and not save compatible. Lock to the commit and use a local copy, as with CWE. After patch 1.15, T&R needs three mods to update.
- **Growth drag.** T&R's `dev_N_country` modifiers slow construction in richer countries. `dev_8_country` has `state_construction_mult = -0.3` (`common/static_modifiers/ztr_economy_modifiers.txt:70`). A boom may look smaller than on CWE.

### Open questions

- What the engine shows when `texture =` names one of vanilla's video aliases.
- Whether an undeclared building-group key drops one line or the whole modifier. Another mod's `error.log` shows "Unknown modifier type" for such a key (East-Asia-Flavor-Pack, `documentation/japan_p0_error.log`). v0.3 declares all four of its own.
- Whether the later-sorting define file wins on T&R as it does on CWE.
- T&R's real research pace against its era comments.
- Vanilla 1.13.11. The files read were 1.13.10.
- MWE's internals. Look again when it has a public source or a stable release.

## Sources

- [Tech & Res on GitHub](https://github.com/mattia2110/tech-and-res) and [on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3472248460)
- [Cold War Era on GitHub](https://github.com/settintotrieste/Victoria-3-Cold-War-Era-Mod-CWE) and [on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2988303719)
- [Modern World Economy on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3797062600)
- [Compatches on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3585473709)
- [Vanilla 1.13.10 files](https://github.com/settintotrieste/V3-Vanilla-Extract)
- [Victoria 3 wiki: Modifier types](https://vic3.paradoxwikis.com/Modifier_types) and [Game rule](https://vic3.paradoxwikis.com/Game_rule)
- [vic3-tiger modifier table](https://github.com/amtep/tiger), for the engine's modifier patterns
- [Steam Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/)