# Changelog

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
- AI 2027 race: added the December 2027 US boom. The rest of the world now gets robots in late 2029, and the run ends in January 2030.
- AI 2027 slowdown: China's robot economy starts in May 2028 with its special economic zones, not with the July deal.

### Other fixes

- The dividend now pays welfare income, so demand responds. v0.1 only raised the standard-of-living number.
- Level names describe deployment ("AI Remote Workers"), not capability. The old names contradicted AI 2040.
- The farm bonus no longer reaches subsistence farms.
- The lint checks that every building group a modifier names exists in CWE, and that no job cut goes below -0.8.

### Known gaps

- Nothing here has run in the game yet.
- Government jobs, plantations, logging and fishing are not automated.
- A job cut applies to every job in a sector, not to specific job types.
- Observers see no events.

## v0.1

First version: game rules, a monthly scenario clock, three scenario schedules, player events and a static lint.
