# Implement a class to hold room information. This should have name and
# description attributes.

# Room Class
# n_to s_to e_to and w_to are directional paths from current_room to the next room


class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
