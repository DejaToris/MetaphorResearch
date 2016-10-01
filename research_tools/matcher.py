import argparse
import pprint

from ObjectsCounter import ObjectsCounter
from synonyms import get_synonyms_for
import DbAccess as AbstractionDB
from WordAbstractionEvaluator import get_abstraction_value_for_word
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
    with AbstractionDB.get_connection(AbstractionDB.AvailableConnections.bgu) as dbConn:
        return [common_object_entry for common_object_entry in common_object_list if
                # get_abstraction_value_for_word(common_object_entry[0], dbConn) > MINIMAL_ABSTRACTION_VALUE]
                get_abstraction_value_for_word(common_object_entry[0], dbConn) < MINIMAL_ABSTRACTION_VALUE]


def calculate_prototypical_objects(target_verb):
    objects_counter = ObjectsCounter(target_verb)
    all_verbs = get_synonyms_for(target_verb) + [target_verb]
    # print 'all synonyms: ',  all_verbs
    with AbstractionDB.get_connection(AbstractionDB.AvailableConnections.bgu) as dbConn:
        for verb in all_verbs:
            common_objects = COCA.get_common_object_list(verb)
            # print 'common objects: ', common_objects
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


def crop_object_list(obj_list, crop_length):
    return obj_list[:crop_length]


def main():
    args = get_cli_arguments()
    ## sanitized_verb = sanitize_verb(args.verb)
    input_list = ('warm', 'sweet', 'deep', 'dark', 'hard')
    for word in input_list:
        sanitized_verb = sanitize_verb(word)

        proto_objs = calculate_prototypical_objects(sanitized_verb)

        proto_objs_no_abstract = filter_abstract_items(proto_objs)

        number_of_objects = args.number_of_objects_to_return
        prototypical_objects = crop_object_list(
            proto_objs_no_abstract,
            number_of_objects)

        print_results_pretty(sanitized_verb, prototypical_objects)


def print_results_pretty(verb, prototypical_objects):
    print("The verb: `{}`".format(verb))
    pprint.pprint(prototypical_objects)


if __name__ == '__main__':
    main()
