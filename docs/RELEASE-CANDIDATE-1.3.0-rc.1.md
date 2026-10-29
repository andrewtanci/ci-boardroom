# CI 1.3.0-rc.1 — Continuity & Recovery

Prepared 29 October 2026 for human review. **No Git tag or GitHub Release has
been published.** Stable `main` remains 1.2.0 while this candidate is reviewed.

## What changes

CI Boardroom is the main combined product home for downloads, setup, examples,
releases and stars. Kernel stays available as the historical component record.
The primary download includes Kernel, Boardroom, all three runtime riders,
short setup instructions, the 18-field checkpoint template, save/load/verify
and recovery instructions, a fictional example and the unchanged MIT licence.

The canonical public Kernel, Boardroom and riders are unchanged. The Kernel's
2026.10.28 / prepared-for-1.2.0 source label records its instruction edition;
the generated package header records the candidate version. Older Boardroom-only
engineering assets remain available and are clearly labelled. Installed and
pasted copies do not automatically update or sync.

## Exact candidate artifacts

Use the files **from this candidate branch/commit**, not a moving `main` URL:

- [Combined CI Skill ZIP](../downloads/Continuation%20Intelligence%20-%20Download%20Skills.zip?raw=true)
- [Complete copy/paste text](../downloads/Continuation%20Intelligence%20-%20Copy%20and%20Paste.txt?raw=true)
- [SHA256SUMS](../downloads/SHA256SUMS)

SHA-256 at candidate preparation:

```text
cecb018dc4ace41fdaf607e31baa49268fc2c28e8bb6deaa64a138d4512f0089  Continuation Intelligence - Download Skills.zip
cb919a5c215c9d03aac1c7b5864bce2a88c5907e0d0fd26d3c4fdbee796fba0a  Continuation Intelligence - Copy and Paste.txt
```

From `downloads/`, run `shasum -a 256 -c SHA256SUMS` (or
`sha256sum -c SHA256SUMS`). The ZIP's internal `PACKAGE-SHA256SUMS` covers all
nine payload files. These hashes detect changed bytes, not trustworthy reasoning
or authenticated provenance. Preserve a separately verified original download.

## Verification observed

On the local macOS/Python 3.9 environment, the existing 13-test baseline passed.
The candidate's 17 deterministic tests passed, including the new offline guide
coverage test and three bounded fictional recovery drills:

- `python3 scripts/sync_package.py --check` — seven generated engineering
  distribution files match canonical sources.
- `python3 scripts/build_reader_downloads.py --check` — combined text, exact
  reproducible ZIP bytes and external SHA-256 list match generated output.
- `python3 -m unittest discover -s tests -v` — 17 tests passed, including
  save/load, deliberate bad-edit detection, Git revert/reload, installed-folder
  corruption detection and complete known-good folder restoration. All recovery
  writes used temporary directories; no real user Skill was modified. A fresh
  review identified the staged-edit recovery gap: a regression reproduced the
  bad index value before the fix, then passed with index and worktree restoration.
- `unzip -t "downloads/Continuation Intelligence - Download Skills.zip"` —
  all ten ZIP entries passed CRC checks.
- JSON manifests agree on 1.3.0-rc.1; changed Markdown file links were checked.

The tests exercise files, checksums, a real local Git repository and the existing
installer with its network mocked. They **do not** establish assistant runtime
behaviour, successful activation in an AI app, automatic continuity, compatibility
across apps/models or comparative superiority. The published Accuracy/Outcome
case definitions are not observed model passes.

The [starting-point value evaluation](../CI-VALUE-ADD-EVALUATION.md) is also
prepared, **NOT RUN**. It gives a baseline and CI the same fictional business
question and scores grounded overlooked options, assumption checks, concrete
trade-offs and executable tests. It records verbose agreement, unsupported
novelty, authority failures and cost separately. No scores are asserted.

## Required before a public release

1. Andrew reviews the exact diff, package, examples, MIT licence and boundaries.
2. Run the [fictional case and relevant behavioural regressions](../CONTINUITY-RECOVERY.md)
   in two actual target assistant setups. Record app, model/version, date,
   complete-load evidence, package hash, responses, failures and corrected reload.
   **Status: NOT RUN.** The available repository tools do not provide those host
   assistant runtimes. No client installation or activation is claimed.
3. After the runtime evidence and human approval, finalize the version, regenerate
   the package/checksums and repeat integrity checks on the exact proposed commit.
4. Review and merge through the normal human-owned process. Creating a tag,
   publishing a GitHub Release and replacing external downloads remain separate
   actions; none is performed by this candidate preparation.

## Discovery metadata prepared, not applied

[SkillsNova's `#bonus` section](https://skillsnova.sg/#bonus) was verified on
29 October 2026 as the public combined CI download/setup section. Proposed
Boardroom homepage: `https://skillsnova.sg/#bonus`.

Suggested accurate topics: `ai-assistant`, `decision-support`,
`human-in-the-loop`, `context-management`, `prompt-engineering`.
The historical Kernel repository can use the main Boardroom repository as its
homepage. No topic or homepage mutation tool is exposed by the existing GitHub
connector, and no authenticated GitHub CLI is installed here. These metadata
changes were not attempted; no new credentials or permissions were requested.

Private source, paid methodology and client evidence were not imported. No
promotion, outreach, paid generation, repository archive, security-setting
change, merge, PR approval or release publication is included.
