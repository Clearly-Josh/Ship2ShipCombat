#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels

v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)
v2 = Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)

#class test statements
#p1.displayShipName()
#pa=p1.attack()
#print(pa)
#p2.displayShipName()
#pa=p2.attack()
#print(pa)
#print(p2.hull)

###########################################################################

battle_continue = True

while battle_continue == True:
  print("\nThe bridge is yours, Captain.\n1. Launch Torpedoes\n2. Fire Energy Weapons\n3. Commence Repairs\n4. Status Report")
  orders = eval(input("\nYour orders? "))

  v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)
  v2 = Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)

  # Attacks by user and v1 are done simultaneously.
  if orders == 1 or orders == 2:
      damage_to_v1 = v2.attack()
      heal_self = 0
      print("You dealt",damage_to_v1,"damage.")

  if orders == 3:
      heal_self = v2.heal()
      damage_to_v1 = 0
      print("You healed",heal_self,"health points.")

  # user_health = user_health - damage_to_user + heal_self
  # v1_health = v1_health - damage_to_v1 + heal_v1


  if v1.hull <= 0 or v2.hull <= 0:
    battle_continue = False

if user_health < v1_health:

    print("\nYou lost! Better luck next time!")

else:

    print("\nYou won against v1!")