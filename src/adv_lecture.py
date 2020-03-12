from room_lecture import Room
from player_lecture import Player
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

# print(room["outside"].n_to.name)
# print(room["outside"].n_to.description)

# create a new player

player = Player(input("What is your name? -> "), room["outside"])

print(f"Hello, {player.name}!")
print(player.current_room)


# begin the game
valid_directions = ("n", "s", "e", "w")
# Read Eval Print Loop
while True:
    print(player.current_room.name)
    print("")
    print(player.current_room.description)
    cmd = input("\n~~> ")
    if cmd == 'q':
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    else:
        print("I did not understand that command!")
