# Write a class to hold player information, e.g. what room they are in
# currently.

from item import LightSource
from game_instance import room, item
from room import Room


class Player:
    def __init__(self, name, current_room, items=[], score=21):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.score = score

    def has_lamp(self):
        is_lamp = False
        for item in self.items:
            if isinstance(item, LightSource) == True:
                is_lamp = True
        return is_lamp

    def able_to_travel(self, input_action, is_light):
        if is_light == False:
            print('\nStumbles in the darkness')
        else:
            if input_action == "w":
                cardinal_dir = "n"
            if input_action == "a":
                cardinal_dir = "w"
            if input_action == "s":
                cardinal_dir = "s"
            if input_action == "d":
                cardinal_dir = "e"

            print('\nYou wish to switch directions')
            direction_to = f'{cardinal_dir}_to'
            if getattr(room[self.current_room], direction_to) != {}:
                next_room = getattr(room[self.current_room], direction_to)
                self.current_room = list(room.keys())[
                    list(room.values()).index(next_room)]
                print('Travelling to %s' % self.current_room)
            else:
                print('Your wish is denied, there is no path in that direction')

    def player_prompt(self, is_light):
        current_room = room[self.current_room]
        if current_room.is_light == True \
                or Room.has_lamp(current_room) == True \
                or Player.has_lamp(self) == True:
            is_light = True

        if is_light == True:
            print('\nNow in %s' % current_room.name,
                  current_room.description)
            print(f'You have {self.score} moves left')

            if current_room.items == []:
                print('There is nothing for you here')
            else:
                room_items = ''
                for i in current_room.items:
                    room_items += f'{i.name}, '
                print(f'You see the following items: {room_items}')
            return True
        else:
            print('Darkness lurks - where are you?')

    def is_dead(self):
        if self.score == 0:
            print('Your body has perished to the poison running in your veins')
            return True
        else:
            self.score -= 1

    def quit_game(self):
        goodbye = input(
            '\nAre you sure you would like to part with your memories? [Y/n]: ')
        if goodbye == "" or goodbye == "y":
            print(
                'Farewell, your memories escape as you leave your body to its own fate')
            return True
        if goodbye == "n":
            print('Wise decision traveller')
            return False

    def drop_item(self, input_item, is_light):
        if is_light == False:
            print('\nIt is too dark to peer into your inventory ')
        else:
            if item[input_item] in self.items:
                self.items.remove(item[input_item])
                room[self.current_room].item_dropped(item[input_item])
                item[input_item].on_drop()
            else:
                print('\nItem does not exists in your inventory')

    def acquire_item(self, input_action, input_item, is_light):
        if is_light == False:
            print('\nHow can you get what you cannot see?')
        else:
            if input_action in ['get', 'take']:
                if item[input_item] in room[self.current_room].items:
                    self.items.append(item[input_item])
                    room[self.current_room].item_taken(item[input_item])
                    item[input_item].on_take()
                else:
                    print('\nWhere do you see that item?')

    def check_inventory(self, is_light):
        if is_light == False:
            print('\nYou can not see what is in your bag')
        else:
            if self.items == []:
                print(
                    '\n You open your bag and it is empty! No wonder it was so light')
            else:
                inventory_items = ''
                for i in self.items:
                    inventory_items += f'{i.name}, '
                    print(
                        f'\nYou open your bag and you see: {inventory_items}')

    def combine_item(self, item_one, item_two):
        if item[item_one] and item[item_two] in self.items:
            if item[item_one] and item[item_two] in [item["marble"], item["shard"]]:
                if item["lamp"] and item["orb"] in self.items:
                    self.items.remove(item[item_one])
                    self.items.remove(item[item_two])
                    self.items.remove(item["orb"])
                    self.items.append(item["glow_orb"])
                    print("You put the glass shard and the marble inside the orb and melt them together with your lamp \na whisper passes you saying 'I'm sleeping wake me up' \nThe orb illuminates with a soft warm glow ")
                else:
                    print("Nothing happened")
            else:
                print("Nothing happened")
        else:
            print('You do not own on or both items you have tried to')

    def is_it_the_end(self):
    
        if item["glow_orb"] in self.items:
            if self.current_room == "coffin":
                if item["dagger"] in self.items:
                    print('You pour the warm liquid into the well \nThe coffin shakes\nA bright light seeps out of the coffin\nThe voice of this being is of the whispers you have heard \n"Traveler - I have doubted your wit. You possess the dagger I need to switch to a physical form\nI shall follow you until I get that dagger in that possesion\nI will lift the poison the villagers gave you in hopes to prevent you from setting me free"\nA soft giggle lifted and you left to return to the kingdom ')
                    return True
                else:
                    print("You pour the warm liquid into the well \nThe coffin shakes\nA bright light seeps out of the coffin\nThe voice of this being is of the whispers you have heard \nYou see a child form grab the dagger and with unbelievable speed push the blade into your heart\nYour eyes roll back as you feel a energy rush into your body and expand\nYou continue as you watch yourself reap vicious attrocities in the village you stayed the night before\nSlashing the neck of all the children that beared the surname Smith before\nAlas slashing your own neck")
                    return True
