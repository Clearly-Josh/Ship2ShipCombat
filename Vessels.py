import random

def calcDefenses(ship2Calc):
  ship2Calc.defenses = (ship2Calc.turn * 2) + (ship2Calc.impulse * 10) + (ship2Calc.shield * 100) + ship2Calc.maneuverBonus
  print("Vessel defensive rating is now",ship2Calc.defenses)
  return ship2Calc.defenses

def displayShipName(self):
  print("These are the voyages of the " + self.name)

class Miranda:
  def __init__(self, name):
    self.name = name
    self.hull = 10000
    self.hullMax = 10000
    self.shield = 1
    self.shieldMax = 1
    self.shieldStatus="Online"
    self.turn = 11.4
    self.impulse = .2
    self.engineMax = 11.6 #turn + impulse
    #self.__attack_choice = attack_choice
    self.energyStatus="Online"
    self.enAttackMod=0
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.defenses = 0
    self.maneuverBonus = 0

  def energy(self):
    print("Firing phasers.")
    attack_points = random.randint(500,1500) + self.enAttackMod
    return attack_points
  def torpedo(self):
    print("Torpedoes away.")
    attack_points = random.randint(750,2000) + self.torpAttackMod
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(25,50)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)
      else:
        print("The hull is alreay at maximum (",self.hull,")")
  
#tests for Mirand class
# p1 = Miranda("USS Robert Scott", 10000, 1)
# p1.displayShipName()
# p2=p1.attack()
# print(p2)

class Saber:
  def __init__(self, name):
    self.name = name
    self.hull = 15000
    self.hullMax = 15000
    self.shield = .9
    self.shieldMax = .9
    self.shieldStatus="Online"
    self.turn = 17
    self.impulse = .2
    self.engineMax = 17.2 #turn + impulse
    #self.__attack_choice = attack_choice
    self.energyStatus="Online"
    self.enAttackMod=0
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.defenses = 0
    self.maneuverBonus = 0

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(500,1500) + self.enAttackMod
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(750,2000) + self.torpAttackMod
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(250,500)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)


class Nova:
  def __init__(self, name):
    self.name = name
    self.hull = 13500
    self.hullMax = 13500
    self.shield = 1.3
    self.shieldMax = 1.3
    self.shieldStatus="Online"
    self.turn = 14
    self.impulse = .15
    self.engineMax = 14.15 #turn + impulse
    #self.__attack_choice = attack_choice
    self.energyStatus="Online"
    self.enAttackMod=0
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.defenses = 0
    self.maneuverBonus = 0

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(500,1500) + self.enAttackMod
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(750,2000) + self.torpAttackMod
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(250,500)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)