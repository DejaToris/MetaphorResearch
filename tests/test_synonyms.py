import unittest

from context import research_tools


class TestSynonyms(unittest.TestCase):
    def test_synonyms_no_source_word_in_output(self):
        TEST_WORD = "shape"
        SYNONYM_OF_TEST_WORD = u"determine"
        result_synonyms = research_tools.synonyms.get_synonyms_for(TEST_WORD)
        print("Synonyms of {}: {}".format(TEST_WORD, result_synonyms))
        self.assertIn(SYNONYM_OF_TEST_WORD, result_synonyms,
                      "{} is a synonym of {} but wasn't in the results.".format(SYNONYM_OF_TEST_WORD, TEST_WORD))
        self.assertNotIn(TEST_WORD, result_synonyms,
                         "{} wasn't filtered out of the results.".format(TEST_WORD))
