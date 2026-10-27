"""Validate public Kernel + Boardroom reader files and their provenance."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from scripts.build_reader_downloads import (
    ROOT, TEXT_PATH, ZIP_PATH, RUNTIME, check_zip, outputs, write_zip_bytes
)


class ReaderDistributionTests(unittest.TestCase):
    def test_public_files_reflect_canonical_runtime(self):
        text, members = outputs()
        self.assertEqual(TEXT_PATH.read_bytes(), text)
        check_zip(ZIP_PATH, members)
        self.assertIn(b"CI KERNEL", text)
        self.assertIn(b"Research-Grounded Expert Deliberation", text)
        self.assertIn(b"Gate 8", text)
        self.assertIn(b"Human Judgment", text)
        self.assertIn(b"full migrate", text)
        self.assertIn(b"1.2.0", text)

    def test_public_archive_contains_exact_files_and_hashes(self):
        text, members = outputs()
        self.assertEqual(len(members), 5)
        self.assertEqual(
            set(members),
            {f"ci-boardroom/{name}" for name in ["SKILL.md", *RUNTIME[1:], "PACKAGE-SHA256SUMS"]},
        )
        with ZipFile(ZIP_PATH) as archive:
            self.assertEqual(set(archive.namelist()), set(members))
            sums = archive.read("ci-boardroom/PACKAGE-SHA256SUMS").decode("ascii").splitlines()
            for line in sums:
                sha, name = line.split("  ", 1)
                value = archive.read(f"ci-boardroom/{name}")
                self.assertEqual(hashlib.sha256(value).hexdigest(), sha)
            skill = archive.read("ci-boardroom/SKILL.md").decode("utf-8")
            self.assertIn("Research-Grounded Expert Deliberation", skill)
            self.assertIn("CI KERNEL", skill)
            self.assertIn("full migrate", skill)

    def test_generation_is_reproducible_and_archive_validation_catches_tampering(self):
        _, members = outputs()
        generated = write_zip_bytes(members)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "reader.zip"
            path.write_bytes(generated)
            check_zip(path, members)
            altered = dict(members)
            altered["ci-boardroom/SKILL.md"] += b"stale\n"
            with self.assertRaises(ValueError):
                check_zip(path, altered)

    def test_skill_riders_match_exported_canonical_content(self):
        _, members = outputs()
        for name in RUNTIME[1:]:
            self.assertEqual(
                members[f"ci-boardroom/{name}"],
                (ROOT / name).read_text().strip().encode("utf-8") + b"\n",
            )


if __name__ == "__main__":
    unittest.main()
