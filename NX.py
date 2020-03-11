#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random

class Pokemon:

    """Blueprint for turn based Pokemon battle"""

    def __init__(self, attack_choice):

        self.__attack_choice = attack_choice


    def attack(self):

        if self.__attack_choice == 1:
            attack_points = random.randint(18,25)
            return attack_points

        elif self.__attack_choice == 2:
            attack_points = random.randint(10,35)
            return attack_points

        else:
            print("That is not a selection. You lost your turn!")

    def heal(self):

        heal_points = random.randint(18,25)
        return heal_points    

###########################################################################

user_health = 100
mew_health = 100
battle_continue = True

while battle_continue == True:
    print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
    attack_choice = eval(input("\nSelect an attack: "))

    # Mew selects an attack, but focuses on attacking if health is full.  
    if mew_health == 100:
        mew_choice = random.randint(1,2)

    else:
        mew_choice = random.randint(1,3)

    mew = Pokemon(mew_choice)
    user_pokemon = Pokemon(attack_choice)

    # Attacks by user and Mew are done simultaneously.
    if attack_choice == 1 or attack_choice == 2:
        damage_to_mew = user_pokemon.attack()
        heal_self = 0
        print("You dealt",damage_to_mew,"damage.")

    if mew_choice == 1 or mew_choice ==2:
        damage_to_user = mew.attack()
        heal_mew = 0
        print("Mew dealt", damage_to_user, "damage.")

    if attack_choice == 3:
        heal_self = user_pokemon.heal()
        damage_to_mew = 0
        print("You healed",heal_self,"health points.")

    if mew_choice == 3:
        heal_mew = mew.heal()
        damage_to_user = 0
        print("Mew healed", heal_mew, "health points.")

    user_health = user_health - damage_to_user + heal_self
    mew_health = mew_health - damage_to_mew + heal_mew

    # Pokemon health points are limited by a min of 0 and a max of 100.
    if user_health > 100:
        user_health = 100

    elif user_health <= 0:
        user_health = 0
        battle_continue = False

    if mew_health > 100:
        mew_health = 100

    elif mew_health <= 0:
        mew_health = 0
        battle_continue = False

    print("Your current health is", user_health)
    print("Mew's current health is", mew_health)

print("Your final health is", user_health)
print("Mew's final health is", mew_health)

if user_health < mew_health:

    print("\nYou lost! Better luck next time!")

else:

    print("\nYou won against Mew!")