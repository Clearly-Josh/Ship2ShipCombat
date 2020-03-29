#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels

vessels = [Vessels.Miranda("USS Robert Scott", 10000, 1, 11.4, .2, 1), Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)]
#v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)

###########################################################################

def turn(actingVessel):
  print("\nThe bridge of the",vessels[actingVessel].name,"is yours.\n1. Fire Energy Weapons\n2. Launch Torpedoes\n3. Commence Repairs\n4. Status Report\n5. Scan a Vessel\n6. Maneuver\n7. Enhance System")
  orders = eval(input("\nYour orders? "))

  if orders == 1 or orders == 2:
    print("")
    length = len(vessels)    
    for i in range(length): 
      if vessels[i].hull > 0 and i != actingVessel:
        print(i,""+vessels[i].name) 
    pewpew = eval(input("Who are we firing at? "))
    target = vessels[pewpew]
    print("Target's defenses are: ",vessels[pewpew].defenses)

    if orders == 1:
      damage = vessels[actingVessel].energy() - defenses
      if damage < 0:
        damage = 0
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      if target.hull <= 0:
        oblivion(pewpew)

    if orders == 2:
      damage = vessels[actingVessel].torpedo() - defenses
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      if target.hull <= 0:
        oblivion(pewpew)

  if orders == 3:
  	#print("\nChpose a system to repair.\n1. Energy Weapons\n2. Torpedoes\n3. Sensors\n4. Engines\n5. The Hull")
  	#orders = eval(input("\nYour orders? "))
  	heal_self = vessels[actingVessel].heal(orders)
  	
  if orders == 4:
    print("The hull is at",vessels[actingVessel].hull)
    print("Energy weapons are",vessels[actingVessel].energyStatus)
    print("Torpedoes are",vessels[actingVessel].torpedoStatus)
    print("Maneuverability is at",vessels[actingVessel].turn)
    print("Engines are at",vessels[actingVessel].impulse)
    print("Our defensive rating is",vessels[actingVessel].defenses)

  if orders == 6:
    vessels[actingVessel].defenses+=2


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
    actingVessel = 0
    #battle_continue = False