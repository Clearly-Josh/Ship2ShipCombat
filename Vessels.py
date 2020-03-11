import random

class Miranda:
  def __init__(self, name, hull, shield, turn, impulse, attack_choice):
    self.name = name
    self.hull = hull
    self.shield = shield
    self.turn = turn
    self.impulse = impulse
    self.__attack_choice = attack_choice

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(10,30)
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(15,50)
    return attack_points

  def heal(self):

      heal_points = random.randint(18,25)
      return heal_points
  
#tests for Mirand class
# p1 = Miranda("USS Robert Scott", 10000, 1)
# p1.displayShipName()
# p2=p1.attack()
# print(p2)

class Saber:
  def __init__(self, name, hull, shield, turn, impulse, attack_choice):
    self.name = name
    self.hull = hull
    self.shield = shield
    self.turn = turn
    self.impulse = impulse
    self.__attack_choice = attack_choice

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def energy(self):
    print("\nFiring phasers.")
    attack_points = random.randint(10,30)
    return attack_points
  def torpedo(self):
    print("\nTorpedoes away.")
    attack_points = random.randint(15,50)
    return attack_points

  def heal(self):

      heal_points = random.randint(18,25)
      return heal_points