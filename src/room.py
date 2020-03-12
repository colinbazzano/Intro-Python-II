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

    def __str__(self):
        return_string = self.name
        return_string = "\n"
        return_string = ""
        return_string = "\n"
        return_string = self.description
        return_string = "\n"
        return_string = self.items
        return_string = f"{self.get_exits_string()}"
        return return_string

    def show_items(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
            else:
                return False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return exits
