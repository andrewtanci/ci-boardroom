"""Release tests: content drift, incomplete installs and failed replacement."""
import os
from pathlib import Path
import re
import subprocess
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
RIDERS = ["CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md", "CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md", "CI-EXECUTION-HARD-GATES.md"]


class DistributionTests(unittest.TestCase):
    def test_packaged_riders_match_the_canonical_runtime(self):
        for name in RIDERS:
            with self.subTest(name=name):
                path = ROOT / "skills/ci-boardroom" / name
                self.assertTrue(path.exists(), f"missing runtime file: {name}")
                self.assertEqual(path.read_bytes(), (ROOT / name).read_bytes())

    def test_one_paste_delivers_each_complete_runtime_body_in_order(self):
        path = ROOT / "BOARDROOM-PASTE.md"
        self.assertTrue(path.exists(), "complete paste bundle missing")
        text = path.read_text()
        previous = -1
        for name in ["BOARDROOM.md", *RIDERS]:
            body = (ROOT / name).read_text().strip()
            self.assertEqual(text.count(body), 1, name)
            position = text.index(body)
            self.assertGreater(position, previous)
            previous = position

    def run_installer(self, failure="", corrupt=False, replacement_failure=False, checksum_mode=""):
        with tempfile.TemporaryDirectory(prefix="ci-install-test-") as temp:
            parent = Path(temp)
            target = parent / "skills" / "ci-boardroom"
            target.mkdir(parents=True)
            (target / "previous.txt").write_text("last known good")
            bin_dir = parent / "bin"
            bin_dir.mkdir()
            # The network alone is mocked. The real documented shell block runs.
            curl = bin_dir / "curl"
            curl.write_text("#!/usr/bin/env python3\nimport os,sys,shutil\nfrom pathlib import Path\na=sys.argv[1:]\nu=next(x for x in a if x.startswith('https://'))\nn=u.rsplit('/',1)[-1]\no=a[a.index('-o')+1]\nif n==os.environ.get('FAIL_DOWNLOAD'): sys.exit(22)\ns=Path(os.environ['PACKAGE_FIXTURE'])/n\nif not s.exists(): sys.exit(22)\nshutil.copyfile(s,o)\n")
            curl.chmod(0o755)
            fixture = parent / "package"
            shutil.copytree(ROOT / "skills/ci-boardroom", fixture)
            if corrupt:
                (fixture / RIDERS[0]).write_text("corrupt download")
            sums_path = fixture / "PACKAGE-SHA256SUMS"
            sums = sums_path.read_text().splitlines(keepends=True)
            if checksum_mode == "missing":
                sums_path.write_text(sums[0])
            elif checksum_mode == "duplicate":
                sums_path.write_text("".join([*sums, sums[0]]))
            elif checksum_mode == "unexpected":
                sums_path.write_text("".join([*sums, sums[0].replace("SKILL.md", "extra.md")]))
            elif checksum_mode == "path":
                sums_path.write_text("".join(sums).replace("SKILL.md", "./SKILL.md"))
            if replacement_failure:
                mv = bin_dir / "mv"
                mv.write_text('#!/usr/bin/env bash\nif [[ "$1" == */staged ]]; then exit 1; fi\nexec /bin/mv "$@"\n')
                mv.chmod(0o755)
            env = os.environ.copy()
            env.update(PATH=str(bin_dir)+os.pathsep+env["PATH"], CI_BOARDROOM_SKILLS_DIR=str(target.parent), PACKAGE_FIXTURE=str(fixture), FAIL_DOWNLOAD=failure)
            body = re.search(r"```bash\n(.*?)\n```", (ROOT / "INSTALL.md").read_text(), re.S).group(1)
            # Substitute only the old default location so the regression never touches real skills.
            body = body.replace('$HOME/.codex/skills/ci-boardroom', str(target))
            run = subprocess.run(["bash", "-c", body + "\ninstaller_status=$?\nprintf 'PARENT_SHELL_ALIVE\\n'\nexit \"$installer_status\""], env=env, text=True, capture_output=True)
            state = {p.name: p.read_bytes() for p in target.iterdir()} if target.exists() else {}
            return run, state

    def test_failed_download_preserves_old_install_and_parent_shell(self):
        result, state = self.run_installer(RIDERS[1])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(state, {"previous.txt": b"last known good"})
        self.assertIn("PARENT_SHELL_ALIVE", result.stdout)

    def test_success_delivers_complete_package(self):
        result, state = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ["SKILL.md", *RIDERS]:
            self.assertIn(name, state)
            self.assertEqual(state[name], (ROOT / "skills/ci-boardroom" / name).read_bytes())
        self.assertNotIn("previous.txt", state)

    def test_checksum_mismatch_preserves_previous_install(self):
        result, state = self.run_installer(corrupt=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(state, {"previous.txt": b"last known good"})
        self.assertIn("PARENT_SHELL_ALIVE", result.stdout)

    def test_failed_final_move_restores_previous_install(self):
        result, state = self.run_installer(replacement_failure=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(state, {"previous.txt": b"last known good"})
        self.assertIn("PARENT_SHELL_ALIVE", result.stdout)

    def test_checksum_manifest_requires_exact_runtime_file_set(self):
        for mode in ["missing", "duplicate", "unexpected", "path"]:
            with self.subTest(mode=mode):
                result, state = self.run_installer(checksum_mode=mode, corrupt=(mode == "missing"))
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(state, {"previous.txt": b"last known good"})
                self.assertIn("PARENT_SHELL_ALIVE", result.stdout)
                self.assertIn("Invalid checksum manifest", result.stderr)

    def test_generator_rejects_incomplete_duplicate_or_malformed_load_manifest(self):
        with tempfile.TemporaryDirectory(prefix="ci-manifest-test-") as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            manifest = copy / "CI-LOAD-MANIFEST.md"
            original = manifest.read_text()
            entry = next(line for line in original.splitlines() if line.startswith("4. `CI-EXECUTION-HARD-GATES.md`"))
            variants = [original.replace(entry, ""), original + "\n" + entry, original.replace(entry, entry.replace("4. ", "- "))]
            for number, value in enumerate(variants):
                with self.subTest(variant=number):
                    manifest.write_text(value)
                    result = subprocess.run(["python3", str(copy / "scripts/sync_package.py")], capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("Invalid canonical runtime order", result.stderr)

    def test_generator_check_catches_drift_without_repairing_it(self):
        with tempfile.TemporaryDirectory(prefix="ci-generator-test-") as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            changed = copy / "skills/ci-boardroom" / RIDERS[0]
            changed.write_text("stale distribution")
            result = subprocess.run(["python3", str(copy / "scripts/sync_package.py"), "--check"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("OUT OF SYNC:", result.stdout)
            self.assertEqual(changed.read_text(), "stale distribution")
            subprocess.run(["python3", str(copy / "scripts/sync_package.py")], check=True, capture_output=True)
            self.assertEqual(changed.read_bytes(), (copy / RIDERS[0]).read_bytes())


if __name__ == "__main__":
    unittest.main()
