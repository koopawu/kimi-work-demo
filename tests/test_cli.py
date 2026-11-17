"""Tests for the command-line interface."""

import unittest
from contextlib import redirect_stdout
from io import StringIO

from kimi_work_demo.cli import main


class CliTests(unittest.TestCase):
    def test_prints_custom_greeting(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            exit_code = main(["--name", "Kimi"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "Hello, Kimi!\n")


if __name__ == "__main__":
    unittest.main()
