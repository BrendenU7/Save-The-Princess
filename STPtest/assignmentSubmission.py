rooms = {
        'Labyrinth': {'South': 'Wardrobe', 'North': 'Armory', 'East': 'Lab', 'West': 'Library'},
        'Wardrobe': {'North': 'Labyrinth', 'East': 'Free Range', 'item': 'Armor'},
        'Free Range': {'West': 'Wardrobe', 'item': 'Bow'},
        'Armory': {'South': 'Labyrinth', 'East': 'Blacksmith', 'item': 'Shield'},
        'Blacksmith': {'West': 'Armory', 'item': 'Sword'},
        'Lab': {'West': 'Labyrinth', 'North': 'Upper Chamber', 'item': 'Potion'},
        'Upper Chamber': {'South': 'Lab', 'item': 'Dragon'},
        'Library': {'East': 'Labyrinth', 'item': 'Scroll of Sealing'}
    }


while True:
    # Loop for the game

    show_status(current_room, inventory, rooms)
        #function to display status
    if current_room == 'Upper Chamber':
        # Checks if the player has reached 'Upper Chamber'.
        if len(inventory) == 6:
            # If the player has collected all 6 items in their inventory.
            print('The princess is saved!')
            # Winning message.
        else:
            # If the player reaches the 'Upper Chamber' without all 6 items.
            print('Game Over. The princess is doomed :(.')
            # Losing message.
        print("GG")
        # Prints (good game).
        break
        # Breaks out of the loop, ending the game.

    move = input("Enter the next move: ").strip().split()
    # Takes input from the player, removes whitespace, and splits it into words.

    move = [word.capitalize() for word in move]
    # Capitalizes the first letter of each word in the player's input.

    if not move:
        # If the input was just spaces.
        print('Invalid Input!')
        # Informs the player the input was invalid.
        continue
        # Continues to the next iteration of the loop, asking for input again.

    action = move[0]
    # Takes the first word of the input as the action.

    if action == "Exit":
        # If the action is 'Exit'.
        print('Thanks for playing!')
        # Thanks the player for playing.
        break
        # Ends the game by breaking out of the loop.

    elif action == "Go" and len(move) == 2:
        # If the action is 'Go' and there is exactly one other word in the input (the direction).
        direction = move[1]
        # Takes the second word as the direction.
        if direction in rooms[current_room]:
            # Checks if the direction is valid from the current room.
            current_room = rooms[current_room][direction]
            # Updates the current room based on the direction provided.
        else:
            print('Invalid direction!')
            # Informs the player that the direction input is invalid.

    elif action == "Get" and len(move) > 1:
        # If the action is 'Get' and there is at least one additional word (the item name).
        item_name = ' '.join(move[1:])
        # Joins the remaining words to form the item name.
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == item_name:
            # Checks if the current room contains the item and if the item matches the player's input.
            inventory.append(item_name)
            # Adds the item to the player's inventory.
            del rooms[current_room]['item']
            # Removes the item from the room.
            print(f'{item_name} retrieved!')
            # Confirms item retrieval.
            if len(inventory) == 6:
                # If all 6 items have been collected.
                print('All items collected! Proceed to the Upper Chamber.')
                # Informs the player to move to the 'Upper Chamber'.

        else:
            print('Cannot get this item!')
            # Informs the player that the item cannot be retrieved.
    else:
        print('Invalid Input!')
        # Handles any other invalid inputs.
