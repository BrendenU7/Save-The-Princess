#BRENDEN UZUEGBU

def show_instructions():
    print("Save the Princess MiniGame")
    print("Collect 6 items to win the game or the princess is doomed!")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'Item name'")

def show_status(current_room, inventory, rooms):
    print("--------------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    print("--------------------------------")

    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

def main():
    inventory = []
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
    current_room = 'Labyrinth'

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        if current_room == 'Upper Chamber':
            if len(inventory) == 6:
                print('The princess is saved!')
            else:
                print('Game Over. The princess is doomed :(.')
            print("GG")
            break

        move = input("Enter the next move: ").strip().split()
        move = [word.capitalize() for word in move]

        if not move:
            print('Invalid Input!')
            continue

        action = move[0]
        if action == "Exit":
            print('Thanks for playing!')
            break
        elif action == "Go" and len(move) == 2:
            direction = move[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print('Invalid direction!')
        elif action == "Get" and len(move) > 1:
            item_name = ' '.join(move[1:])
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == item_name:
                inventory.append(item_name)
                del rooms[current_room]['item']
                print(f'{item_name} retrieved!')
                if len(inventory) == 6:
                    print('All items collected! Proceed to the Upper Chamber.')
            else:
                print('Cannot get this item!')
        else:
            print('Invalid Input!')

if __name__ == "__main__":
    main()
