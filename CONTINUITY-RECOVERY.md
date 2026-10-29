# Continuity & Recovery

CI helps you carry reviewed working state between chats. You save the files;
the AI does not automatically back up, sync or restore them. Keep your original
sources and a known-good copy of the CI package. An unverified summary can carry
the same mistake into a new chat.

## Save

1. At a milestone or before switching chats, ask: **full migrate**. Ask for the
   [checkpoint template](CHECKPOINT-TEMPLATE.md) fields, including the exact
   package version, artifact paths, approved decisions and approval boundaries.
2. Compare the block with your sources. Correct names, amounts, dates, versions,
   assumptions and missing information. Mark unknowns. Remove secrets and private
   material that the next assistant does not need or is not authorized to see.
3. Save the reviewed block as a dated checkpoint in storage you control. Save
   the exact draft/data/source files beside it, and retain the previous verified
   checkpoint. A link to an inaccessible file is not transferred evidence.
4. Record the package version and, where useful, file hashes or a Git commit.
   Hashes detect changed bytes; they do not prove that the content is true.

## Load and verify

1. Start a fresh chat. Load the complete combined CI package of the recorded
   version using [Start Here](START-HERE.md). Check that all content fits and
   all required riders can be read. If the host cannot read it, stop this trial
   and use a supported loading route; do not assume partial loading is complete.
2. Provide the reviewed checkpoint and the source artifacts it references.
   Place the block between the Kernel's `PASTED CI CONTINUATION BLOCK STARTS HERE`
   and `PASTED CI CONTINUATION BLOCK ENDS HERE` markers, or clearly label it as
   your reviewed continuation block when supplying it separately.
3. Ask: **Before continuing, restate the objective, package and artifact
   versions, locked decisions, human owner, uncertainties and next exact step.
   Identify missing sources and conflicts. Do not infer new external-action
   approval from the checkpoint. Wait for my correction or confirmation.**
4. Compare the response with the saved block and originals. A confident answer
   is not verification. Correct conflicts explicitly, then confirm the bounded
   next step. Preserve the old checkpoint rather than silently rewriting history.
5. Save a new checkpoint after the next meaningful change.

## Recover a bad edit with Git

Use this for a work file already tracked in your own Git repository. A checkpoint
and a Git commit preserve different things: the block records reviewed state;
Git preserves the exact tracked file bytes. Neither replaces the other.

First inspect `git status --short`, `git diff`, `git diff --cached` and the
history of the affected file. Distinguish the working file from the staged
version in Git's index. Copy the current file and checkpoint to a separate
recovery folder; if the index contains different edits, also preserve its exact
version with `git show :<path/to/file>` or a staged patch. Identify and inspect
the known-good commit and the bad edit; do not guess from a filename or choose
an arbitrary earlier commit.

For a **staged bad edit**, after saving both versions and reviewing all changes
in that path, restore the affected path in **both the index and working tree**
from the verified commit. This replaces all staged and unstaged edits in that
path, so preserve any valid work first. Replace the placeholders before running:

```bash
git show <known-good-commit>:<path/to/file>
git restore --source=<known-good-commit> --staged --worktree -- <path/to/file>
git diff -- <path/to/file>
git diff --cached -- <path/to/file>
git show :<path/to/file>
```

For an **unstaged-only bad edit**, restore only the working file from the verified
commit with `git restore --source=<known-good-commit> --worktree -- <path/to/file>`.
This leaves the index unchanged. Inspect both diffs and the staged version before
the next commit; restoring what you see in the working file alone does not prove
what Git will commit. Keep unrelated paths outside the recovery scope.

For a **committed bad edit**, use a new revert commit to retain history:

```bash
git show --stat <bad-edit-commit>
git revert --no-edit <bad-edit-commit>
```

Inspect the whole bad commit first: revert affects every change in that commit.
If it mixes valid work with the error, prepare a focused correction instead.
If there are uncommitted changes, conflicts or a merge commit, stop and inspect
before proceeding. Resolve deliberately or abort the pending revert with
`git revert --abort`; do not use a hard reset or force push as a recovery shortcut.

After restoration, compare the exact file with the known-good version, rerun the
relevant checks, and create a new checkpoint naming the recovery commit. Reload
the restored source and reviewed checkpoint in a fresh chat, then verify the
locked fields again. A Git revert does not reload any assistant automatically.

## Recover an installed CI package

1. Keep the current installation and original downloaded ZIP as separate backup
   copies before attempting an update. Record the version and download hash.
   Keep backups outside directories your app discovers as active Skills.
2. If a package is damaged, pause its use and preserve the damaged copy outside
   the active Skill location. Inspect the app's supported disable/replace flow.
3. Restore the **whole known-good package** using the app's supported import
   process, or its documented local Skill-directory replacement process. Do not
   mix `SKILL.md` from one version with riders from another. If you have no
   known-good backup, obtain a reviewed package from the main repository and
   verify its exact version; do not treat a random cached file as trusted.
4. Where local file access is available, verify every restored file from inside
   its `ci-boardroom/` directory:

   ```bash
   shasum -a 256 -c PACKAGE-SHA256SUMS
   ```

   On a system with `sha256sum`, `sha256sum -c PACKAGE-SHA256SUMS` is the
   equivalent. Require every listed file to pass and inspect for unexpected
   active runtime files. Retain the original ZIP and external download checksum
   separately; replacing a file and its hash together can hide a bad edit.
5. Reload or restart the client as its documentation requires. In a fresh chat,
   confirm the restored version and rider access, provide the reviewed checkpoint
   and exact sources, and repeat **Load and verify**. An intact package alone is
   not an installation, discovery or behavioural test pass.

The legacy Boardroom-only shell installer retains an update directory with a
`previous/` copy. Its printed path is specific to that update. Inspect that copy
before restoring it; it is not necessarily the combined reader package. See the
[engineering installation reference](https://github.com/andrewtanci/ci-boardroom/blob/main/INSTALL.md).

## Fictional drill and actual runtime checks

The [fictional workshop example](examples/continuity-recovery-example.md) has no
real customer data. The automated drill saves and reloads its checkpoint,
introduces a bad edit, detects changed bytes, reverts the Git commit, restores a
damaged extracted package from a known-good copy and checks all file hashes.
Those are **local file/Git/package checks**. They do not exercise an assistant.

Before publishing behavioural claims, run the example in two actual assistant
setups. For each, record date, app, model/version, package hash, loading route,
complete-load evidence, checkpoint response, discrepancies and corrected reload
response. Transfer only the reviewed fictional block and exact sources. Both
assistants must preserve the objective, 90-minute limit, 12-person limit, named
human owner and drafting-only boundary, and surface the unknown venue. Introduce
the stated bad edit and verify the response against the original source. Do not
score the AI's self-report as proof. Retain failures and mark unrun checks
**not run**. Passing this one case would not establish general compatibility or
comparative superiority.
