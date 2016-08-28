import argparse

from ObjectsCounter import ObjectsCounter
from synonyms import get_synonyms_for
from ..WordAbstractionEvaluator.DAL_AbstractionDB import DbAccess as AbstractionDB
from ..WordAbstractionEvaluator.WordAbstractionEvaluator import get_abstraction_value_for_word
import COCA

MINIMAL_ABSTRACTION_VALUE = 0.5


def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("verb", type=str, help="The target verb.")
    default_number_of_objects = 10
    parser.add_argument(
        "-n", "--number_of_objects_to_return", type=int, default=default_number_of_objects,
        help="Number of prototypical objects to match to the verb and return in the final list. "
             "Defaults to {0}.".format(default_number_of_objects))
    return parser.parse_args()


def filter_abstract_items(common_object_list):
    # TODO Test with the BGU connection as well.
    # TODO alter method to match the current data structure of the object_list
    with AbstractionDB.get_connection(AbstractionDB.AvailableConnections.bgu) as dbConn:
        return [noun for noun in common_object_list if
                get_abstraction_value_for_word(noun, dbConn) > MINIMAL_ABSTRACTION_VALUE]


def calculate_prototypical_objects(target_verb, amount_of_objects):
    objects_counter = ObjectsCounter(target_verb)
    all_verbs = get_synonyms_for(target_verb)
    with AbstractionDB.get_connection(AbstractionDB.AvailableConnections.bgu) as dbConn:
        for verb in all_verbs:
            common_objects = COCA.get_common_object_list(verb)
            for obj in common_objects:
                objects_counter.inc_object_prototypicality(obj.lemma)

    return objects_counter.get_objects_sorted_by_prototypicality()


def contains_letters_only(word):
    return word.isalpha()


def sanitize_verb(target_verb):
    if not contains_letters_only(target_verb):
        raise Exception("The word '{0}' is not a valid verb. Should contain letters only.".format(target_verb))
    sanitized_verb = target_verb.lower()
    return sanitized_verb


def main():
    args = get_cli_arguments()
    sanitized_verb = sanitize_verb(args.verb)
    prototypical_objects = calculate_prototypical_objects(sanitized_verb, args.number_of_objects_to_return)
    print(prototypical_objects)


if __name__ == '__main__':
    main()
