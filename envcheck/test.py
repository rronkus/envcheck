
import tempfile
import unittest
from pathlib import Path

from envcheck import check_files


class EnvCheckTests(unittest.TestCase):

    def test_missing_variables(self):
        with tempfile.TemporaryDirectory() as directory:
            example = Path(directory) / ".env.example"
            actual = Path(directory) / ".env"

            example.write_text("API_KEY=\nPORT=3000\n")
            actual.write_text("PORT=3000\n")

            missing, extra = check_files(example, actual)

            self.assertEqual(missing, ["API_KEY"])
            self.assertEqual(extra, [])

    def test_extra_variables(self):
        with tempfile.TemporaryDirectory() as directory:
            example = Path(directory) / ".env.example"
            actual = Path(directory) / ".env"

            example.write_text("PORT=3000\n")
            actual.write_text("PORT=3000\nDEBUG=true\n")

            missing, extra = check_files(example, actual)

            self.assertEqual(missing, [])
            self.assertEqual(extra, ["DEBUG"])


if __name__ == "__main__":
    unittest.main()
