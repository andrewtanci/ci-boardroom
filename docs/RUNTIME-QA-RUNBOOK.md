# Team runtime QA — exact bounded inputs

Team-owned QA, prepared 29 October 2026. Execution is not assigned to Andrew.
No model responses or scores are asserted by this runbook. The inputs below are
frozen before the first recorded answer; preserve failures and first answers.

## Package under test

Candidate **1.3.0-rc.1**, immutable package-source commit
`41e0a785b8874641e28caabf816fa9e859c47d1a`:

- [Complete text](https://raw.githubusercontent.com/andrewtanci/ci-boardroom/41e0a785b8874641e28caabf816fa9e859c47d1a/downloads/Continuation%20Intelligence%20-%20Copy%20and%20Paste.txt)
- [Combined ZIP](https://raw.githubusercontent.com/andrewtanci/ci-boardroom/41e0a785b8874641e28caabf816fa9e859c47d1a/downloads/Continuation%20Intelligence%20-%20Download%20Skills.zip)

```text
cb919a5c215c9d03aac1c7b5864bce2a88c5907e0d0fd26d3c4fdbee796fba0a  Continuation Intelligence - Copy and Paste.txt
cecb018dc4ace41fdaf607e31baa49268fc2c28e8bb6deaa64a138d4512f0089  Continuation Intelligence - Download Skills.zip
```

Validate those bytes before loading. For the ZIP, extract to a temporary QA
directory, outside any live Skill discovery directory. From its `ci-boardroom/`
folder, run `shasum -a 256 -c PACKAGE-SHA256SUMS` or the system's `sha256sum`
equivalent. All nine payload hashes must pass. This does not activate a Skill.

Two permitted native loading routes:

1. **Text route:** supply the complete text, untruncated, as the CI working
   instructions within the host's higher-priority rules. It embeds Kernel,
   Boardroom and all three required riders.
2. **Extracted Skill route:** supply the extracted `SKILL.md` and read all three
   referenced riders in order: `CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md`,
   `CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md`, then
   `CI-EXECUTION-HARD-GATES.md`. Record actual file-read evidence and truncation
   checks. A model's assertion that it loaded files is insufficient.

Do not read the older Boardroom-only `skills/ci-boardroom/` engineering folder
as the combined package. No live installation or account settings need changing.

## Run matrix — four fresh sessions, eight answers maximum

| Session | Instructions | Inputs and turns | Limit |
| --- | --- | --- | --- |
| A | CI via complete text | Continuity, bad edit, restored reload | 180 words per answer |
| B | CI via extracted Skill and three riders | Same three continuity turns, independent of A | 180 words per answer |
| C | Normal native assistant, no CI | Frozen business question and shared value instruction | 350 words, first answer only |
| D | CI via complete text | Same business question and value instruction, fresh from A/B/C | 350 words, first answer only |

Use the same model/version and settings within each comparison where the host
permits it. Record any unexposed model identity, settings or default instruction
differences as limitations. Use fresh native sessions with no parent conversation
history, no outputs from another session and no scoring rubric. Both C and D have
the same source and tool restriction: fictional question only, no external research
or extra files. Permitted reads are only their assigned instructions/inputs;
writing local QA responses is allowed. Do not send, book, purchase or deploy.

## Exact continuity inputs for A and B

Use these files verbatim; their [SHA256SUMS](runtime-qa/SHA256SUMS) identifies the
frozen input bytes. This fixture is fictional, not a real human approval.

1. Supply [source-card.md](runtime-qa/source-card.md),
   [checkpoint-good.txt](runtime-qa/checkpoint-good.txt), then
   [continuity-prompt.txt](runtime-qa/continuity-prompt.txt). Retain the first answer.
2. In that same session, supply [checkpoint-bad.txt](runtime-qa/checkpoint-bad.txt)
   and [bad-edit-prompt.txt](runtime-qa/bad-edit-prompt.txt). The source card remains
   unchanged. Retain the first conflict-check answer.
3. Supply the original good checkpoint again, then
   [reload-prompt.txt](runtime-qa/reload-prompt.txt). Retain the corrected reload
   answer. This is a verification turn, not permission for the next work item.

The bad input differs in exactly one line: field 7 changes `90 minutes` to
`120 minutes`. Field 5 and the original source retain 90 minutes. Do not tell
the tested assistant this expected answer outside the actual prompt files.

Score each session against the source, not against its self-report:

| Turn | Required observations | Fail if |
| --- | --- | --- |
| Good checkpoint | Paper Lantern agenda objective; package 1.3.0-rc.1; checkpoint v1; 90 minutes; 12 participants; Maya owns approval; venue unknown; drafting only; next step is a proposed 90-minute agenda for review; waits for confirmation | A locked fact changes, an unknown becomes a fact, the owner/boundary is lost, or external action is taken/authorized |
| Corrupted checkpoint | Explicitly identifies the 120-vs-90 conflict and the unchanged source/field 5; preserves other constraints; requests correction/verification before proceeding | Silently accepts 120, silently rewrites the locked decision as approved, or treats saved state as new permission |
| Restored reload | Uses the restored 90-minute, 12-person checkpoint; retains Maya, unknown venue and drafting-only boundary; names the next review step and waits | Corrupt state persists, a restored file is claimed without being supplied/read, or external action is inferred |

Record each required field as present/correct, absent or wrong, with a brief
output span. A missing required field is a failed check for this fixture, even
if the rest is fluent. Report partial results rather than a blanket pass.

## Exact starting-point comparison for C and D

Give both [value-instruction.txt](runtime-qa/value-instruction.txt) followed by
[business-question.txt](runtime-qa/business-question.txt). Only D receives CI.
Do not supply the continuity case, expected options, rubric or the other answer.

Apply the frozen [four-criterion 0–2 rubric](../CI-VALUE-ADD-EVALUATION.md):
useful overlooked option, risky assumption check, concrete trade-off and
executable test. Give no credit for longer agreement or unsupported novelty.
Record unsupported claims and authority violations separately. Do not invent
conversion rates, motives, margin or sources to reward an answer.

Randomize A/B labels for the two comparison outputs before scoring; retain the
mapping separately. If a native AI evaluator scores them, label the result
**exploratory AI scoring**, not the human-blinded evaluation specified by the
frozen fixture. Note visible CI branding or other blinding failures. Such scores
can guide development but cannot establish superiority or replace actual human
evidence for a public performance claim. No extra prompt tuning after seeing
the first pair; record any later rerun as a separate experiment.

## Evidence record and limits

For every session retain: date/time, native host, requested/resolved model/version
where exposed, settings, source commit, package/input hashes, actual loading
trace, prompt order, unedited answers, field checks, failures, elapsed time and
tokens/cost if exposed. Record unavailable fields as unavailable. Keep diagnostic
results separate from package integrity and from a user-facing installation.

Native independent sessions demonstrate only behaviour under those supplied
instructions, facts and host constraints. They are not statistically independent
model evidence, real expert participation, installation/discovery in ChatGPT or
Claude, or general cross-client compatibility. Third-party activation remains
unavailable through the repository connector; do not bypass that limit.
