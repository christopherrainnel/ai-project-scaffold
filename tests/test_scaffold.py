import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "tools" / "scaffold_project.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("scaffold_project", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scaffold = _load_module()

    def test_template_files_match_embedded_templates(self):
        template_root = REPO_ROOT / "project_templates"
        expected_paths = set(self.scaffold.FILES.keys())
        actual_paths = set(
            str(path.relative_to(template_root)).replace("\\", "/")
            for path in template_root.rglob("*")
            if path.is_file()
        )

        self.assertEqual(expected_paths, actual_paths)

        for rel_path in sorted(expected_paths):
            disk_content = (template_root / rel_path).read_text(encoding="utf-8")
            embedded_content = self.scaffold.FILES[rel_path]
            self.assertEqual(
                disk_content.rstrip("\n"),
                embedded_content.rstrip("\n"),
                msg=f"Template mismatch for {rel_path}",
            )

    def test_create_scaffold_and_skip_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            created, skipped = self.scaffold.create_scaffold(
                target_dir=target,
                project_name="demo-project",
            )
            self.assertEqual(len(created), len(self.scaffold.FILES))
            self.assertEqual(skipped, [])
            self.assertTrue((target / "README.md").exists())

            readme = (target / "README.md").read_text(encoding="utf-8")
            self.assertIn("# demo-project", readme)

            created2, skipped2 = self.scaffold.create_scaffold(
                target_dir=target,
                project_name="demo-project",
            )
            self.assertEqual(created2, [])
            self.assertEqual(len(skipped2), len(self.scaffold.FILES))


if __name__ == "__main__":
    unittest.main()
