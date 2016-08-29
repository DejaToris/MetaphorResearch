from nltk.corpus import wordnet as wn


def get_synonyms_for(verb):
    synonym_sets = wn.synsets(verb, pos=wn.VERB)
    synset_lemmas = [w.lemmas()[0].name() for w in synonym_sets]
    return [x for x in set(synset_lemmas)]
