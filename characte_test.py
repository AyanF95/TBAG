from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("Hi im Dave and totally wont eat your brain")
dave.talk()
dave.set_weakness("cheese")
print("what will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)