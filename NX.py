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
  officersActed = 0
  oneDone = 0
  twoDone = 0
  threeDone = 0
  fourDone = 0
  fiveDone = 0
  sixDone = 0
  sevenDone = 0

  while officersActed <= 3:
    if officersActed == 0:
      print("\nThe bridge of the",vessels[actingVessel].name,"is yours, Captain.")
    elif officersActed == 1:
      print("\nWhat's the word from Ops, Commander?")
    elif officersActed == 2:
      print("\nReady weapons, Lietenant.")
    elif officersActed == 3:
      print("\nEngineering, we need a miracle.")
    print("\n1. Fire Energy Weapons\n2. Launch Torpedoes\n3. Commence Repairs\n4. Status Report\n5. Scan a Vessel\n6. Maneuver\n7. Enhance System")
    orders = eval(input("\nYour orders? "))

    if orders == 1 or orders == 2:
      target = listAndTarget()
      print("Target's defenses are: ",target.defenses)

      if orders == 1 and oneDone <= 1:
        damage = vessels[actingVessel].energy() - target.defenses
        if damage < 0:
          damage = 0
        target.hull = (target.hull - damage)
        print("The "+target.name+" took",damage,"damage.")
        #print(target.hull)
        if target.hull <= 0:
          oblivion(target)
        oneDone += 1

      if orders == 2 and twoDone <= 1:
        damage = vessels[actingVessel].torpedo() - target.defenses
        target.hull = (target.hull - damage)
        print("The "+target.name+" took",damage,"damage.")
        #print(target.hull)
        if target.hull <= 0:
          oblivion(target)
        twoDone += 1

    if orders == 3 and threeDone <=1:
      #print("\nChpose a system to repair.\n1. Energy Weapons\n2. Torpedoes\n3. Sensors\n4. Engines\n5. The Hull")
      #orders = eval(input("\nYour orders? "))
      heal_self = vessels[actingVessel].heal(orders)
      threeDone += 1
      
    if orders == 4 and fourDone <= 1:
      print("The hull is at",vessels[actingVessel].hull)
      print("Energy weapons are",vessels[actingVessel].energyStatus)
      print("Torpedoes are",vessels[actingVessel].torpedoStatus)
      print("Maneuverability is at",vessels[actingVessel].turn)
      print("Engines are at",vessels[actingVessel].impulse)
      print("Our defensive rating is",vessels[actingVessel].defenses)
      fourDone += 1

    if orders == 5 and fiveDone <= 1:
      subject = listAndTarget()
      print("Their hull is at",subject.hull)
      print("Their energy weapons are",subject.energyStatus)
      print("Their torpedoes are",subject.torpedoStatus)
      print("Their maneuverability is at",subject.turn)
      print("Their engines are at",subject.impulse)
      print("Their defensive rating is",subject.defenses)
      fiveDone += 1
    
    if orders == 6 and sixDone <= 0:
      vessels[actingVessel].defenses+=4
      sixDone += 1

    if orders == 7 and sevenDone <= 1:
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
      sevenDone += 1
    
    officersActed += 1

def oblivion(lost):
  lostName = vessels[lost].name
  vessels.pop(lost)
  print("We mark the passing of the "+lostName+" and her crew. May God have mercy on their souls.")

### battle loop ###
battle_continue = True
actingVessel = 0

while battle_continue == True:

  turn(actingVessel)

  if len(vessels) <= 1:
    battle_continue = False
    print("The",vessels[0],"has won the fight!")

  actingVessel += 1
  if actingVessel >=2:
    actingVessel = 0
    #battle_continue = False