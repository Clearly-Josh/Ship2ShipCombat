#a great deal of credit to: https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python?rq=1

import random
import Vessels
import time

vessels = [Vessels.Dhelan("Gates"), Vessels.Miranda("USS Sitting Duck")]
# calculate everybody's initial defensive rating
length = len(vessels)    
for i in range(length):
  vessels[i].defenses = Vessels.calcDefenses(vessels[i])

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
  #reset for turn
  officersActed = 0
  oneDone = 0
  twoDone = 0
  threeDone = 0
  fourDone = 0
  fiveDone = 0
  sixDone = 0
  sevenDone = 0
  enOffline = 0
  torpOffline = 0
  shieldOffline = 0
  vessels[actingVessel].maneuverBonus = 0

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
      precision = eval(input("\nTarget 1. Their Hull or 2. A System? "))
      if precision == 2:
        if orders == 1:
          oneDone += 1
        if orders == 2:
          twoDone += 2
        targetSys = eval(input("1. Energy Weapons\n2. Torpedoes\n3. Shields\n4. Engines\n\nTarget which system? "))
        if enOffline == 1 or torpOffline == 1 or shieldOffline == 1:
          if targetSys == 1:
            print("Their energy weapons are down!")
            target.energyStatus = "**Offline**"
            target.enAttackMod = -1000
          elif targetSys == 2:
            print("Their torpedoes are down!")
            target.torpedoStatus = "**Offline**"
            target.torpAttackMod = -1000
          elif targetSys == 3:
            print("Their shields are down!")
            target.shieldStatus = "**Offline**"
            target.shield = 0
        elif enOffline == 0 or torpOffline == 0 or shieldOffline == 0:
          if targetSys == 4:
            print("Their engines have been damaged.")
            target.turn -= 2
            target.impulse -= .1
          else:
            print("Target hit! One more ought to take it out.")
            if targetSys == 1:
              enOffline += 1
            elif targetSys == 2:
              torpOffline += 1
            elif targetSys == 3:
              shieldOffline += 1
      else:
        if orders == 1:
          if vessels[actingVessel].energyStatus == "**Offline**":
            print("We can't fire!")
            officersActed -= 1
          elif oneDone > 1:
              print("That's as fast as they can fire, sir.")
              officersActed -= 1
          else:
            print("Firing.")
            damage = random.randint(vessels[actingVessel].enBase,vessels[actingVessel].enMax) + vessels[actingVessel].enAttackMod - target.defenses
            if damage < 0:
              damage = 0
            target.hull = (target.hull - damage)
            time.sleep(1)
            print("The "+target.name+" took",damage,"damage.")
            time.sleep(1)
            #print(target.hull)
            if target.hull <= 0:
              oblivion(actingVessel)
            oneDone += 1

        if orders == 2:
          if vessels[actingVessel].torpedoStatus == "**Offline**":
            print("The launchers are inoperable, sir!")
            officersActed -= 1
          elif twoDone > 1:
            print("We need a few more seconds to reload, sir!")
            officersActed -= 1
          else:
            print("Torpedoes away.")
            damage = random.randint(vessels[actingVessel].torpBase,vessels[actingVessel].torpMax) + vessels[actingVessel].torpAttackMod - target.defenses
            target.hull = (target.hull - damage)
            time.sleep(1)
            print("The "+target.name+" took",damage,"damage.")
            time.sleep(1)
            #print(target.hull)
            if target.hull <= 0:
              lost = vessels.index(target)
              oblivion(lost)
            twoDone += 2

    if orders == 3:
      if threeDone > 1:
        print("That's all we can do short of pulling into drydock.")
        officersActed -= 1
      else:
        precision = eval(input("Repair 1. Our Hull or 2. A System? "))
        if precision == 2:
          targetSys = eval(input("1. Energy Weapons\n2. Torpedoes\n3. Shields\n4. Engines\n\nTarget which system? "))

          if targetSys == 1:
            print("The energy weapons are back up!")
            vessels[actingVessel].energyStatus = "Online"
            vessels[actingVessel].enAttackMod = 0
          elif targetSys == 2:
            print("We have torpedoes!")
            vessels[actingVessel].torpedoStatus = "Online"
            vessels[actingVessel].torpAttackMod = 0
          elif targetSys == 3:
            print("Shields are back!")
            vessels[actingVessel].shieldStatus = "Online"
            vessels[actingVessel].shield = vessels[actingVessel].shieldMax
          elif targetSys == 4:
            print("We're moving again.")
            vessels[actingVessel].turn += 2
            vessels[actingVessel].impulse += .1
          time.sleep(2)
          threeDone += 1
        else:
          heal_points = random.randint(250,500)
          if vessels[actingVessel].hullMax > vessels[actingVessel].hull:
            vessels[actingVessel].hull+=heal_points
            print("We repaired",heal_points,"hull points.\nThe hull is at",vessels[actingVessel].hull)
          else:
            print("The hull is alreay at maximum (",vessels[actingVessel].hull,")")
            officersActed-=1
          time.sleep(2)
          threeDone += 1
      
    if orders == 4:
      if fourDone > 1:
        print("The ship'll be fine! Your attention is needed elsewhere!")
        officersActed -= 1
      else:
        print("The hull is at",vessels[actingVessel].hull)
        print("Energy weapons are",vessels[actingVessel].energyStatus)
        print("Torpedoes are",vessels[actingVessel].torpedoStatus)
        print("Shields are",vessels[actingVessel].shieldStatus)
        print("Maneuverability is at",vessels[actingVessel].turn)
        print("Engines are at",vessels[actingVessel].impulse)
        print("Our defensive rating is",vessels[actingVessel].defenses)
        time.sleep(4)
        fourDone += 1
      
    if orders == 5:
      if fiveDone > 1:
        print("We won't learn anything new from another scan.")
        officersActed -= 1
      else:
        subject = listAndTarget()
        print("Their hull is at",subject.hull)
        print("Their energy weapons are",subject.energyStatus)
        print("Their torpedoes are",subject.torpedoStatus)
        print("Their shields are",subject.shieldStatus)
        print("Their maneuverability is at",subject.turn)
        print("Their engines are at",subject.impulse)
        print("Their defensive rating is",subject.defenses)
        time.sleep(4)
        fiveDone += 1
    
    if orders == 6:
      if sixDone > 0:
        print("We're already engaged in evasive maneuvers.")
        officersActed -= 1
      else:
        vessels[actingVessel].maneuverBonus = 40
        Vessels.calcDefenses(vessels[actingVessel])
        sixDone += 1

    if orders == 7:
      if sevenDone > 1:
        print("We've enhanced her all we could right now.")
        officersActed -= 1
      else:
        print("\n1. Energy Weapons\n2. Torpedoes\n3. Scanners\n4. Engines")
        orders = eval(input("\nEnhance which system? "))
        if orders == 1:
          vessels[actingVessel].enAttackMod = 100
        elif orders == 2:
          vessels[actingVessel].torpAttackMod = 120
        elif orders == 3:
          vessels[actingVessel].enAttackMod += 50
          vessels[actingVessel].torpAttackMod += 50
        elif orders == 4:
          vessels[actingVessel].turn += 3
          vessels[actingVessel].impulse += .1
          Vessels.calcDefenses(vessels[actingVessel])
        sevenDone += 1
    
    officersActed += 1

def oblivion(lost):
  lostName = vessels[lost].name
  vessels[lost].ded=True
  print("\n 💀  We mark the passing of the "+lostName+" and her crew. May God have mercy on their souls. 💀")

### battle loop ###
battle_continue = True
actingVessel = 0

while battle_continue == True:

  if vessels[actingVessel].ded == True:
    actingVessel +=1
  
  turn(actingVessel)

  #if len(vessels) <= 1:
  #we need to check all vessels for ded here
  length = len(vessels)  
  dedCount = 0
  for i in range(length):
    if vessels[i].ded == True:
      dedCount += 1
    else:
      champion = i
  print(length)
  print(dedCount)
  if dedCount == (length-1):
    battle_continue = False
    print("The",vessels[champion].name,"has won the fight!")

  if vessels[actingVessel].ded == True:
    actingVessel +=1

  actingVessel += 1

  if actingVessel >= len(vessels):
    actingVessel = 0
    #battle_continue = False
  
  if battle_continue == True:
    print("\nTurn ended.\nReadying the",vessels[actingVessel].name)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("\n------------------------------------------------------------------\n")