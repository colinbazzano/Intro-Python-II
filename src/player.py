# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(
                self.current_room, f"{direction}_to")
            print("You can go: ", self.current_room)
            print("Current Room: ", self.current_room.name)
            print(self.current_room.description)
        else:
            print(
                f"{self.name} tried going that way, and walked straight into a wall...ouch!")
