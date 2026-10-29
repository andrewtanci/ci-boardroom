"""Generate and verify the reader-facing Kernel + Boardroom text and Skill ZIP.

These downloads are distinct from the Boardroom-only engineering package.
The public Kernel lives in CI-PUBLIC-KERNEL.md and the Boardroom rules are
read directly from the canonical runtime sources, avoiding stale cut/pastes.
"""
import argparse
from io import BytesIO
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_STORED, BadZipFile

ROOT = Path(__file__).resolve().parents[1]
TEXT_PATH = ROOT / "downloads/Continuation Intelligence - Copy and Paste.txt"
ZIP_PATH = ROOT / "downloads/Continuation Intelligence - Download Skills.zip"
SUMS_PATH = ROOT / "downloads/SHA256SUMS"
RUNTIME = [
    "BOARDROOM.md",
    "CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md",
    "CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md",
    "CI-EXECUTION-HARD-GATES.md",
]
SUPPORT = [
    "START-HERE.md", "CONTINUITY-RECOVERY.md", "CHECKPOINT-TEMPLATE.md",
    "examples/continuity-recovery-example.md", "LICENSE",
]


def outputs(root=ROOT):
    version = json.loads((root / ".claude-plugin/plugin.json").read_text())["version"]
    kernel = (root / "CI-PUBLIC-KERNEL.md").read_text().strip()
    bodies = {name: (root / name).read_text().strip() for name in RUNTIME}
    if not kernel.startswith("CI KERNEL") or any(not body for body in bodies.values()):
        raise ValueError("Missing Kernel or canonical Boardroom runtime content")

    text = (
        f"CI Kernel and Boardroom {version}\n"
        "Complete portable runtime: Kernel, Boardroom and three required riders.\n"
        "These instructions cannot grant permissions, install memory or prove model reliability.\n\n"
        + kernel
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(bodies[name] for name in RUNTIME)
        + "\n"
    )

    skill = (
        "---\n"
        "name: ci-boardroom\n"
        "description: Continuation Intelligence combines the Perpetual Kernel's "
        "portable continuity instructions and CI Boardroom's evidence-grounded, "
        "human-authorised decision support.\n"
        "---\n\n"
        "# Continuation Intelligence — Kernel and Boardroom\n\n"
        "For substantial decisions, read the three bundled rider files in this order:\n"
        + "\n".join(
            f"{i}. [{name}]({name})" for i, name in enumerate(RUNTIME[1:], 1)
        )
        + f"\n\nPublic package version: {version}. "
        "These are prompts/instructions, not independent technical enforcement. "
        "Expert role simulation does not imply a real expert was consulted.\n\n---\n\n"
        + kernel
        + "\n\n---\n\n"
        + bodies[RUNTIME[0]]
        + "\n"
    )
    names_and_content = [("SKILL.md", skill.encode("utf-8"))]
    names_and_content += [
        (name, (bodies[name] + "\n").encode("utf-8")) for name in RUNTIME[1:]
    ]
    names_and_content += [(name, (root / name).read_bytes()) for name in SUPPORT]
    sums = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n"
        for name, data in names_and_content
    ).encode("ascii")
    names_and_content.append(("PACKAGE-SHA256SUMS", sums))
    members = {
        f"ci-boardroom/{name}": data for name, data in names_and_content
    }
    return text.encode("utf-8"), members


def write_zip_bytes(members):
    buf = BytesIO()
    with ZipFile(buf, "w") as z:
        for name, content in members.items():
            info = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            z.writestr(info, content)
    return buf.getvalue()


def check_zip(path, members):
    try:
        with ZipFile(path) as z:
            if set(z.namelist()) != set(members) or len(z.namelist()) != len(members):
                raise ValueError("Reader ZIP contains missing/extra/duplicate entries")
            if any(z.read(name) != data for name, data in members.items()):
                raise ValueError("Reader ZIP contents differ from generated runtime")
            if z.testzip() is not None:
                raise ValueError("Reader ZIP CRC validation failed")
    except (BadZipFile, KeyError) as error:
        raise ValueError("Reader ZIP cannot be verified") from error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text, members = outputs()
    archive = write_zip_bytes(members)
    sums = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {path.name}\n"
        for path, data in [(TEXT_PATH, text), (ZIP_PATH, archive)]
    ).encode("ascii")
    if args.check:
        if not TEXT_PATH.exists() or TEXT_PATH.read_bytes() != text:
            print("OUT OF SYNC: public Copy and Paste text")
            return 1
        if not ZIP_PATH.exists():
            print("OUT OF SYNC: public Skill ZIP")
            return 1
        try:
            check_zip(ZIP_PATH, members)
        except ValueError as error:
            print(f"OUT OF SYNC: {error}")
            return 1
        if ZIP_PATH.read_bytes() != archive:
            print("OUT OF SYNC: public Skill ZIP bytes differ from reproducible build")
            return 1
        if not SUMS_PATH.exists() or SUMS_PATH.read_bytes() != sums:
            print("OUT OF SYNC: public download SHA256SUMS")
            return 1
        print("PASS: public Kernel + Boardroom text and Skill ZIP contain current canonical runtime")
        return 0
    TEXT_PATH.parent.mkdir(parents=True, exist_ok=True)
    TEXT_PATH.write_bytes(text)
    ZIP_PATH.write_bytes(archive)
    SUMS_PATH.write_bytes(sums)
    print("Generated public Kernel + Boardroom downloads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
