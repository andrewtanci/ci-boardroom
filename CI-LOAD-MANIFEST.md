# CI Boardroom — Canonical Load Manifest

**Purpose:** keep Chat, Work, custom implementations and future product surfaces aligned to the same current operating logic.

GitHub `main` is the canonical source of truth.

## Required runtime files

Load in this order:

1. `BOARDROOM.md` — core operating instructions and authority architecture.
2. `CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md` — reality, objective, whole-outcome, goal/runway, consequence and practitioner-synthesis rules.
3. `CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md` — primary-driver, timing, marginal-gain and habit rules.
4. `CI-EXECUTION-HARD-GATES.md` — mandatory runtime interruption gates for retrieval, decision-changing details, whole-option recalculation, practitioner synthesis and ex-ante learning.
5. Any domain-specific rider explicitly required for the work item.

## Required release / regression tests

Before a version is treated as aligned:

- run `CI-OUTCOME-TESTS.md`;
- run the relevant diagnostic cases in `CI-BENCHMARK-CASES.md`;
- specifically test the specification/execution gap and retrieval-before-user-handoff behaviour;
- record model/version/date and observed failures.

CI-authored benchmark cases are **diagnostic/regression tests**. They are not, by themselves, evidence that CI is externally superior.

## Competitive proof files

- `CI-COMPETITIVE-BENCHMARK.md` — external comparison, model-control, case-origin, efficiency and claim-separation standard.
- `CI-BENCHMARK-CASES.md` — CI-authored cross-domain diagnostic/regression cases plus external-case intake requirements.
- `CI-BENCHMARK-PREREGISTRATION.md` — protocol-freeze and publish-regardless-of-outcome commitment required before scored external runs.
- `CI-BENCHMARK-JUDGE-PROTOCOL.md` — blinded external-human judging standard; LLM judge is secondary only.

These proof files do not replace runtime instructions; they test whether runtime behaviour works and whether any performance claim is actually earned.

## Alignment rule

A Chat, Work or product implementation must not claim to be the current CI Boardroom if it loads only `BOARDROOM.md` while omitting mandatory riders/hard gates that materially affect behaviour.

**Written specification is not executed behaviour.** Alignment means the current files are loaded **and** the regression tests pass.

For external performance claims, alignment also requires the current benchmark governance files above. A runtime can be operationally aligned while still having no external superiority proof.

## Change-control rule

When live use reveals a material miss:

1. classify the failure generically rather than preserving the anecdote alone;
2. update the appropriate runtime rule;
3. add or strengthen a regression case;
4. rerun affected diagnostic cases;
5. record whether behaviour actually changed;
6. if the change affects an external benchmark, increment the benchmark version and follow preregistration/change-control rules rather than silently editing the exam after seeing results.

Do not treat a GitHub commit by itself as proof that runtime behaviour has improved, and do not treat CI-authored benchmark success as proof of external superiority.