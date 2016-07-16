import argparse
import COCA

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
    # TODO go to abstraction value DB, get values, remove all below threshold, return.
    for noun in common_object_list:
        if db.get_abstrast_value(noun) > 0.5:
            common_object_list.remove(noun)
    return common_object_list


def calculate_prototypical_objects(target_verb):
    objects_counter = ObjectsCounter(target_verb)
    all_verbs = nltk.get_synonyms(target_verb)
    for verb in all_verbs:
        common_objects = COCA.get_common_object_list(verb)
        for obj in common_objects:
            objects_counter.inc_object_prototypicality(obj) # if exists already, +1

    return objects_counter.get_objects_sorted_by_prototypicality

class ObjectsCounter():
    def __init__(self, target_verb):
        self.verb = target_verb
        self.countable_objs = {}
        common_objs = COCA.get_common_object_list(self.verb)
        for obj in common_objs:
            self.countable_objs[obj] = 0

    def inc_object_prototypicality(self, object_word):
        if self.countable_objs.has_key(object_word):
            self.countable_objs[object_word] += 1

    def get_objects_sorted_by_prototypicality(self):
        return sorted(
            self.countable_objs.items(),    # All objects and their values
            key=lambda countable_obj: countable_obj[1], # sort by count
            reverse=True)   # sort descending
    
def calculate_prototypical_objects(abstract_object_list, verb_synonym_list, number_of_objects):
    # implement algorithm here

    pass


## def get_prototypical_objects_for(target_verb, number_of_objects):
##    common_object_list = target_verb.get_common_object_list  # or maybe WordNet can do this?
##    abstract_object_list = filter_abstract_items(common_object_list)
##    verb_synonym_list = nltk.get_synonym_list(target_verb) # TODO figure out how to get synonym list from nltk. Import nltk!
##    for synonym_verb in verb_synonym_list:
##        synonym_verb.get_common_object_list()
##    prototypical_object_list = calculate_prototypical_objects(abstract_object_list, verb_synonym_list, number_of_objects)

##    return prototypical_object_list

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
