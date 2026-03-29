import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "quick_validate.py"
SPEC = importlib.util.spec_from_file_location("quick_validate", MODULE_PATH)
quick_validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quick_validate)


class ValidateSkillTests(unittest.TestCase):
    def create_skill(self, content: str) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)

        skill_dir = Path(temp_dir.name) / "sample-skill"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text(
            textwrap.dedent(content).lstrip(),
            encoding="utf-8",
        )
        return skill_dir

    def test_validate_skill_reads_utf8_skill_files(self):
        skill_dir = self.create_skill(
            """
            ---
            name: sample-skill
            description: 含中文的 UTF-8 技能说明
            ---

            # 示例
            这里有中文内容。
            """
        )

        valid, message = quick_validate.validate_skill(skill_dir)

        self.assertTrue(valid)
        self.assertEqual(message, "Skill is valid!")

    def test_validate_skill_allows_common_optional_frontmatter_keys(self):
        skill_dir = self.create_skill(
            """
            ---
            name: obsidian-cli
            description: Skill for the official Obsidian CLI.
            version: 2.0.0
            author: adolago
            tags:
              - obsidian
              - cli
            triggers:
              - vault
            ---

            # Obsidian CLI
            """
        )

        valid, message = quick_validate.validate_skill(skill_dir)

        self.assertTrue(valid)
        self.assertEqual(message, "Skill is valid!")

    def test_validate_skill_rejects_unknown_frontmatter_keys(self):
        skill_dir = self.create_skill(
            """
            ---
            name: sample-skill
            description: Valid description
            unexpected: true
            ---

            # Sample
            """
        )

        valid, message = quick_validate.validate_skill(skill_dir)

        self.assertFalse(valid)
        self.assertIn("Unexpected key(s)", message)


if __name__ == "__main__":
    unittest.main()
