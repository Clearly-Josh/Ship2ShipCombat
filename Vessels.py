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
    self.torpedoStatus="Operational"
    self.defenses = 0
    if self.turn >= 10:
      self.defenses +=5
    if self.impulse >= .2:
      self.defenses += 2
    if self.shield >= 1:
      self.defenses += 10

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(20,55)
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(25,50)
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(18,25)
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
    self.shieldStatus="Operational"
    self.turn = turn
    self.impulse = impulse
    self.engineMax = turn + impulse
    self.__attack_choice = attack_choice
    self.energyStatus="Operational"
    self.torpedoStatus="Operational"
    self.defenses = 0
    if self.turn >= 10:
      self.defenses +=5
    if self.impulse >= .2:
      self.defenses += 2
    if self.shield >= 1:
      self.defenses += 10

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(20,55)
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(25,50)
    return attack_points

  def heal(self,sys):
      #if sys==1: 
      #elif sys == 5:
      heal_points = random.randint(18,25)
      if self.hullMax > self.hull:
        self.hull+=heal_points
        print("You repaired",heal_points,"hull points.\nYour hull is at",self.hull)