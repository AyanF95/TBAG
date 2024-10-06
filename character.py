class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")
    
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight you.")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.inventory = []  # To hold items the enemy has
        self.is_asleep = False  # Track whether the enemy is asleep

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def steal(self):
        if self.inventory:  # Check if the enemy has items to steal
            return self.inventory.pop(0)  # Return the first item in the list
        else:
            return None

    def put_to_sleep(self):
        if not self.is_asleep:  # If the enemy is not already asleep
            self.is_asleep = True
            return True
        else:
            return False


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favorite_gift = None  # Friend's favorite gift

    def hug(self):
        print(f"You hug {self.name}. They smile warmly.")

    def give_gift(self, gift):
        if gift == self.favorite_gift:
            print(f"{self.name} is overjoyed! You gave them their favorite gift:")
