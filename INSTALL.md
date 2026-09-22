# Install CI Boardroom

**Delegate the work. Do not delegate the authority.**

CI Boardroom remains usable by copy and paste and as a reusable Skill. The complete package contains `SKILL.md`, three runtime references (including execution gates), and a checksum list. Package integrity is not proof of reliable model behaviour.

## 1. Codex Skill — complete self-contained package

Run this in Terminal:

```bash
#!/usr/bin/env bash
# Run in a subshell: failure must not close the caller's interactive shell.
(
  set -eu
  skills_dir="${CI_BOARDROOM_SKILLS_DIR:-$HOME/.codex/skills}"
  install_dir="$skills_dir/ci-boardroom"
  base_url="https://raw.githubusercontent.com/andrewtanci/ci-boardroom/main/skills/ci-boardroom"
  mkdir -p "$skills_dir"
  if [ -L "$install_dir" ] || { [ -e "$install_dir" ] && [ ! -d "$install_dir" ]; }; then
    printf '%s\n' 'Refusing to replace a symlink or non-directory installation.' >&2
    exit 1
  fi
  lock_dir="$skills_dir/.ci-boardroom-install.lock"
  mkdir "$lock_dir" || { printf '%s\n' 'Another install or an interrupted install holds the lock; inspect it before retrying.' >&2; exit 1; }
  update_dir=""
  restore_previous() {
    result=$?
    trap - EXIT HUP INT TERM
    if [ -n "$update_dir" ] && [ -d "$update_dir/previous" ] && [ ! -e "$install_dir" ]; then
      if ! mv "$update_dir/previous" "$install_dir"; then
        printf 'Restore needed: previous installation remains at %s/previous\n' "$update_dir" >&2
        result=1
      fi
    fi
    rmdir "$lock_dir" || true
    if [ "$result" -ne 0 ] && [ -n "$update_dir" ]; then
      printf 'Install failed; staged files retained at %s\n' "$update_dir" >&2
    fi
    exit "$result"
  }
  trap restore_previous EXIT
  trap 'exit 130' HUP INT TERM
  update_dir="$(mktemp -d "$skills_dir/ci-boardroom-update.XXXXXX")"
  stage_dir="$update_dir/staged"
  mkdir "$stage_dir"
  for file in SKILL.md CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md CI-EXECUTION-HARD-GATES.md PACKAGE-SHA256SUMS; do
    curl -fsSL "$base_url/$file" -o "$stage_dir/$file"
    test -s "$stage_dir/$file"
  done
  (
    cd "$stage_dir"
    # Hash tools check listed entries only; require exactly every runtime file.
    if ! awk '
      BEGIN {
        expected["SKILL.md"] = 1
        expected["CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md"] = 1
        expected["CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md"] = 1
        expected["CI-EXECUTION-HARD-GATES.md"] = 1
      }
      NF != 2 || length($1) != 64 || $1 !~ /^[0-9a-fA-F]+$/ || !($2 in expected) { bad = 1; next }
      { if (seen[$2]++) bad = 1; count++ }
      END { if (bad || count != 4) exit 1 }
    ' PACKAGE-SHA256SUMS; then
      printf '%s\n' 'Invalid checksum manifest: expected exactly four named runtime files.' >&2
      exit 1
    fi
    if command -v sha256sum >/dev/null 2>&1; then
      sha256sum -c PACKAGE-SHA256SUMS
    else
      shasum -a 256 -c PACKAGE-SHA256SUMS
    fi
  )
  if [ -d "$install_dir" ]; then mv "$install_dir" "$update_dir/previous"; fi
  mv "$stage_dir" "$install_dir"
  printf 'Installed complete CI Boardroom package at %s\n' "$install_dir"
  if [ -d "$update_dir/previous" ]; then printf 'Recoverable previous copy: %s/previous\n' "$update_dir"; fi
  printf '%s\n' 'Package integrity verified; model behavioural tests are still required.'
)
```

The block runs in a subshell, downloads and verifies all files before replacement, and retains the previous installation for recovery. A failed download or checksum leaves the previous version unchanged. A caught interruption during replacement attempts restoration; an uncatchable termination or power loss can require restoring the retained `previous` directory manually. No existing installation is deleted. Inspect the installed files, then use CI Boardroom in your compatible client. This shell route is for local Codex, not an automatic installation into ChatGPT's personal Skills directory.

## 2. Claude Code plugin

In Claude Code:

```text
/plugin marketplace add andrewtanci/ci-boardroom
/plugin install ci-boardroom@ci-boardroom
/reload-plugins
```

Then ask naturally or invoke the CI Boardroom skill.

## 3. Claude.ai custom Skill

Download all four runtime files into one folder named `ci-boardroom`:

- [SKILL.md](skills/ci-boardroom/SKILL.md)
- [Multi-Factor Reality & Outcome Rider](skills/ci-boardroom/CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md)
- [Marginal Gains, Timing & Habit Leverage Rider](skills/ci-boardroom/CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md)
- [Execution Hard Gates](skills/ci-boardroom/CI-EXECUTION-HARD-GATES.md)

The generated [checksum list](skills/ci-boardroom/PACKAGE-SHA256SUMS) can verify file consistency. It is not a digital signature or behavioural certification.

Compress the complete `ci-boardroom` folder as a ZIP, then upload the ZIP through Claude.ai's Skills interface if your account supports custom Skills.

## 4. Universal paste — works across models

1. Open [BOARDROOM-PASTE.md](BOARDROOM-PASTE.md), the complete generated bundle.
2. Copy the whole file.
3. Paste it into a compatible AI conversation or use the client's supported file-loading route. Verify that the complete content fits the client's limits; do not assume truncated text was loaded.
4. Add your task. You remain the final decision-owner.

## 5. ChatGPT and public plugin listing

The source package and Codex manifest are public in this repository. A public ChatGPT plugin/GPT listing is a separate review and publishing step and is not claimed here.

## What a Skill is

A Skill is a reusable instruction package with discovery metadata. Its core is still readable Markdown: that transparency is intentional. Compatible clients load it automatically when relevant; the universal-paste route remains available for clients that do not install Skills.

## Updates and verification

- Pasted copies do not auto-update.
- Re-run the complete Codex installation block above to update all required local package files together.
- Before relying on a new model or setup, run the published Accuracy and Outcome behavioural tests.
- Test files are regression benchmarks, not guarantees of universal performance.

Maintainers: run `python3 scripts/sync_package.py`, then `python3 scripts/sync_package.py --check` and `python3 -m unittest discover -s tests -v`. The shell block above is generated from `scripts/install_skill.sh`. Do not maintain separate manual copies.
