# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items, is_light=False):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
        self.n_to = {}
        self.s_to = {}
        self.e_to = {}
        self.w_to = {}

    def item_dropped(self, item):
        self.items.append(item)

    def item_taken(self, item):
        self.items.remove(item)
