from numpy import random
equipment = ['sword', 'axe', 'bow']

class Knight:
  def __init__(self, health):
    self.health = health
  
  def attack_dragon(self, dragon):
    if dragon.health > 0 or dragon.slain == False:
      if random.randint(100) >= 70:
        dragon.dragon_damage(20)
        print("Critical hit! The dragon takes 20 damage!")
        print("The dragon has {health} health left!".format(health = dragon.health))
      elif random.randint(100) >= 10:
        dragon.dragon_damage(10)
        print("The dragon takes 10 damage!")
        print("The dragon has {health} health left!".format(health = dragon.health))
      else:
        print("The knight misses!")
    elif dragon.slain == True:
      print("Stop, stop, he's already dead!")

class Dragon:
  def __init__(self, health, slain = False):
    self.health = health
    self.slain = slain

  def dragon_damage(self, knight_damage):
    if self.health > 0:
      self.health -= knight_damage
    elif self.health <= 0:
      self.dragon_slain()
  
  def dragon_slain(self):
    self.slain == True
    print("The dragon has been defeated!")