import argparse


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
    # go to abstraction value DB, get values, remove all below threshold, return.
    for noun in common_object_list:
        if db.get_abstrast_value(noun) > 0.5:
            common_object_list.remove(noun)
    return common_object_list


def calculate_prototypical_objects(abstract_object_list, verb_synonym_list, number_of_objects):
    # implement algorithm here

    pass


def get_prototypical_objects_for(target_verb, number_of_objects):
    common_object_list = target_verb.get_common_object_list  # or maybe WordNet can do this?
    abstract_object_list = filter_abstract_items(common_object_list)
    verb_synonym_list = nltk.get_synonym_list(target_verb)
    for synonym_verb in verb_synonym_list:
        synonym_verb.get_common_object_list()
    prototypical_object_list = calculate_prototypical_objects(abstract_object_list, verb_synonym_list, number_of_objects)


    return prototypical_object_list


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
    prototypical_objects = get_prototypical_objects_for(sanitized_verb, args.number_of_objects_to_return)
    print(prototypical_objects)


if __name__ == '__main__':
    main()
