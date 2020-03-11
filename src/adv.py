from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# adventurer = Player("Colin", room["outside"])
# active_room = adventurer.current_room


# for error handling so it is visible to the user
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

# for prompts at the beginning


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

# for updating location prompts


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


user_name = input("What is your name? ")
player = Player(user_name, room["outside"])
prGreen(f"Welcome, {player.name}!")
prGreen("You can move by typing n, s, e, w to go in that cardinal direction.")

while True:
    prLightPurple(
        f">>> You are in: {player.current_room.name}\n>>> {player.current_room.description}")

    cmd = input(f">>> {player.name} thinks... where to next? -> ")

    if cmd == "n":
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
        else:
            prRed("*************** There's no room to the North! ***************")
    elif cmd == "s":
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
        else:
            prRed("*************** There's no room to the South! ***************")
    elif cmd == "e":
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
        else:
            prRed("*************** There's no room to the East! ***************")
    elif cmd == "w":
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
        else:
            prRed("*************** There's no room to the West! ***************")
    elif cmd == "q":
        quit()
    else:
        prRed("That is no a valid entry, try n, s, w, e, or q to quit.")

#         # * Prints the current room name
#         # * Prints the current description (the textwrap module might be useful here).
#         # * Waits for user input and decides what to do.
#         #
#         # If the user enters a cardinal direction, attempt to move to the room there.
#         # Print an error message if the movement isn't allowed.
#         #
#         # If the user enters "q", quit the game.
