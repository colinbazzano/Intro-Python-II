from item_lecture import Food, Egg, Item


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.strength = 100

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print("you can go:", self.current_room)
            print("Current Room:", self.current_room.name)
            # print("Items available:", self.current_room.items)
            print(self.current_room.description)
        else:
            print("You cannot move in that direction")

    def print_inventory(self):
        if len(self.items) > 0:
            print("You are holding: ")
            for item in self.items:
                print(f"{item.name} - {item.description}")
        else:
            print("You don't have any items! You can find them within rooms.")

    def __str__(self):
        return_string = self.items
        return return_string
# commands should be get/take and drop

    # def get_item(self, item):
    #     if item not in self.items:
    #         self.items.append(item)

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

    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"You cannot eat {food_item.name}")
        else:
            self.strength += food_item.calories
            print(
                f"You have eaten {food_item.name}, your strength is now {self.strength}")
            self.items.remove(food_item)
