from room import Room
from player import Player
from item import Treasure, LightSource, Item

# Declare all the rooms

item = {
    'key': Item('key', 'A reqular key covered in dried blood'),
    'dagger':   Item('dagger', 'A dull dagger that has a cloth wrapped around its handle'),
    'orb':  Item('orb', 'A darken orb'),
    'shard':  Item('shard', 'A shard of multicolored glass'),
    'marble':  Item('marble', 'A small glass marble with a red and orange swirls'),
    'chalice':  Item('chalice', 'A golden chalice with jewels encrusted'),
    'journal':  Item('journal', 'A leather bound journal'),
    'lamp':  Item('oil lamp', 'A silver oil lamp with only a small amount of oil left')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['marble'], item['lamp'], item['shard']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['key']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['journal']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['orb']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
    'coffin': Room("Child's Coffin", """A soft wind breezes by with a faint whisper of your name,
    dusty and half burnt children toys spread over the floor""", [item['dagger']]),
    'throne': Room("Throne Room", """Cold stone floors with a high cieling surrounds a throne in
    the long room - a faded ripped potrait hands behind the throne. It looks like a family with
    only the small eyes on a child's face is recognizable""", [item['chalice']]),
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
room['narrow'].e_to = room['coffin']
room['narrow'].s_to = room['throne']
room['coffin'].w_to = room['narrow']
room['throne'].n_to = room['narrow']


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


def has_lamp(inventory):
    is_lamp = False
    for item in inventory:
        if isinstance(item, LightSource) == True:
            is_lamp = True
    return is_lamp


while True:
    is_light = False 
    if room[account.current_room].is_light == True \
        or has_lamp(room[account.current_room].items) == True \
        or has_lamp(account.items) == True:
            is_light = True
            
    if is_light==True:
        print('\nNow in %s' % room[account.current_room].name,
            room[account.current_room].description)
        print(f'You have {account.score} moves left')

        if room[account.current_room].items == []:
            print('There is nothing for you here')
        else:
            room_items = ''
            for i in room[account.current_room].items:
                room_items += f'{i.name}, '
            print(f'You see the following items: {room_items}')
    else: 
        print('Darkness lurks - where are you?')

    if account.score == 0:
        print('Your body has perished to the poison running in your veins')
        break
    else:
        account.score -= 1
    playerAction = input('\nDecide what you will do: ').split()
    input_action = playerAction[0]

    if len(playerAction) == 1:
        if input_action in ['w', 'a', 's', 'd']:
            if input_action == "w":
                cardinal_dir = "n"
            if input_action == "a":
                cardinal_dir = "w"
            if input_action == "s":
                cardinal_dir = "s"
            if input_action == "d":
                cardinal_dir = "e"
            print('\nYou wish to switch directions')
            if is_light==False:
                print('\nStumbles in the darkness')
            able_to_travel(cardinal_dir)

        if input_action == "q" or input_action == "quit":
            goodbye = input(
                '\nAre you sure you would like to part with your memories? [Y/n]: ')
            if goodbye == "" or goodbye == "y":
                print(
                    'Farewell, your memories escape as you leave your body to its own fate')
                break
            if goodbye == "n":
                print('Wise decision traveller')
        if input_action == "i" or input_action == "inventory":
            if is_light==False:
                print('\nYou can not see what is in your bag')
            else:
                if account.items == []:
                    print('\n You open your bag and it is empty! No wonder it was so light')
                else:
                    inventory_items = ''
                    for i in account.items:
                        inventory_items += f'{i.name}'
                    print(f'\nYou open your bag and you see: {inventory_items}')

    if len(playerAction) == 2:
        input_item = playerAction[1]
        if is_light==False:
            print('\nHow can you get what you cannot see?')
        else:
            if input_action in ['get', 'take']:
                if item[input_item] in room[account.current_room].items:
                    account.items.append(item[input_item])
                    room[account.current_room].item_taken(item[input_item])
                    item[input_item].on_take()
                else:
                    print('\nWhere do you see that item?')

    elif input_action == 'drop':
        if is_light==False:
            print('\nIt is too dark to peer into your inventory ')
        else:
            if item[input_item] in account.items:
                account.items.remove(item[input_item])
                room[account.current_room].item_dropped(item[input_item])
                item[input_item].on_drop()
            else:
                print('\nItem does not exists in your inventory')
