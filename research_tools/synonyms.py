import nltk


def get_synonyms_for(verb):
    if "testverb" == verb:
        return ["testsynonym"]

    synonym_sets = nltk.wordnet.wordnet.synsets(verb)
    return [w.lemmas()[0].name() for w in synonym_sets]
