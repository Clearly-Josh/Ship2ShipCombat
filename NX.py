#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels

vessels = [Vessels.Miranda("USS Robert Scott", 10000, 1, 11.4, .2, 1), Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)]
#v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)
#v2 = Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)

#class test statements
#p1.displayShipName()
#pa=p1.attack()
#print(pa)
#p2.displayShipName()
#pa=p2.attack()
#print(pa)
#print(p2.hull)

###########################################################################

def turn(actingVessel):
  print("\nThe bridge is yours, Captain.\n1. Fire Energy Weapons\n2. Launch Torpedoes\n3. Commence Repairs\n4. Status Report\n5. Scan a Vessel")
  orders = eval(input("\nYour orders? "))

  if orders == 1 or orders == 2:
    print("")
    length = len(vessels)    
    for i in range(length): 
      if vessels[i].hull > 0:
        print(i,""+vessels[i].name) 
    pewpew = eval(input("Who are we firing at? "))
    target = vessels[pewpew]

    if orders == 1:
      damage = vessels[actingVessel].energy()
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      
      #example vessel kill
      #oblivion(pewpew)
    if orders == 2:
      damage = vessels[actingVessel].torpedo()
      target.hull = (target.hull - damage)
      print("You dealt",damage,"damage.")
      #print(target.hull)

  if orders == 3:
    heal_self = actingVessel.heal()
    print("You healed",heal_self,"health points.")

def oblivion(lost):
  lostName = vessels[lost].name
  vessels.pop(lost)
  print("We mark the passing of the "+lostName+" and her crew. May God have mercy on their souls.")

### battle loop ###
battle_continue = True
actingVessel = 0

while battle_continue == True:

  turn(actingVessel)

  #if vessels[0] <= 0
   # battle_continue = False

  actingVessel += 1
  if actingVessel >=2:
    battle_continue = False
