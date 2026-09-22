"""Generate distribution files from the canonical load manifest; --check never writes."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_RUNTIME = [
    "BOARDROOM.md",
    "CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md",
    "CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md",
    "CI-EXECUTION-HARD-GATES.md",
]


def outputs(root):
    manifest = (root / "CI-LOAD-MANIFEST.md").read_text()
    names = re.findall(r"^\d+\. `([^`]+\.md)`", manifest, re.M)
    if names != REQUIRED_RUNTIME:
        raise ValueError("Invalid canonical runtime order: expected the four required files exactly once")
    for name in names:
        if Path(name).name != name:
            raise ValueError("Runtime files must be repository-root Markdown files")
    version = json.loads((root / ".claude-plugin/plugin.json").read_text())["version"]
    bodies = {name: (root / name).read_bytes() for name in names}
    if not all(bodies.values()):
        raise ValueError("Empty runtime source")
    # The package remains reference-based; the paste export embeds every body.
    header = """---
name: ci-boardroom
description: Use when a user wants consequential decision support, a task-specific expert council, source and assumption challenge, real-world multi-factor comparison, marginal-gains testing, or explicit human-authority boundaries.
---

# CI Boardroom Skill

Before using the operating instructions below, read these bundled runtime files in order:
"""
    header += "\n".join(f"{i}. [{name}]({name})" for i, name in enumerate(names[1:], 1))
    header += f"\n\nPackage version: {version}\nGenerated from CI-LOAD-MANIFEST.md. Do not edit generated copies.\nThese are model instructions, not independent technical enforcement. Loading files does not establish a behavioural test pass.\n\n---\n\n"
    result = {"skills/ci-boardroom/SKILL.md": header.encode() + bodies[names[0]].rstrip() + b"\n"}
    result.update({f"skills/ci-boardroom/{name}": bodies[name] for name in names[1:]})
    sums = "".join(f"{hashlib.sha256(data).hexdigest()}  {Path(path).name}\n" for path, data in result.items())
    result["skills/ci-boardroom/PACKAGE-SHA256SUMS"] = sums.encode()
    paste = f"# CI Boardroom — Complete Paste Bundle\n\nPackage {version}. Generated from CI-LOAD-MANIFEST.md; all required runtime bodies follow in order.\nPasted copies do not auto-update. If your client truncates this file, use its supported file/Skill loading route; do not claim missing content was loaded. Behavioural performance remains model- and setup-dependent.\n\n"
    paste += "\n\n---\n\n".join(bodies[name].decode().strip() for name in names) + "\n"
    result["BOARDROOM-PASTE.md"] = paste.encode()
    install = (root / "INSTALL.md").read_text()
    shell = (root / "scripts/install_skill.sh").read_text().rstrip()
    result["INSTALL.md"] = re.sub(r"```bash\n.*?\n```", lambda _: "```bash\n" + shell + "\n```", install, count=1, flags=re.S).encode()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = outputs(ROOT)
    changed = [name for name, data in expected.items() if not (ROOT / name).exists() or (ROOT / name).read_bytes() != data]
    if args.check:
        for name in changed:
            print(f"OUT OF SYNC: {name}")
        if changed:
            return 1
        print(f"PASS: {len(expected)} generated distribution files match canonical sources")
        return 0
    for name in changed:
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(expected[name])
        print(f"Generated {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
