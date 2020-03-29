#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels

vessels = [Vessels.Miranda("USS Robert Scott", 10000, 1, 11.4, .2, 1), Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)]
#v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)

###########################################################################

def turn(actingVessel):
  print("\nThe bridge is yours, Captain.\n1. Fire Energy Weapons\n2. Launch Torpedoes\n3. Commence Repairs\n4. Status Report\n5. Scan a Vessel\n6. Maneuver\n7. Enhance System")
  orders = eval(input("\nYour orders? "))

  if orders == 1 or orders == 2:
    print("")
    length = len(vessels)    
    for i in range(length): 
      if vessels[i].hull > 0 and i != actingVessel:
        print(i,""+vessels[i].name) 
    pewpew = eval(input("Who are we firing at? "))
    target = vessels[pewpew]
    defenses = 0
    if target.turn >= 10:
      defenses +=5
    if target.impulse >= .2:
      defenses += 2
    if target.shield >= 1:
      defenses += 10
    print("Target's defenses are: ",defenses)

    if orders == 1:
      damage = vessels[actingVessel].energy() - defenses
      if damage < 0:
        damage = 0
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      
      #example vessel kill
      #oblivion(pewpew)
    if orders == 2:
      damage = vessels[actingVessel].torpedo() - defenses
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)

  if orders == 3:
  	print("\nChpose a system to repair.\n1. Energy Weapons\n2. Torpedoes\n3. Sensors\n4. Engines\n5. The Hull")
  	orders = eval(input("\nYour orders? "))
  	heal_self = vessels[actingVessel].heal(orders)
  	

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