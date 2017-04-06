""" Let's create a class object"""
import characters
import random

class Object():
	def __init__(self,name, weight):
		self.name=name
		self.weight=weight
	def __repr__(self):
		return self.name


class Weapon(Object):
	def __init__(self,name,weight,distance,damage_range,style,
				strength_min=0,agility_min=0,intelligence_min=0):
		Object.__init__(self,name,weight)
		self.range=distance
		self.damage_range=damage_range
		self.strength_min=strength_min
		self.agility_min=agility_min
		self.intelligence_min=intelligence_min
	def equip_weapon(self,character):
		old_weapon=character.weapon
		if old_weapon!=None:
			character.inventory.append(old_weapon)
		character.weapon=self
		character.drop(self)


class Potion(Object):
	def __init__(self,name, weight, life_points_gained,mana_points_gained):
		Object.__init__(self,name,weight)
		self.life_points_gained = life_points_gained
		self.mana_points_gained=mana_points_gained
	def use(self,character):
		character.gain_lp(self.life_points_gained)
		character.gain_mana(self.mana_points_gained)
		if character.life_points >character.max_life_points:
			character.life_points=character.max_life_points
		if character.mana_points >character.max_mana_points:
			character.mana_points=character.max_mana_points


class Armour(Object):
	def __init__(self,name,weight,type_of_armour,protection,style,
					strength_min=0,endurance_min=0):
		Object.__init__(self,name,weight)
		self.type_of_armour=type_of_armour
		self.protection=protection
		self.strength_min=strength_min
		self.endurance_min=endurance_min
	def equip_armour(self,character):
		if character.strength<self.strength_min:
			return "strength too low"
		if character.endurance<self.endurance_min:
			return "endurance too low"
		else:
			if self.type_of_armour=="head":
				old_armour=character.head_equipment
				character.head_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
			elif self.type_of_armour=="arm":
				old_armour=character.arm_equipment
				character.arm_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
			elif self.type_of_armour=="torso":
				old_armour=character.torso_equipment
				character.torso_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
			elif self.type_of_armour=="leg":
				old_armour=character.leg_equipment
				character.leg_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
			elif self.type_of_armour=="foot":
				old_armour=character.foot_equipment
				character.foot_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
			character.body_protection=character.body_protection+self.protection
			if old_armour!=None:
				character.body_protection-=old_armour.protection
			character.drop(self)