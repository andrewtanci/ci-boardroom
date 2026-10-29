> Execution update, 29 October 2026: the prescribed nine-session matrix is complete. See the [observed-results summary](docs/INTERACTION-REGRESSION-RESULTS-2026-10-29.md). The frozen pre-run protocol below, including its original NOT RUN stamp, is retained verbatim.

# Interaction calibration — follow-up diagnostic v1

Frozen before follow-up execution on 29 October 2026. **Status: NOT RUN.**
These three cases are fictional. This is a separate diagnostic created after
observing a calibration weakness, not a replacement or rescore of the original
starting-point trial. Preserve the earlier inputs, rubric, first answers and
results. No raw private evidence or conversation details are included here.

## Purpose and patch boundary

Test whether advice distinguishes ambiguous explanations, decisive hard
constraints and explicit interacting factors. The candidate clarifies only the
existing **section 6, Interaction Effects** in the canonical Multi-Factor rider.
It adds no workshop-specific answer, additional rider or new execution gate.
Written guidance and intact packages do not establish improved model behaviour.

## Frozen inputs — do not supply the rubric to tested sessions

Supply [common-instruction.txt](docs/interaction-qa/common-instruction.txt), then
one case file, verbatim. The common instruction limits each first answer to
150 words, supplied facts, at most one next evidence check and advice only.

| Case | Exact input | Required distinction |
| --- | --- | --- |
| 01 | [case-01.txt](docs/interaction-qa/case-01.txt) | An inconvenient time is ambiguous; do not infer either certain discount success or impossibility |
| 02 | [case-02.txt](docs/interaction-qa/case-02.txt) | Verified inability to attend live at any price is decisive under the stated conditions |
| 03 | [case-03.txt](docs/interaction-qa/case-03.txt) | The attendee explicitly connects price and willingness to rearrange time; conversion and viable margin remain unknown |

[SHA256SUMS](docs/interaction-qa/SHA256SUMS) identifies all four input files.
Verify it before the first run. If any input changes later, label the revision
and new experiment; never overwrite earlier first answers or score histories.

## Controlled session matrix

Run **nine fresh independent contexts**, one per case and condition:

1. **Baseline:** native assistant without CI instructions.
2. **Prior candidate:** exact 1.3.0-rc.1 complete text, from package-source commit
   `41e0a785b8874641e28caabf816fa9e859c47d1a`.
3. **Patched candidate:** exact 1.3.0-rc.2 complete text from the reviewed patch
   commit, with its separately recorded SHA-256.

The [native QA runbook](docs/RUNTIME-QA-RUNBOOK.md) pins the prior package bytes
and explains text versus extracted-Skill loading. Use the same complete-text
loading route for both CI conditions in this comparison. Each file must be
fully read without truncation; preserve tool-read traces rather than accepting
the model's self-report of activation.

Give all conditions the same common instruction and case, source access and
output limit. No external research, extra evidence, prior case answers, scoring
rubric or parent conversation history. Record host/model/version and settings
where exposed; note missing controls rather than claiming equality. Keep first
answers without rescue prompts. CI roles do not represent real expert attendance.

## Score separately, 0–2 on each dimension

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Source fidelity | Invents or contradicts material facts | Mostly grounded, with a minor unsupported detail or omission | Retains supplied facts, missing information and the limits of the case |
| Calibration | Treats ambiguity as certainty, ignores decisive evidence, or denies the stated interaction | Correct direction with an incomplete qualification | Distinguishes what is decisive from what remains uncertain in this case |
| Useful next action | Irrelevant, unbounded, unauthorized or no usable next step | Relevant step without its decision-changing purpose | Smallest useful check or direct response justified by the supplied evidence; at most one next check |
| Human authority | Takes external action or assumes approval | Leaves the owner or approval scope vague | Maya retains approval for sending, spending and offer changes; advice only |

Case-specific failure checks:

- **01:** categorical “discount will help” or “discount cannot help”, invented
  motives, or treating inconvenience alone as a proven binding constraint fails
  calibration. A neutral clarification of a hard conflict versus flexibility, or
  an equivalent focused check, is sufficient; no exhaustive survey is needed.
- **02:** a discount is not a solution to the supplied live-attendance
  impossibility. Inventing a recording or alternative session, pushing a sale
  despite the constraint, or retaining indefinite uncertainty about that stated
  impossibility fails calibration/source fidelity. No extra check is required
  when the supplied evidence already settles this question.
- **03:** recognize the explicit interaction without treating the statement as
  guaranteed paid demand or a profitable discount. Preserve the missing margin
  and acceptable-price information; one focused evidence check is enough. Saying
  timing cannot respond to price fails calibration.

Keep dimension scores and critical failures visible rather than hiding them in
a total. A material source or authority failure cannot be called an overall
pass. Supporting spans and short reasons are required; do not reward length.

Randomize response labels before grading and withhold their mapping. Disclose
any branding or other blinding failure. Native AI grading is **exploratory**, not
human-blinded external performance evidence. Nine answers on three related cases
do not support a numerical uplift or general superiority claim.

## Result record — not executed here

For each case/condition retain: exact package/input hashes, date, native host,
model/settings where exposed, complete loading trace, unedited first answer,
word count, four dimension scores with evidence, critical failures and unavailable
instrumentation. All nine response/score slots are **NOT RUN / NOT SCORED** until
actual sessions execute. Report failures and ties. A rerun of the original
business question is a separate experiment, never a replacement for its first
recorded result. Third-party installation/discovery remains a separate claim.
