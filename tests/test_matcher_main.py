from unittest import TestCase

import research_tools.ObjectsCounter
from context import research_tools


class TestMatcherMainUtilityFunctions(TestCase):
    def test_contains_letters_only(self):
        self.assertTrue(research_tools.matcher.contains_letters_only("abcdefghijklmnOPQRSTUVWXYz"))
        self.assertFalse(research_tools.matcher.contains_letters_only("6"))
        self.assertFalse(research_tools.matcher.contains_letters_only("a word"))

    def test_sanitized_verb(self):
        self.assertEqual(research_tools.matcher.sanitize_verb("CAPS"), "caps")
        with self.assertRaises(Exception) as cm:
            research_tools.matcher.sanitize_verb("a word")
            research_tools.matcher.sanitize_verb("w0rd")
