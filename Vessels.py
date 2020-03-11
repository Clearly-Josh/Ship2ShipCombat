import random

class Miranda:
  def __init__(self, name, hull, attack_choice):
    self.name = 'USS Robert Scott'
    self.hull = 10000
    self.__attack_choice = attack_choice

  def displayShipName(self):
    print("These are the voyages of the " + self.name)

  def attack(self):

      if self.__attack_choice == 1:
          print("Torpedoes away.")
          attack_points = random.randint(18,25)
          return attack_points

      elif self.__attack_choice == 2:
          attack_points = random.randint(10,35)
          return attack_points

      else:
          print("That is not a selection. You lost your turn!")

  def heal(self):

      heal_points = random.randint(18,25)
      return heal_points
  

# p1 = Miranda("USS Robert Scott", 10000, 1)
# p1.displayShipName()
# p2=p1.attack()
# print(p2)