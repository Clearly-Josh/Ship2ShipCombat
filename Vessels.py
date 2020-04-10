import random

def calcDefenses(ship2Calc):
  ship2Calc.defenses = (ship2Calc.turn * 3) + (ship2Calc.impulse * 15) + (ship2Calc.shield * 1000) + ship2Calc.maneuverBonus
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
    self.enBase=500
    self.enMax=750
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.torpBase=750
    self.torpMax=2000
    self.defenses = 0
    self.maneuverBonus = 0
    self.ded = False
  
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
    self.enBase=500
    self.enMax=750
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.torpBase=750
    self.torpMax=2000
    self.defenses = 0
    self.maneuverBonus = 0
    self.ded = False

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
    self.enBase=500
    self.enMax=750
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.torpBase=750
    self.torpMax=2000
    self.defenses = 0
    self.maneuverBonus = 0
    self.ded = False

class Dhelan:
  def __init__(self, name):
    self.name = name
    self.hull = 15800
    self.hullMax = 15800
    self.shield = .95
    self.shieldMax = .95
    self.shieldStatus="Online"
    self.turn = 16
    self.impulse = .2
    self.engineMax = 16.2 #turn + impulse
    #self.__attack_choice = attack_choice
    self.energyStatus="Online"
    self.enAttackMod=0
    self.enBase=500
    self.enMax=750
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.torpBase=750
    self.torpMax=2000
    self.defenses = 0
    self.maneuverBonus = 0
    self.ded = False

class NX:
  def __init__(self, name):
    self.name = name
    self.hull = 10000
    self.hullMax = 10000
    self.shield = 1
    self.shieldMax = 1
    self.shieldStatus="Online"
    self.turn = 14
    self.impulse = .17
    self.engineMax = 14.17 #turn + impulse
    #self.__attack_choice = attack_choice
    self.energyStatus="Online"
    self.enAttackMod=0
    self.enBase=500
    self.enMax=750
    self.torpedoStatus="Online"
    self.torpAttackMod=0
    self.torpBase=750
    self.torpMax=2000
    self.defenses = 0
    self.maneuverBonus = 0
    self.ded = False

