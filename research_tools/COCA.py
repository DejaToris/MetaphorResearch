# manages connection to COCA website/DB
import DbAccess as AbstractionDB
from collections import namedtuple
import pymssql

COCAResultTuple = namedtuple('QueryResult', 'run_id freq calcMI SearchCIid SearchPosType FoundCIid FoundPosType FoundWordCI spanLeft spanRight lemma')

def get_common_object_list(verb):
    # should call get_all_bigrams_for_word with both 1 and 2 spanRight
    # TODO find a clever way to combine the two lists to merge dups and order by freq
    with AbstractionDB.get_connection(AbstractionDB.AvailableConnections.bgu) as dbConn:
        common_objects = get_all_bigrams_for_word(verb, 0, 1, dbConn)

    return common_objects

def get_all_bigrams_for_word(word, spanLeft, spanRight, conn):
    # spans = size of window to look for object.
    # expected spans: Left - 0, Right - 1 or 2 (assuming Det or Adj)
    cursor = conn.cursor()
    cursor.execute("EXEC \"dbo\".\"GetNgrams\" \'{}\', \'2\', \'1\', \'{}\', \'{}\', \'0\'".format(word.lower(), spanLeft, spanRight))
    query_result = safe_fetch_all(cursor, word)
    return parse_bigrams(query_result)


def safe_fetch_all(cursor, word):
    try:
        query_result = cursor.fetchall()
        return query_result
    except pymssql.OperationalError as e:
        print("Couldn't fetch results for {}. Error: {}".format(word, e.message))
        return []


def parse_bigrams(query_result):
    parsed_bigrams = []
    for item in query_result:
        parsed_bigrams.append(COCAResultTuple(*item))
    return parsed_bigrams


