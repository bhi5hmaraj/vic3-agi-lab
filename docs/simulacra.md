# What Simulacra takes from Victoria 3 and EU4

Design decision 1 in [design.md](design.md) rejected EU4 as the host for this lab. It did not reject EU4's mechanics, and three of the six below come from it.

Simulacra today, in the `ai-risk-ttx` repo: a `GameSetup` is a title, a description, one `coreMetric` number and stakeholders with hidden objectives. Each round the model picks one `publicScoreUpdate` and writes the `nextEvent`, and `sessionEngine.ts` adds the number to the score. Nothing can explain why it moved.

Mechanics to port, most useful first:

| From | Mechanic | In Simulacra |
|---|---|---|
| Both | Named, timed, stacking modifiers with slots. An action never edits a number. It adds a named effect with a size and a duration, and the number is the sum of what is active. | Each action adds one. The "why did this move" breakdown is the list of active ones. This covers the effect-template and per-round-breakdown items in `TODO.md`. |
| Victoria 3 journal entries, EU4 disasters | Threshold bars. Progress creeps toward a marked line while its conditions hold. | Every tipping point shows as a bar, so players see a regime shift coming |
| Victoria 3 | Interest groups: approval times clout | Each AI stakeholder is two numbers computed from the state, and its move follows from them without an LLM call |
| Victoria 3 | Radicals come from a fall in living standards, not from a low level | The public score reacts to the change since last round |
| EU4 | Aggressive expansion. Each grab leaves a fading grudge, and past a threshold the neighbours form a coalition. | A self-serving action adds fading suspicion with the stakeholders it hurts. Past a threshold they act together, so a hidden objective has a visible cost. |
| EU4 | Institutions. A technology starts in one place and spreads, and laggards pay a growing penalty. | AI capability spreads between actors, and falling behind costs more each round |

Do not take the scale. These games track hundreds of modifier types, and Simulacra needs about eight numbers.

Scenario data needs no new code. Paste a scenario's `summary` and step notes into `getCustomScenarioPromptAndSchema` in `prompts.ts`, which already takes free text. The model still invents the core metric and the stakeholders, because a scenario file holds country blocs and no people.

Two published scenarios, AI-Enabled Coups and Superintelligence Strategy (MAIM), need actors, choices and rules. They do not fit this mod (see [extending.md](extending.md)), so they are written as Simulacra scenarios directly.

Lab runs give signs and orderings that beat the control's noise floor, such as whether radicals rise less where an income floor is paid. They wait for Simulacra's state vector, which is still an open item in `TODO.md`.

No `scenarios.json` export and no importer are built. Emit that file when something exists to read it.
