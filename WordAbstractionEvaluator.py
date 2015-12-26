import json
import os
from collections import namedtuple

from DAL_AbstractionDB.DbAccess import ServerConnection

EVALUATIONS_JSON = "Evaluations.json"
INPUT_FILE = "Output.txt"

WordAbstractionValuePair = namedtuple("WordAbstractionValue", "word abstraction_value")


def get_abstraction_value_for_word(word, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT ABSTRACT_SCALE FROM PHRASE_ABSTRACT WHERE PHRASE_ABSTRACT.PHRASE='{0}'".format(word.lower()))
    query_result = cursor.fetchone()
    if query_result:
        return query_result[0]
    else:
        return -1.0


def get_non_metaphor_sets():
    with open(INPUT_FILE, 'r') as words:
        non_metaphor_sets = words.readlines()
    return non_metaphor_sets


def get_all_word_abstraction_sets(non_metaphor_sets):
    list_of_word_abstraction_sets = []
    not_found = []
    with ServerConnection("sqlsrv.cs.bgu.ac.il", "noamant", "1qa@WS") as conn:
        for non_metaphor_set in non_metaphor_sets:
            word_abstraction_set = []
            non_metaphor_words = non_metaphor_set.rsplit()
            for word in non_metaphor_words:
                abs_value = get_abstraction_value_for_word(word, conn)
                pair = WordAbstractionValuePair(word, abs_value)
                print "Paired! {0}: {1}".format(pair.word, pair.abstraction_value)
                if pair.abstraction_value == -1.0:
                    not_found.append(pair)
                word_abstraction_set.append(pair)
            list_of_word_abstraction_sets.append(word_abstraction_set)

    print "Didn't find {0} words!".format(len(not_found))
    for pair in not_found:
        print pair.word
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
