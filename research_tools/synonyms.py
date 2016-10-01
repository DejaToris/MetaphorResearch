from nltk.corpus import wordnet as wn


def get_synonyms_for(source_word):
    # TODO include hypernyms and words with a common hypernym in the synonym list.
    ## synonym_sets = wn.synsets(source_word, pos=wn.VERB)
    synonym_sets = wn.synsets(source_word, pos=wn.ADJ)
    synset_lemmas = [w.lemmas()[0].name() for w in synonym_sets]
    all_synonyms = [x for x in set(synset_lemmas)]
    ## print all_synonyms
    return filter(lambda single_synonym: single_synonym != source_word, all_synonyms)
