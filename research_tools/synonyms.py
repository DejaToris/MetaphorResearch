from nltk.corpus import wordnet as wn


def get_synonyms_for(source_word):
    synonym_sets = wn.synsets(source_word, pos=wn.VERB)
    synset_lemmas = [w.lemmas()[0].name() for w in synonym_sets]
    all_synonyms = [x for x in set(synset_lemmas)]
    return filter(lambda single_synonym: single_synonym != source_word, all_synonyms)
