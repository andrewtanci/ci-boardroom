# CI 1.3.0-rc.2 — Interaction calibration candidate

Prepared 29 October 2026. Draft review only; no Git tag, merge or public release.
Stable `main` remains 1.2.0. This candidate supersedes rc.1 for new package review,
while all earlier candidate commits and frozen trial inputs remain available.

## Bounded change

The canonical Multi-Factor rider already requires interaction checks and
uncertainty discipline. Section 6 now clarifies the missing distinction: a
preference or untested explanation is not a proven hard constraint; a verified
infeasibility should still receive a decisive answer. Use conditional advice
and the smallest useful check when evidence is incomplete. This is one paragraph
in an existing section, not another gate, rider or test-specific answer.

The public Kernel, canonical Boardroom and other riders are unchanged. The
Kernel's source-edition/prepared-for-1.2.0 label records its instruction edition;
generated headers identify the actual rc.2 package. Both plugin manifests and
the marketplace entry identify 1.3.0-rc.2.

## Exact candidate artifacts

Use the files from the reviewed rc.2 commit, never assume a moving URL still
serves the same bytes:

- [Combined ZIP](../downloads/Continuation%20Intelligence%20-%20Download%20Skills.zip?raw=true)
- [Complete text](../downloads/Continuation%20Intelligence%20-%20Copy%20and%20Paste.txt?raw=true)
- [Download hashes](../downloads/SHA256SUMS)

```text
9e39de7a13356fabb49d140e4ac67178e70112ea9d9baa4b83f96429893a65fc  Continuation Intelligence - Copy and Paste.txt
e6fef927c227b2aa3e04096b24f378f51673ecc2b0aa2ba827cb1a8217bc6afb  Continuation Intelligence - Download Skills.zip
```

The ZIP bundles Kernel/Boardroom instructions, three riders, setup/recovery
references, the current fictional checkpoint example and MIT licence. Its
internal manifest covers all nine payload files. File integrity is separate
from model behaviour, client installation and discovery.

## Separate follow-up regression

The [interaction diagnostic v1](../CI-INTERACTION-REGRESSION.md) freezes three
fictional cases: ambiguous objection, verified impossibility and explicit
interaction. Its [four exact input files and hashes](interaction-qa/SHA256SUMS)
are new follow-up inputs; the prior starting-point question, rubric, eight
runtime-QA input files and native runbook are unchanged.

The completed matrix used nine fresh sessions: baseline, rc.1 and rc.2 for each
case, with the same 150-word instruction, evidence access and complete-text
loading route. The rubric was withheld from tested sessions, first answers were
retained, and source fidelity, calibration, useful next action and authority were
scored separately. Native AI scores are
exploratory. No numerical uplift or general superiority claim is warranted by
this small, related diagnostic.

**Runtime status: prescribed nine-session matrix completed and stopped.**
Baseline, rc.1 and rc.2 each scored 8/8 on all three fictional cases under
exploratory blinded AI grading, with no critical failure identified. The prior
overstatement did not recur under rc.1. These results do not demonstrate a
causal patch improvement, a reproducible failure repaired by rc.2, or superiority.
See the [observed-results summary](INTERACTION-REGRESSION-RESULTS-2026-10-29.md)
for controls, score interpretation and limits. The original tied business-question
experiment and its weakness remain preserved. No further runtime experiment is
authorized by this candidate status update.

## Integrity and preservation checks

- `python3 scripts/sync_package.py --check` — all seven generated engineering
  files match canonical sources.
- `python3 scripts/build_reader_downloads.py --check` — current combined text,
  exact reproducible ZIP bytes and external hashes match.
- `python3 -m unittest discover -s tests -v` — all 17 deterministic tests pass;
  these include file/Git/package recovery and are counted separately from the
  nine native assistant sessions.
- All three manifest versions, changed relative file links, ZIP CRC and internal
  and external SHA-256 values are checked before saving the candidate commit.
- Earlier source commits retain the original package bytes. The original
  question, rubric, runtime-QA input bytes and runbook are not overwritten.
  Private original evidence remains outside the public tree; no private report,
  raw trial conversation or Library identifier is bundled or uploaded.

The [rc.1 native runbook](RUNTIME-QA-RUNBOOK.md) pins its original package-source
commit `41e0a785b8874641e28caabf816fa9e859c47d1a`. Use those immutable URLs for the
prior condition. Historical relative download links may otherwise resolve to a
newer branch artifact; always verify the recorded version and hash.

## Remaining release gate

Team QA has recorded the prescribed native observations and retained failures
and ties. Andrew or the specifically authorized owner must now decide whether
to accept the bounded clarification and, separately, whether to mark the draft
ready, merge an identified commit or publish an identified artifact. No such
action is authorized by test completion; no merge, approval, tag or release has
been performed. Any further experiment also requires a separate decision.

Third-party ChatGPT/Claude installation, discovery and activation remain
unverified through the available repository connection. The new matrix exercised
complete text, not a live ZIP installation. No automatic synchronization,
general compatibility or performance-superiority claim is supported.
