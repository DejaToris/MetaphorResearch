import COCA


class Verb(object):
    def __init__(self, word):
        self.word = word
        self.common_objects = []

    def populate_common_objects(self):
        # TODO make sure it's sorted
        self.common_objects = COCA.get_common_object_list(self.word)

    def __repr__(self):
        return "[Verb: {0}, objs: {1}]".format(self.word, len(self.common_objects))
