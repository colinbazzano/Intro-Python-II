from room import Room
from player import Player
from item import Item

"""
PRINT COLORS BELOW
"""
# for error handling so it is visible to the user


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

# for prompts at the beginning


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

# for updating location prompts


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


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

# Items

items = {
    "sword": Item("sword", "A really old and rusty sword"),
    "plastic": Item("plastic", "Really? A plastic bag, even in this old cave?"),
    "money": Item("money", "A clean, crisp 5 dollar bill, nice!")
}

# Add items to rooms

room["foyer"].items = [items["sword"]]
room["overlook"].items = [items["money"]]
room["treasure"].items = [items["plastic"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# We access the room["like this"] because it is a dictionary!
player = Player(input("Please enter your name: "), room["outside"])
# print("You can go: ", player.current_room)
print("You may go: ", player.current_room.get_available_rooms())
print("You are currently: ", player.current_room.name)
print(player.current_room.description)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = ("n", "s", "e", "w")

while True:
    cmd = input("\n~~~> ")
    if cmd == "q":
        prGreen("Thank you for playing!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
        player.display_items()
    elif cmd == "i":
        player.display_inventory()
    elif cmd.startswith("get") or cmd.startswith("take"):
        cmd_word = cmd.split()
        if len(player.current_room.items) > 0 and player.current_room.show_items(cmd_word[1]):
            player.take_item(items[cmd_word[1]])
        else:
            print(f"This room doesn't have a {cmd_word[1]}")
    elif cmd.startswith("drop"):
        cmd_word = cmd.split()
        player.drop_item(cmd_word[1])
    else:
        prRed("I did not understand that command...")
