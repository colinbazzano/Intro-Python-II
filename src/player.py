# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

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

    def display_inventory(self):
        if len(self.items) > 0:
            print("You are holding: ")
            for item in self.items:
                print(f"{item.name} - {item.description}")
        else:
            print("You aren't holding any items! You can find them in some rooms.")

    def take_item(self, item):
        if item in self.current_room.items:
            self.current_room.remove_item(item)
            self.items.append(item)
            print(f"You picked up {item.name}!")

    def drop_item(self, item_name):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
                self.current_room.add_item(item)
                print(f"You dropped {item.name}!")
            else:
                print(f"You don't have {item.name} in your inventory...")

    def display_items(self):
        if len(self.current_room.items) > 0:
            for item in self.current_room.items:
                print(f"Available Items: {item.name}")
        else:
            return

    def __str__(self):
        return f"{self.items}"
