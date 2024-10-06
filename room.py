class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None  # Item placed in the room

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)
    
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("--------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    def move(self, direction, locked_rooms):
        if direction in self.linked_rooms:
            next_room = self.linked_rooms[direction]
            if next_room.get_name() in locked_rooms:
                if locked_rooms[next_room.get_name()]:
                    print(f"The door to {next_room.get_name()} is locked!")
                    return self  # Stay in the current room if locked
            return next_room  # Move to the next room
        else:
            print("You can't go that way!")
            return self  # Stay in the current room
