import json
import os
from collections import namedtuple

EVALUATIONS_JSON = "Evaluations.json"
INPUT_FILE = "Output.txt"

WordAbstractionValuePair = namedtuple("WordAbstractionValue", "word abstraction_value")


def get_abs_value_for_word(w):
    import random
    return random.randint(1, 10)


def get_non_metaphor_sets():
    with open(INPUT_FILE, 'r') as words:
        non_metaphor_sets = words.readlines()
    return non_metaphor_sets


def get_all_word_abstraction_sets(non_metaphor_sets):
    list_of_word_abstraction_sets = []
    for non_metaphor_set in non_metaphor_sets:
        word_abstraction_set = []
        non_metaphor_words = non_metaphor_set.rsplit()
        for word in non_metaphor_words:
            abs_value = get_abs_value_for_word(word)
            word_abstraction_set.append(WordAbstractionValuePair(word, abs_value))
        list_of_word_abstraction_sets.append(word_abstraction_set)
    return list_of_word_abstraction_sets


def dump_to_json(list_of_word_abstraction_sets):
    with open(EVALUATIONS_JSON, 'w') as evaluations:
        json.dump(list_of_word_abstraction_sets, evaluations)
        print "Output file is in " + os.path.abspath(EVALUATIONS_JSON)


def main():
    non_metaphor_sets = get_non_metaphor_sets()

    list_of_word_abstraction_sets = get_all_word_abstraction_sets(non_metaphor_sets)

    dump_to_json(list_of_word_abstraction_sets)


if __name__ == "__main__":
    main()
