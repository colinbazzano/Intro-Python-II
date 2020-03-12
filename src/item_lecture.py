class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        item_string = self.name
        item_string = self.description
        return item_string
    # TODO: on_take / on_drop for when user interacts with item


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 20)
