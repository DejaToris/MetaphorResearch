# manages connection to COCA website/DB
from ..WordAbstractionEvaluator.DAL_AbstractionDB import DbAccess as AbstractionDB
from collections import namedtuple

COCAResultTuple = namedtuple('QueryResult', 'run_id freq calcMI SearchCIid SearchPosType FoundCIid FoundPosType FoundWordCI spanLeft spanRight lemma')

def get_common_object_list(verb):
    # should call get_all_bigrams_for_word with both 1 and 2 spanRight
    # TODO find a clever way to combine the two lists to merge dups and order by freq
    if "testverb" == verb:
        return ["testobj1", "testobj2", "testobj3"]
    elif "testsynonym" == verb:
        return ["testobj3", "testobj4"]
    return []  # TODO connect to DB and get the verbs


def get_all_bigrams_for_word(word, spanLeft, spanRight, conn):
    # spans = size of window to look for object.
    # expected spans: Left - 0, Right - 1 or 2 (assuming Det or Adj)
    cursor = conn.cursor()
    cursor.execute("EXEC \"dbo\".\"GetNgrams\" \'{}\', \'2\', \'1\', \'{}\', \'{}\', \'0\'".format(word.lower(), spanLeft, spanRight))
    query_result = cursor.fetchall()
    if query_result:
        return parse_bigrams(query_result)
    else:
        return -1.0


def parse_bigrams(query_result):
    parsed_bigrams = []
    for item in query_result:
        parsed_bigrams.append(COCAResultTuple(*item))
    return parsed_bigrams


