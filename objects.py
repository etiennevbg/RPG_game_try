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


class Potion(Object):
	def __init__(self, weight, life_points_gained,mana_points_gained):
		Object.__init__(self,weight)
		self.life_points_gained = life_points_gained
		self.mana_points_gained=mana_points_gained
	def use(self,character):
		character.gain_lp(self.life_points_gained)
		character.gain_mana(self.mana_points_gained)
		if character.life_points >character.max_life_points:
			character.life_points=character.max_life_points
		if character.mana_points >character.max_mana_points:
			character.mana_points=character.max_mana_points

