from item import Item, LightSource
from player import Player
from room import Room
from game_instance import item, room

playerName = input(
    '\nYou have awaken! \nThe cool damp ground seeps shivers into your spine as you gain consciousness. \nAs you slowly gain awareness you remember that you [Enter your name]: ')
player = Player(playerName, 'outside')
print('\nthat you %s were on a mission sent out by the king to retrieve the treasures hidden deep inside of this cave before you - \nmysteriously ... you have awaken here' % playerName)
print('\nYou choose your destiny - press w to go north, a to go west, s to go south, and d to go east\nYou may also leave this place by pressing q but you will leave your memories as well. \nYou may combine items like: combine lamp dagger')


while True:
    is_light = False
    if player.is_it_the_end() == True:
        break
    else:
        is_light = player.player_prompt(is_light)
        playerAction = input('\nDecide what you will do: ').split()
        player.is_dead()
        input_action = playerAction[0]

        if len(playerAction) == 1:
            if input_action in ['w', 'a', 's', 'd']:
                player.able_to_travel(input_action, is_light)

            if input_action == "q" or input_action == "quit":
                is_confirmed = player.quit_game()
                if is_confirmed:
                    break

            if input_action == "i" or input_action == "inventory":
                player.check_inventory(is_light)

        if len(playerAction) == 2:
            input_item = playerAction[1]
            player.acquire_item(input_action, input_item, is_light)

            if input_action == 'drop':
                player.drop_item(input_item, is_light)

        if len(playerAction) == 3:
            input_item_one = playerAction[1]
            input_item_two = playerAction[2]

            if input_action == "combine":
                player.combine_item(input_item_one, input_item_two)
