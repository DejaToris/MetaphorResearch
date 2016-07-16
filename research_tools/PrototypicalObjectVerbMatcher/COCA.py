# manages connection to COCA website/DB


verbs_with_objects = {'surge': {'campaign', 'wave', 'tension', 'power', 'flow'},
                      'arise': {'power', 'water', 'tension', '', ''}}

def get_common_object_list(verb):
    if "testverb" == verb:
        return ["testobj1", "testobj2", "testobj3"]
    elif "testsynonym" == verb:
        return ["testobj3", "testobj4"]
    return []  # TODO connect to COCA and get the verbs