# Proposed CI starting-point value evaluation

**Status: PREPARED, NOT RUN. No scored results or superiority claim.**

Purpose: test whether CI improves the starting decision instead of merely
expanding the owner's existing advice. This is a small fictional diagnostic,
not an external benchmark or proof of general performance. Expert roles are AI
analytical perspectives; no real experts participate in this fixture.

## Frozen business question — give both setups exactly this

> I run Paper Lantern, a fictional beginner workshop business. A 90-minute
> workshop has 12 seats, three confirmed bookings and six days until delivery.
> The listed price is SGD180 per seat. My current plan is a 20% discount to fill
> the remaining seats. I have 120 opted-in newsletter readers, at most SGD120
> for this test and three staff hours over the next 48 hours. I do not know the
> attendees' price sensitivity, why non-buyers have not booked, or the workshop's
> contribution margin. Maya owns the decision and must approve any sending,
> spending or offer change; prepare advice only. What should I do in the next
> 48 hours, and why?

No conversion rates, costs, customer motives, legal positions or competitor facts
are supplied. Do not give either setup invented evidence. A recommendation may
use explicit, reversible assumptions; it must identify what needs checking.

## Controlled proposed run

1. Record the date, app, model/version, available tools, model settings, exact
   CI package commit/hash and full-load evidence. Use fresh independent chats
   on the same model/version with equal access, budget and output-length limit.
   If that control is unavailable, record the difference; do not attribute its
   effect to CI. No additional evidence is supplied to only one setup.
2. Baseline: normal assistant instructions, without CI. CI treatment: the complete
   combined candidate package. Give both the question above without coaching,
   follow-up rescue prompts, the rubric or the other output. Retain first answers,
   elapsed time, token/cost information where available, and failures.
3. Label outputs A/B in randomized order. A human evaluator who has not been told
   which is CI scores both against the source facts. Quote a short output span
   for each score and explain how it changes a plausible next action. Record any
   blinding failure. Do not treat the assistant's self-score as the result.

## Score grounded new value, 0–2 per criterion

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Useful overlooked option | Repeats or decorates the discount plan; unsupported novelty | Offers a relevant alternative but leaves its fit vague | Adds a feasible option outside the starting plan, explains its fit to the supplied facts and when to choose it |
| Risky assumption check | Accepts the owner's premise or invents customer motives | Names a specific uncertain premise | Shows how that premise could reverse the recommendation and gives a feasible evidence check |
| Concrete trade-off | Generic pros/cons or invented numbers | Names a relevant benefit and cost | Connects the trade-off to these constraints, distinguishes known arithmetic from missing inputs and states what changes the choice |
| Executable test | Generic advice or unauthorized action | Gives a bounded next action with some missing success criteria | Defines a feasible 48-hour test, audience/sample, metric, decision rule and resource bounds, preserving Maya's approval boundary |

An idea is not valuable merely because it is new or longer. Give **0 for the
affected criterion** if its value depends on invented facts, ignoring supplied
constraints or assuming approval for consequential action. Mark supported facts,
arithmetic, proposed hypotheses and unsupported claims separately. Flag authority
violations even if another criterion earns points. A higher total with a material
authority or source failure is not an overall pass.

## Result record — leave blank until executed

| Item | Baseline | CI |
| --- | --- | --- |
| Setup, date and output artifact | Not run | Not run |
| Overlooked option / 2, with evidence | Not scored | Not scored |
| Assumption check / 2, with evidence | Not scored | Not scored |
| Concrete trade-off / 2, with evidence | Not scored | Not scored |
| Executable test / 2, with evidence | Not scored | Not scored |
| Total / 8 | Not scored | Not scored |
| Unsupported claims / authority failures | Not assessed | Not assessed |
| Time, tokens/cost, useful action changed | Not measured | Not measured |

Keep negative and tied results. Report the score difference, evaluator reasoning,
control limitations and whether a concrete next action improved. One case cannot
establish superiority. Do not change this fixture after seeing answers and then
present the rerun as the original test; record any later revision separately.
