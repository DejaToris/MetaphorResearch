from unittest import TestCase
from context import research_tools


class TestMatcherMain(TestCase):
    def test_contains_letters_only(self):
        self.assertTrue(research_tools.protoobj_matcher.matcher.contains_letters_only("abcdefghijklmnOPQRSTUVWXYz"))
        self.assertFalse(research_tools.protoobj_matcher.matcher.contains_letters_only("6"))
        self.assertFalse(research_tools.protoobj_matcher.matcher.contains_letters_only("a word"))

    def test_sanitized_verb(self):
        self.assertEqual(research_tools.protoobj_matcher.matcher.sanitize_verb("CAPS"), "caps")
        self.assertRaises(research_tools.protoobj_matcher.matcher.sanitize_verb("a word"))
        self.assertRaises(research_tools.protoobj_matcher.matcher.sanitize_verb("w0rd"))

    def test_inc_object_prototypicality(self):
        o = research_tools.protoobj_matcher.matcher.ObjectsCounter("testverb")
        o.
        self.assertEqual(o.verb, "testverb")