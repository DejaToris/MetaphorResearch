from research_tools.PrototypicalObjectVerbMatcher import COCA


class ObjectsCounter:
    def __init__(self, target_verb):
        self.verb = target_verb
        self.countable_objs = {}
        common_objs = COCA.get_common_object_list(self.verb)
        for obj in common_objs:
            self.countable_objs[obj] = 0

    def inc_object_prototypicality(self, object_word):
        if self.countable_objs.has_key(object_word):
            self.countable_objs[object_word] += 1

    def get_objects_sorted_by_prototypicality(self):
        return sorted(
            self.countable_objs.items(),  # All objects and their values
            key=lambda countable_obj: countable_obj[1],  # sort by count
            reverse=True)  # sort descending
