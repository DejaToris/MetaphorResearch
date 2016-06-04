# manages connection to COCA website/DB


verbs_with_objects = {'surge': {'campaign', 'wave', 'tension', 'power', 'flow'},
                      'arise': {'power', 'water', 'tension', '', ''}}

def get_common_object_list(verb):
    return