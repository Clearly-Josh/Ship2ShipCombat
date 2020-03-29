import random

class Miranda:
  def __init__(self, name, hull, shield, turn, impulse, attack_choice):
    self.name = name
    self.hull = hull
    self.hullMax = hull
    self.shield = shield
    self.shieldStatus="Operational"
    self.turn = turn
    self.impulse = impulse
    self.engineMax = turn + impulse
    self.__attack_choice = attack_choice
    self.energyStatus="Operational"
    self.enAttackMod=0
    self.torpedoStatus="Operational"
    self.torpAttackMod=0
    self.defenses = (self.turn * .5) + (self.impulse * 10) + (self.shield * 10)

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(50,150) + self.enAttackMod
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(75,200) + self.torpAttackMod
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(25,50)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)
  
#tests for Mirand class
# p1 = Miranda("USS Robert Scott", 10000, 1)
# p1.displayShipName()
# p2=p1.attack()
# print(p2)

class Saber:
  def __init__(self, name, hull, shield, turn, impulse, attack_choice):
    self.name = name
    self.hull = hull
    self.hullMax = hull
    self.shield = shield
    self.shieldOriginal = shield
    self.shieldStatus="Operational"
    self.turn = turn
    self.turnOriginal = turn
    self.impulse = impulse
    self.impulseOriginal = impulse
    self.engineMax = turn + impulse
    self.__attack_choice = attack_choice
    self.energyStatus="Operational"
    self.enAttackMod=0
    self.torpedoStatus="Operational"
    self.torpAttackMod=0
    self.defenses = (self.turn * .5) + (self.impulse * 10) + (self.shield * 10)

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(50,150) + self.enAttackMod
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(75,200) + self.torpAttackMod
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(25,50)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)