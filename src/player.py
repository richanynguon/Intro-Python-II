# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=[], score=20):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.score = score
