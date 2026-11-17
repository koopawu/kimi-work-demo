"""Tests for greeting generation."""

import unittest

from kimi_work_demo import build_greeting


class GreetingTests(unittest.TestCase):
    def test_default_name(self) -> None:
        self.assertEqual(build_greeting(), "Hello, World!")

    def test_custom_name(self) -> None:
        self.assertEqual(build_greeting("Kimi"), "Hello, Kimi!")

    def test_surrounding_whitespace_is_removed(self) -> None:
        self.assertEqual(build_greeting("  Kimi  "), "Hello, Kimi!")

    def test_blank_names_are_rejected(self) -> None:
        for name in ("", "   ", "\t\n"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                build_greeting(name)


if __name__ == "__main__":
    unittest.main()
