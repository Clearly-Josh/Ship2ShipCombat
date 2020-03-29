#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels

vessels = [Vessels.Miranda("USS Robert Scott", 10000, 1, 11.4, .2, 1), Vessels.Saber("USS Skirata", 15000, .9, 17, .2, 1)]
#v1 = Vessels.Miranda("USS Robert Scott", 10000, 1)

###########################################################################

def listAndTarget():
  print("")
  length = len(vessels)    
  for i in range(length): 
    if vessels[i].hull > 0 and i != actingVessel:
      print(i,""+vessels[i].name) 
  pewpew = eval(input("Who are we targeting? "))
  return vessels[pewpew]

def turn(actingVessel):
  print("\nThe bridge of the",vessels[actingVessel].name,"is yours.\n1. Fire Energy Weapons\n2. Launch Torpedoes\n3. Commence Repairs\n4. Status Report\n5. Scan a Vessel\n6. Maneuver\n7. Enhance System")
  orders = eval(input("\nYour orders? "))

  if orders == 1 or orders == 2:
    target = listAndTarget()
    print("Target's defenses are: ",target.defenses)

    if orders == 1:
      damage = vessels[actingVessel].energy() - target.defenses
      if damage < 0:
        damage = 0
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      if target.hull <= 0:
        oblivion(target)

    if orders == 2:
      damage = vessels[actingVessel].torpedo() - target.defenses
      target.hull = (target.hull - damage)
      print("The "+target.name+" took",damage,"damage.")
      #print(target.hull)
      if target.hull <= 0:
        oblivion(target)

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

  if orders == 5:
    subject = listAndTarget()
    print("Their hull is at",subject.hull)
    print("Their energy weapons are",subject.energyStatus)
    print("Their torpedoes are",subject.torpedoStatus)
    print("Their maneuverability is at",subject.turn)
    print("Their engines are at",subject.impulse)
    print("Their defensive rating is",subject.defenses)
  
  if orders == 6:
    vessels[actingVessel].defenses+=4

  if orders == 7:
    print("\n1. Energy Weapons\n2. Torpedoes\n3. Scanners\n4. Engines")
    orders = eval(input("\nEnhance which system? "))
    if orders == 1:
      vessels[actingVessel].enAttackMod = 15
    elif orders == 2:
      vessels[actingVessel].torpAttackMod = 15
    elif orders == 3:
      vessels[actingVessel].enAttackMod += 2
      vessels[actingVessel].torpAttackMod += 2
    elif orders == 4:
      vessels[actingVessel].turn += 1
      vessels[actingVessel].impulse += .1

def oblivion(lost):
  lostName = vessels[lost].name
  vessels.pop(lost)
  print("We mark the passing of the "+lostName+" and her crew. May God have mercy on their souls.")

### battle loop ###
battle_continue = True
actingVessel = 0

while battle_continue == True:

  turn(actingVessel)
  
  
  #need to debuff enhancements upon vessel's next turn


  if len(vessels[0]) <= 1:
    battle_continue = False
    print("The",vessels[0],"has won the fight!")

  actingVessel += 1
  if actingVessel >=2:
    actingVessel = 0
    #battle_continue = False