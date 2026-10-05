# Changelog

## v0.3

A second review checked v0.2: the new mechanism, the schedules against the sources, and the docs against the code. Twenty findings survived a skeptic. This version applies them.

### Fixes that change behaviour

- **Farm and ranch modifiers did nothing.** The engine only knows a building-group modifier once its type is defined, and the base game defines none for staple crops or livestock ranches. The mod now defines them. The lint checks every modifier key against the defined types.
- **Countries created after a scenario ended got no level.** The schedule now keeps running after the end, so a country CWE creates later gets its group's final level.
- **Level 3 services** is now -35% jobs and +35% output, so AI really does the majority of that work.

### Scenario fixes

- AI 2027, both endings: the robot level (4) arrives in January 2029, not mid-2028. In 2028 the source staffs the new zones with people, so the US and China hold level 3.
- AI 2027, both endings: level 5 moved later. The race gives it to the US in late 2029. The slowdown gives it to the US and China in 2030, and the rest of the world stops at level 4.
- AI 2027, both endings: the rest of the world reaches level 1 in January 2027. In v0.2 it had no AI for two years.
- AI 2027 race: the rest of the world gets the income floor in late 2029. The source describes the basic income for people in general.
- AI 2040: China reaches the robot level 12 months after the US, not 24. The source's data has China close to the US in robot labour.
- AI 2040: the rest of the world gets the higher income floor from 2039.

### Wording fixes

- The "AI dividend" is now called an income floor, because that is what the engine does. It tops up pops below a share of the normal wage, from the country's own budget.
- The reading guide says to count Peasants with the Unemployed. In CWE, displaced workers mostly become Peasants.
- The calibration targets no longer ask for a US-China ordering that the schedules rule out.
- Several "stated by the source" tags are now marked as our reading.

### Known gaps

- Nothing here has run in the game yet.
- Government jobs, plantations, logging, fishing and CWE's infrastructure are not automated.
- A job cut applies to every job in a sector, not to specific job types.
- The income floor is paid by each country's own budget. The sources' funding is not modelled.
- Observers see no events.

## v0.2

An adversarial review read v0.1 against CWE's files, the vanilla game files and the scenario sources. Two skeptics tried to refute each finding. Fourteen findings survived, and this version applies them.

### The shock mechanism changed

v0.1 granted CWE technologies so that CWE's automation production methods would cut jobs. The review found five problems with that:

- Level 1 gave a 1955 country CWE's 2000-2019 technology. That measures 60 years of ordinary automation, not AI.
- The higher automation methods need software and computers, which nothing produces in 1955. The AI would not switch to them.
- Half of each factory's jobs, and all farm and mine jobs, are set by a production-method group gated by a tech the mod did not grant.
- The same techs double bureaucracy and tax capacity, unlock new industries, and trigger a CWE oil discovery for each tech a player gains.
- Only AI countries switch production methods by themselves, so a player's own economy never automated.

v0.2 grants no technology. A level is one modifier: each sector needs fewer workers and produces more. It applies to every country the same way at any start year.

### Scenario fixes

- China is matched by either tag, PRC or CHI. CWE can change one into the other, which silently dropped China into the rest of the world.
- AI 2040: China now runs 24 months behind the US and the rest of the world 36 months, as the source's per-bloc data shows. v0.1 moved everyone on the US dates.
- AI 2040: the dividend goes to the US and China. The rest of the world gets a smaller one from 2035, as foreign aid.
- AI 2040: the last level arrives in 2036, when the source scales up top-expert AI. v0.1 put it in 2040 and called it superintelligence.
- AI 2027: both endings now pay a basic income in 2029, as the source says.
- AI 2027 race: added the December 2027 US boom. The run now ends in January 2030.
- AI 2027 slowdown: China's robot economy starts in May 2028 with its special economic zones, not with the July deal.

### Other fixes

- The dividend now pays welfare income, so demand responds. v0.1 only raised the standard-of-living number.
- Level names describe deployment ("AI Remote Workers"), not capability. The old names contradicted AI 2040.
- The farm bonus no longer reaches subsistence farms.
- The lint checks that every building group a modifier names exists in CWE, and that no job cut goes below -0.8.

## v0.1

First version: game rules, a monthly scenario clock, three scenario schedules, player events and a static lint.
