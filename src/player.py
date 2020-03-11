# Write a class to hold player information, e.g. what room they are in
# currently.

# Player Class


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def check_room(self):
        getattr(Room, "n_to")
        print("Did this work?")
