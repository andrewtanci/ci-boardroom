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
