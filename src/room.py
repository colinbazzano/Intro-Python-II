# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

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

    def __str__(self):
        return f"{self.name} \n {self.description} \nYou may go: {self.get_available_rooms()}"
