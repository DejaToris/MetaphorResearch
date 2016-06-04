# manages connection to COCA website/DB
# TODO make actual connection

verbs_with_objects = {'shape': ['clay', 'reality'],
                      'determine': ['truth', 'reality'],
                      'surge': ['campaign', 'wave', 'tension', 'power', 'flow'],
                      'arise': ['power', 'water', 'tension', '', '']}


def get_common_object_list(verb):
    try:
        return verbs_with_objects[verb]
    except KeyError:
        return []
