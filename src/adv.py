from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'key': Item('key', 'A reqular key covered in dried blood'),
    'dagger':   Item('dagger', 'A dull dagger that has a cloth wrapped around its handle'),
    'orb':  Item('orb', 'A darken orb'),
    'shard':  Item('shard', 'A shard of multicolored glass'),
    'marble':  Item('marble', 'A small glass marble with a red and orange swirls'),
    'chalice':  Item('chalice', 'A golden chalice with jewels encrusted'),
    'journal':  Item('journal', 'A leather bound journal')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['marble'], item['shard']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['key'], item['chalice']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['dagger'], item['journal']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['orb'], item['chalice']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
playerName = input(
    '\nYou have awaken! \nThe cool damp ground seeps shivers into your spine as you gain consciousness. \nAs you slowly gain awareness you remember that you [Enter your name]: ')
account = Player(playerName, 'outside')
print('\nthat you %s were on a mission sent out by the king to retrieve the treasures hidden deep inside of this cave before you - \nmysteriously ... you have awaken here' % playerName)
print('\nYou choose your destiny - press w to go north, a to go west, s to go south, and d to go east\nYou may also leave this place by pressing q but you will leave your memories as well.')
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


def able_to_travel(direction):
    direction_to = f'{direction}_to'
    if getattr(room[account.current_room], direction_to) != {}:
        next_room = getattr(room[account.current_room], direction_to)
        account.current_room = list(room.keys())[
            list(room.values()).index(next_room)]
        print('Travelling to %s' % account.current_room)
    else:
        print('Your wish is denied, there is no path in that direction')


while True:

    print('\nNow in %s' % room[account.current_room].name,
          room[account.current_room].description)

    if room[account.current_room].items == []:
        print('There is nothing for you here')
    else:
        room_items = ''
        for i in room[account.current_room].items:
            room_items += f'{i.name}, '
        print(f'You see the following items: {room_items}')

    playerAction = input('\nDecide what you will do: ').split()

    if len(playerAction) == 1:
        if playerAction[0] in ['w', 'a', 's', 'd']:
            if playerAction[0] == "w":
                cardinal_dir = "n"
            if playerAction[0] == "a":
                cardinal_dir = "w"
            if playerAction[0] == "s":
                cardinal_dir = "s"
            if playerAction[0] == "d":
                cardinal_dir = "e"
            print('\nYou wish to switch directions')
            able_to_travel(cardinal_dir)

        if playerAction[0] == "q" or playerAction[0] == "quit":
            goodbye = input(
                '\nAre you sure you would like to part with your memories? [Y/n]: ')
            if goodbye == "" or goodbye == "y":
                print(
                    'Farewell, your memories escape as you leave your body to its own fate')
                break
            if goodbye == "n":
                print('Wise decision traveller')
        if playerAction[0] == "i" or playerAction[0] == "inventory":
            if account.items == []:
                print('\n You open your bag and it is empty! No wonder it was so light')
            else:
                inventory_items = ''
                for i in account.items:
                    inventory_items += f'{i.name}'
                print(f'\nYou open your bag and you see: {inventory_items}')

    if len(playerAction) == 2:
        if playerAction[0] in ['get', 'take']:
            if item[playerAction[1]] in room[account.current_room].items:
                account.items.append(item[playerAction[1]])
                room[account.current_room].item_taken(item[playerAction[1]])
                item[playerAction[1]].on_take()
            else:
                print('\nWhere do you see that item?')

    elif playerAction[0] == 'drop':
        if item[playerAction[1]] in account.items:
            account.items.remove(item[playerAction[1]])
            room[account.current_room].item_dropped(item[playerAction[1]])
            item[playerAction[1]].on_drop()
        else:
            print('\nItem does not exists in your inventory')
