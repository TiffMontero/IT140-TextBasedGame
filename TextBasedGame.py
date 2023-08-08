# Tiffany Montero

# print initial instructions
def instructions():
    print("Baking Competition: Facing the Final Judge")
    print("Collect all 5 items needed for your tres leches before facing Gordon Ramsay!")
    print("Move commands: Go South, Go North, Go East, Go West")
    print("Add item to inventory: get 'item name'")


# function for stats, updates/prints as user moves through rooms
def stats(current_room, rooms, inventory):
    print("-" * 20)
    print("You are in the {}".format(current_room))
    print("Inventory:", inventory)
    # prints only if there is an item in room
    if 'Item' in rooms[current_room]:
        print("You see: {}".format(rooms[current_room]['Item']))
    print("-" * 20)
    print("Enter your move:")


def main():
    # define an empty inventory to start game
    inventory = []

    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {
            'Dining Room': {
                'North': 'Expo Station',
                'East': 'Walk-in Cooler',
                'South': 'Terrace',
                'West': 'Host Stand'
            },
            'Host Stand': {
                'East': 'Dining Room',
                'Item': 'Secret Ingredient'
            },
            'Terrace': {
                'North': 'Dining Room',
                'Item': 'Flour'
            },
            'Expo Station': {
                'South': 'Dining Room',
                'East': 'Kitchen',
                'Item': 'Baking Pan'
            },
            'Kitchen': {
                'West': 'Expo Station',
                'South': 'Walk-in Cooler',
                'Item': 'Chantilly'
            },
            'Walk-in Cooler': {
                'North': 'Kitchen',
                'West': 'Dining Room',
                'South': 'Walk-in Freezer',
                'Item': 'Eggs'
            },
            'Walk-in Freezer': {
                'North': 'Walk-in Cooler',
            }
        }

    current_room = "Dining Room"

    while True:
        # calls stats in beginning to keep player updated
        stats(current_room, rooms, inventory)
        # take direction from user, assign to variable, and split into array
        command = input(">").split(" ")
        if len(command) > 1:
            command[1] = " ".join(command[1:])
        # update input as new variable to exclude the word "go"
        # isolated for direction command
        if command[0] == "Go" or command[0] == 'go':
            if command[1] == "South" or command[1] == "North" \
                or command[1] == "East" or command[1] == "West":
                # look for direction availability in current room
                if command[1] in rooms[current_room]:
                    current_room = rooms[current_room][command[1]]  # update current room
                    # checks if player enters final room
                    if current_room == "Walk-in Freezer":
                        if len(inventory) >= 5:
                            # prints winning line if all items have been collected
                            print("You have impressed Gordon Ramsay with your tres leches!")
                            print("Congratulations! You win!")
                            break
                        else:
                            # if length isn't 5 or more, prints losing line
                            print("Gordon Ramsay says: 'You're an idiot sandwich!'")
                            print("Game Over!")
                            break
                elif command[1] != rooms[current_room]:  # if no room in that direction
                    print("You can't go that way!")
            else:
                print("Invalid move!")
        # isolates for getting items
        elif command[0] == "Get" or command[0] == 'get':
            # check if there is an item in room
            if 'Item' in rooms[current_room]:
                # confirms item is in current room
                if command[1] == rooms[current_room]['Item']:
                    print("You retrieved {}!".format(command[1]))
                    inventory.append(command[1])  # adds item to inventory
                    del rooms[current_room]['Item']  # removes item after retrieval
                else:
                    print("Can't get {}".format(command[1]))
            else:  # error message if item not in current room
                print("Can't get {}".format(command[1]))
        else:  # for any other input, will print for invalid move
            print("Invalid move!")


# call instructions for start of game
instructions()
main()

# main gameplay
