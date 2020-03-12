# Implement a class to hold room information. This should have name and
# description attributes.

# Room Class
# n_to s_to e_to and w_to are directional paths from current_room to the next room

# , n_to, s_to, e_to, w_to


class Room:
    n_to = None
    s_to = None
    e_to = None
    w_to = None

    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.n_to = n_to
        # self.s_to = s_to
        # self.e_to = e_to
        # self.w_to = w_to

    def __str__(self):
        return f"{self.name} \n {self.description}"
