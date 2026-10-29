"""Bounded fictional file/Git drills, never assistant-runtime evaluations.

All writes occur in temporary folders. No installed user Skill is touched.
"""
import hashlib
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tempfile
import unittest
from zipfile import ZipFile

from scripts.build_reader_downloads import ROOT, ZIP_PATH


class ContinuityRecoveryDrills(unittest.TestCase):
    def test_documented_restore_does_not_recommit_a_staged_bad_checkpoint(self):
        guide = (ROOT / "CONTINUITY-RECOVERY.md").read_text()
        restore = next(line for line in guide.splitlines()
                       if line.startswith("git restore --source="))
        with tempfile.TemporaryDirectory(prefix="ci-staged-recovery-") as folder:
            work = Path(folder)
            env = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}

            def git(*args):
                return subprocess.run(
                    ["git", "-c", "user.name=CI fictional fixture",
                     "-c", "user.email=ci-fixture@example.invalid",
                     "-c", "commit.gpgsign=false", *args],
                    cwd=work, env=env, text=True, capture_output=True, check=True,
                ).stdout

            git("init", "-q")
            checkpoint = work / "checkpoint.md"
            checkpoint.write_text("Duration: 90 minutes\nParticipants: 12\n")
            git("add", "checkpoint.md")
            git("commit", "-qm", "Known good fictional checkpoint")
            good = git("rev-parse", "HEAD").strip()
            checkpoint.write_text("Duration: 120 minutes\nParticipants: 12\n")
            git("add", "checkpoint.md")
            self.assertIn("+Duration: 120 minutes", git("diff", "--cached"))
            shutil.copyfile(checkpoint, work / "bad-working-copy.md")
            (work / "bad-index-copy.md").write_text(git("show", ":checkpoint.md"))
            command = restore.replace("<known-good-commit>", good).replace(
                "<path/to/file>", "checkpoint.md")
            git(*shlex.split(command)[1:])
            self.assertEqual(git("show", ":checkpoint.md"),
                             "Duration: 90 minutes\nParticipants: 12\n")
            (work / "recovery-note.md").write_text("Restored the fictional checkpoint.\n")
            git("add", "recovery-note.md")
            git("commit", "-qm", "Record recovery")
            self.assertEqual(git("show", "HEAD:checkpoint.md"),
                             "Duration: 90 minutes\nParticipants: 12\n")
            self.assertEqual(checkpoint.read_text(), "Duration: 90 minutes\nParticipants: 12\n")
            self.assertIn("120 minutes", (work / "bad-index-copy.md").read_text())

    def test_fictional_checkpoint_save_load_bad_edit_revert_reload(self):
        example = (ROOT / "examples/continuity-recovery-example.md").read_text()
        block = re.search(r"```text\n(.*?)\n```", example, re.S).group(1) + "\n"
        with tempfile.TemporaryDirectory(prefix="ci-checkpoint-drill-") as folder:
            work = Path(folder)
            env = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}

            def git(*args):
                return subprocess.run(
                    ["git", "-c", "user.name=CI fictional fixture",
                     "-c", "user.email=ci-fixture@example.invalid",
                     "-c", "commit.gpgsign=false", *args],
                    cwd=work, env=env, text=True, capture_output=True, check=True,
                ).stdout

            git("init", "-q")
            checkpoint = work / "checkpoint.md"
            checkpoint.write_text(block)
            original = checkpoint.read_bytes()
            self.assertEqual(original.decode(), block)  # saved block reloads exactly
            git("add", "checkpoint.md")
            git("commit", "-qm", "Save fictional reviewed checkpoint")
            good_commit = git("rev-parse", "HEAD").strip()
            bad = block.replace("7. Constraints and boundaries: 90 minutes;",
                                "7. Constraints and boundaries: 120 minutes;")
            checkpoint.write_text(bad)
            self.assertNotEqual(hashlib.sha256(checkpoint.read_bytes()).digest(),
                                hashlib.sha256(original).digest())
            self.assertIn("+7. Constraints and boundaries: 120 minutes;", git("diff"))
            shutil.copyfile(checkpoint, work / "bad-checkpoint-backup.md")
            git("add", "checkpoint.md")
            git("commit", "-qm", "Introduce fictional bad edit")
            bad_commit = git("rev-parse", "HEAD").strip()
            git("revert", "--no-edit", bad_commit)
            reloaded = checkpoint.read_bytes()
            self.assertEqual(reloaded, original)
            self.assertEqual(git("show", f"{good_commit}:checkpoint.md"), block)
            self.assertIn("120 minutes;", (work / "bad-checkpoint-backup.md").read_text())
            self.assertIn("90 minutes; 12 participants; beginner audience; draft only.", reloaded.decode())
            self.assertIn("Venue unknown", reloaded.decode())
            self.assertIn("Maya owns final approval; AI may draft only", reloaded.decode())
            self.assertEqual(git("rev-list", "--count", "HEAD").strip(), "3")

    def test_extracted_combined_package_bad_edit_detection_and_whole_copy_recovery(self):
        with tempfile.TemporaryDirectory(prefix="ci-package-recovery-") as folder:
            work = Path(folder)
            with ZipFile(ZIP_PATH) as archive:
                archive.extractall(work / "known-good")
            previous = work / "known-good/ci-boardroom"
            current = work / "active-skills/ci-boardroom"
            shutil.copytree(previous, current)
            hash_command = (["shasum", "-a", "256"] if shutil.which("shasum")
                            else ["sha256sum"])

            def verify():
                return subprocess.run([*hash_command, "-c", "PACKAGE-SHA256SUMS"],
                                      cwd=current, capture_output=True, text=True)

            self.assertEqual(verify().returncode, 0)
            with (current / "SKILL.md").open("a") as stream:
                stream.write("\nFictional corrupt edit\n")
            (current / "unexpected-runtime.md").write_text("fictional leftover")
            self.assertNotEqual(verify().returncode, 0)
            damaged = work / "damaged-backup"
            shutil.move(str(current), damaged)
            shutil.copytree(previous, current)
            self.assertEqual(verify().returncode, 0)
            expected = {p.relative_to(previous): p.read_bytes()
                        for p in previous.rglob("*") if p.is_file()}
            restored = {p.relative_to(current): p.read_bytes()
                        for p in current.rglob("*") if p.is_file()}
            self.assertEqual(restored, expected)
            self.assertTrue((damaged / "unexpected-runtime.md").exists())
            self.assertFalse((current / "unexpected-runtime.md").exists())


if __name__ == "__main__":
    unittest.main()
