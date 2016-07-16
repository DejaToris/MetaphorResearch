from unittest import TestCase

import research_tools.PrototypicalObjectVerbMatcher.ObjectsCounter
from context import research_tools


class TestMatcherMain(TestCase):
    def test_contains_letters_only(self):
        self.assertTrue(research_tools.protoobj_matcher.matcher.contains_letters_only("abcdefghijklmnOPQRSTUVWXYz"))
        self.assertFalse(research_tools.protoobj_matcher.matcher.contains_letters_only("6"))
        self.assertFalse(research_tools.protoobj_matcher.matcher.contains_letters_only("a word"))

    def test_sanitized_verb(self):
        self.assertEqual(research_tools.protoobj_matcher.matcher.sanitize_verb("CAPS"), "caps")
        with self.assertRaises(Exception) as cm:
            research_tools.protoobj_matcher.matcher.sanitize_verb("a word")
            research_tools.protoobj_matcher.matcher.sanitize_verb("w0rd")

    def test_objects_counter(self):
        o = research_tools.PrototypicalObjectVerbMatcher.ObjectsCounter.ObjectsCounter("testverb")
        self.assertEqual(o.verb, "testverb")

        o.inc_object_prototypicality("testobj2")
        o.inc_object_prototypicality("testobj2")
        o.inc_object_prototypicality("testobj3")
        result = o.get_objects_sorted_by_prototypicality()
        expected_output = [('testobj2', 2), ('testobj3', 1), ('testobj1', 0)]
        self.assertEqual(expected_output, result)

    def test_proto_calculation_algorithm(self):
        proto_objects = research_tools.protoobj_matcher.matcher.calculate_prototypical_objects("testverb", 3)
        expected_output = [('testobj3', 1), ('testobj1', 0), ('testobj2', 0)]
        self.assertEqual(expected_output, proto_objects)
