# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def get_available_rooms(self):
        available_rooms = []
        if self.n_to is not None:
            available_rooms.append("n")
        if self.s_to is not None:
            available_rooms.append("s")
        if self.e_to is not None:
            available_rooms.append("e")
        if self.w_to is not None:
            available_rooms.append("w")
        return available_rooms

    def show_items(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
            else:
                return False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.name} \n {self.description} \nYou may go: {self.get_available_rooms()}"
