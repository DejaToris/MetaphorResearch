import argparse
import verb
from research_tools.WordAbstractionEvaluator.DAL_AbstractionDB import DbAccess
from research_tools.WordAbstractionEvaluator import WordAbstractionEvaluator
from nltk.corpus import wordnet


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
    filtered_objects = []
    with DbAccess.get_connection(DbAccess.AvailableConnections.test) as conn:
        for noun in common_object_list:
            if MINIMAL_ABSTRACTION_VALUE > WordAbstractionEvaluator.get_abstraction_value_for_word(noun, conn):
                filtered_objects.append(noun)
    return filtered_objects


class RatedObject(object):
    def __init__(self, word):
        self.word = word
        self.ranking = 0

    def __repr__(self):
        return "word: '{0}'\tranking: {1}".format(self.word, self.ranking)


def calculate_prototypical_objects(abstract_object_list, verb_synonym_list, number_of_objects):
    rated_objects = create_zero_ranked_object_list(abstract_object_list)

    for current_object in rated_objects:
        for synonym in verb_synonym_list:
            current_object.ranking += get_single_word_ranking(current_object.word, synonym)

    return sorted(rated_objects,
                  key=lambda obj: obj.ranking,  # Sort by commonness rating
                  reverse=True)                 # Descending


def get_single_word_ranking(word, synonym):
    try:
        # TODO how to rank? should probably be relative between 1 and 0, 0 means non-existant, 1 means the most common
        return len(synonym.common_objects) - synonym.common_objects.index(word)
    except ValueError:  # object doesn't exist in synonym
        return 0


def create_zero_ranked_object_list(abstract_object_list):
    rated_objects = [RatedObject(abs_object) for abs_object in abstract_object_list]
    return rated_objects


def get_synonym_list(target_verb):
    synonyms = wordnet.synsets(target_verb, pos=wordnet.VERB)
    synonym_verbs = []
    for synonym in synonyms:
        # TODO figure this out
        # TODO remove duplicates
        synonym_word = synonym.lemmas()[0].name()
        synonym_verbs.append(verb.Verb(synonym_word))

    return synonym_verbs


def get_prototypical_objects_for(target_verb, number_of_objects):
    target_verb = verb.Verb(target_verb)
    target_verb.populate_common_objects()
    abstract_object_list = filter_abstract_items(target_verb.common_objects)
    verb_synonym_list = get_synonym_list(target_verb.word)
    for synonym_verb in verb_synonym_list:
        synonym_verb.populate_common_objects()
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
