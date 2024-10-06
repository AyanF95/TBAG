from room import Room
from character import Enemy, Friend
from item import Item

# Rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
library = Room("Library")  # New room
secret_room = Room("Secret Room")  # Locked room

# Enemy: Dave
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave, and I totally won't eat your brain.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Enemy: Ayan
ayan = Enemy("Ayan", "A sneaky thief lurking in the shadows.")
ayan.set_conversation("I'm Ayan. Got anything shiny for me?")
ayan.set_weakness("flashlight")
ayan.inventory = ["gold coin", "diamond ring"]  # Ayan has items to steal
library.set_character(ayan)

# Friend: Lily
lily = Friend("Lily", "A friendly wizard who likes hugs.")
lily.set_conversation("Hi! Want a hug or a magical gift?")
lily.favorite_gift = "magic wand"
kitchen.set_character(lily)

# Room Descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor.")
dining_hall.set_description("A large room with ornate golden decoration.")
library.set_description("A quiet room filled with dusty bookshelves.")
secret_room.set_description("A room that seems to be locked from the inside.")

# Linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(library, "east")
library.link_room(dining_hall, "west")
library.link_room(secret_room, "north")  # Secret room is locked

# Items
key = Item("key", "A small rusty key.")
library.set_item(key)  # Place the key in the library

# Game state
inventory = []  # Player's inventory
locked_rooms = {"Secret Room": True}  # Track locked rooms

# Game loop
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    # Check for items in the room
    item = current_room.get_item()
    if item:
        print(f"You see a {item.get_name()} here.")
        command = input(f"Do you want to pick up the {item.get_name()}? (yes/no) > ").lower()
        if command == "yes":
            inventory.append(item)
            current_room.set_item(None)
            print(f"You picked up the {item.get_name()}!")

    # Check for characters in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        if isinstance(inhabitant, Enemy):
            command = input(f"What will you do? Talk/Fight/Steal/Sleep/Move? > ").lower()
            if command == "talk":
                inhabitant.talk()
            elif command == "fight":
                item = input("What will you fight with? > ")
                if inhabitant.fight(item):
                    print(f"You defeated {inhabitant.name}!")
                    current_room.set_character(None)  # Remove character if defeated
                else:
                    print(f"{inhabitant.name} defeated you.")
            elif command == "steal":
                item = inhabitant.steal()
                if item:
                    print(f"You successfully stole {item} from {inhabitant.name}!")
                else:
                    print(f"{inhabitant.name} has nothing left to steal.")
            elif command == "sleep":
                if inhabitant.put_to_sleep():
                    print(f"{inhabitant.name} has fallen asleep.")
                else:
                    print(f"{inhabitant.name} is already asleep.")
        elif isinstance(inhabitant, Friend):
            command = input(f"What will you do? Talk/Hug/Gift/Move? > ").lower()
            if command == "talk":
                inhabitant.talk()
            elif command == "hug":
                inhabitant.hug()
            elif command == "gift":
                gift = input("What gift would you like to give? > ")
                inhabitant.give_gift(gift)

    # Move to another room
    command = input("Move which direction? > ").lower()

    # Check if the current room is Library and the player wants to go to the Secret Room
    if current_room.get_name() == "Library" and command == "north":
        if "key" in [item.get_name() for item in inventory]:  # Check if player has the key
            print("You use the key to unlock the Secret Room!")
            locked_rooms["Secret Room"] = False  # Unlock the Secret Room
        else:
            print("The door to the Secret Room is locked. You need a key.")
            continue

    # Pass locked_rooms to the move method
    current_room = current_room.move(command, locked_rooms)
