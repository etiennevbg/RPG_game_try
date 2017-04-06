""" Let's create a class object"""
import characters
import random

class Object():
	def __init__(self, weight):
		self.weight=weight


class Weapon(Object):
	def __init__(self,weight,distance,damage_range,
				strength_min=0,agility_min=0,intelligence_min=0):
		Object.__init__(self,weight)
		self.range=distance
		self.damage_range=damage_range
		self.strength_min=strength_min
		self.agility_min=agility_min
		self.intelligence_min=intelligence_min
	def attack(self,foe):
		damages=random.randint(self.damage_range[0],self.damage_range[1])
		foe.lose_lp(damages)

