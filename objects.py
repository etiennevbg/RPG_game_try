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
	def __init__(self,name,weight,distance,damage_range,
				strength_min=0,agility_min=0,intelligence_min=0):
		Object.__init__(self,name,weight)
		self.range=distance
		self.damage_range=damage_range
		self.strength_min=strength_min
		self.agility_min=agility_min
		self.intelligence_min=intelligence_min
	def equip_weapon(self,character):
		if not self in character.inventory:
			return None
		old_weapon=character.weapon
		if old_weapon!=None:
			character.add_in_inventory(old_weapon)
			character.weight-=old_weapon.weight
		character.weapon=self
		character.weight+=self.weight
		character.drop(self)
	def unequip_weapon(self,character):
		character.add_in_inventory(self)
		character.weapon=None


class Potion(Object):
	def __init__(self,name, weight, life_points_gained,
						mana_points_gained,stamina_points_gained):
		Object.__init__(self,name,weight)
		self.life_points_gained = life_points_gained
		self.mana_points_gained=mana_points_gained
		self.stamina_points_gained=stamina_points_gained
	def use(self,character):
		if not self in character.inventory:
			return None
		character.gain_lp(self.life_points_gained)
		character.gain_mana(self.mana_points_gained)
		if character.life_points >character.max_life_points:
			character.life_points=character.max_life_points
		elif character.life_points<=0:
			death=character.die()
			return death
		if character.mana_points >character.max_mana_points:
			character.mana_points=character.max_mana_points
		if character.stamina_points >character.max_stamina_points:
			character.stamina_points=character.max_stamina_points
		character.drop(self)


class Armour(Object):
	def __init__(self,name,weight,type_of_armour,protection,
					strength_min=0,endurance_min=0):
		Object.__init__(self,name,weight)
		self.type_of_armour=type_of_armour
		self.protection=protection
		self.strength_min=strength_min
		self.endurance_min=endurance_min
	def equip_armour(self,character):
		if not self in character.inventory:
			return None
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
					character.weight-=old_armour.weight
			elif self.type_of_armour=="arm":
				old_armour=character.arm_equipment
				character.arm_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
					character.weight-=old_armour.weight
			elif self.type_of_armour=="torso":
				old_armour=character.torso_equipment
				character.torso_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
					character.weight-=old_armour.weight
			elif self.type_of_armour=="leg":
				old_armour=character.leg_equipment
				character.leg_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
					character.weight-=old_armour.weight
			elif self.type_of_armour=="foot":
				old_armour=character.foot_equipment
				character.foot_equipment=self
				if old_armour!=None:
					character.add_in_inventory(old_armour)
					character.weight-=old_armour.weight
			character.body_protection=character.body_protection+self.protection
			if old_armour!=None:
				character.body_protection-=old_armour.protection
			character.weight+=self.weight
			character.drop(self)

class Food(Potion):
	def __init__(self,name,weight,life_points_gained,side_effect):
		Potion.__init__(self,name,weight,life_points_gained,0,0)
		self.side_effect=side_effect
		self.duration_of_effect=-1
	def eat(self,character):
		if self.side_effect!=None:
			effect=self.side_effect.split()
			#  the type of side_effect will be a string written
			#  this way : "gain 1 strength for 5 rounds" or
			#  "lose 30 max_life_points for 2 rounds"
			self.duration_of_effect=int(effect[4])
			value=int(effect[1])
			if effect[0]=='lose':
				value=value*(-1)
			if effect[2]=='strength':
				character.change_strength(value)
			if effect[2]=='agility':
				character.change_agility(value)
			if effect[2]=='endurance':
				character.change_endurance(value)
			if effect[2]=='intelligence':
				character.change_intelligence(value)
			if effect[2]=='will':
				character.change_will(value)
			if effect[2]=='luck':
				character.change_luck(value)
			if effect[2]=='max_life_points':
				character.max_life_points+=value
				character.life_points+=value
			if effect[2]=='max_mana_points':
				character.max_mana_points+=value
				character.mana_points+=value
			if effect[2]=='max_stamina_points':
				character.max_stamina_points+=value
				character.stamina_points+=value
		character.add_in_consumed_inventory(self)
		self.use(character)
	def end_effect(self,character):
		self.duration_of_effect-=1
		if self.duration_of_effect==0:
			effect=self.side_effect.split()
			value=-int(effect[1])
			if effect[0]=='lose':
				value=value*(-1)
			if effect[2]=='strength':
				character.change_strength(value)
			if effect[2]=='agility':
				character.change_agility(value)
			if effect[2]=='endurance':
				character.change_endurance(value)
			if effect[2]=='intelligence':
				character.change_intelligence(value)
			if effect[2]=='will':
				character.change_will(value)
			if effect[2]=='luck':
				character.change_luck(value)
			if effect[2]=='max_life_points':
				character.max_life_points+=value
				character.life_points+=value
			if effect[2]=='max_mana_points':
				character.max_mana_points+=value
				character.mana_points+=value
			if effect[2]=='max_stamina_points':
				character.max_stamina_points+=value
				character.stamina_points+=value
			character.drop_consumed(self)
			print("{} do not affect {} anymore".format(self,character))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""armours={'category type':[
											(name1,weight1,protection_range1),
											(name2,weight2,protection_range2)
											]}"""
armours={'heavy head':[
				("iron helmet",2,[5,10]),
				("bronze helmet",2.5,[8,12])
				],
			'medium head':[
				("reenforced cap",1.25,[4,6])
				],
			'light head':[
				('iron crown',0.5,[2,4]),
				('gold crown',0.75,[3,5]),
				('fur chapka',0.25,[1,3])
				],
			'heavy arm':[
				('iron gantlet',2,[7,12])
				],
			'medium arm':[
				('leather gantlet',1,[5,8])
				],
			'light arm':[
				('textile gantlet',0.5,[3,6])
				],
			'heavy torso':[
				('iron plastron',4.5,[18,22])
				],
			'medium torso':[
				('leather plastron',3,[14,18])
				],
			'light torso':[
				('textile plastron',1.75,[11,15])
				],
			'heavy leg':[
				('iron legs',3.5,[10,15])
				],
			'medium leg':[
				('leather legs',2.5,[7,10])
				],
			'light leg':[
				('textile legs',1.25,[5,8])
				],
			'heavy foot':[
				('iron boots',2,[7,12])
				],
			'medium foot':[
				('leather boots',1,[5,8])
				],
			'light foot':[
				('textile boots',0.5,[3,6])
				]}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""weapons={'category type':[
								('name1',weight1,[attack_min_range1,attack_max_range1]),
								('name2',weight2,[attack_min_range2,attack_max_range2])
								]}"""
weapons={'heavy mele':[
				('adamantium axe',6,[[23,26],[27,30]]),
				('adamantium sword',5,[[21,24],[24,28]])
				],
			'medium mele':[
				('iron sword',3,[[12,14],[16,20]])
				],
			'light mele':[
				('iron dagger',1.5,[[8,10],[10,12]]),
				('wood staff',2,[[4,6],[13,15]]),
				('knuckles',1,[[5,6],[6,8]])
				],
			'heavy distance':[
				('artillery',5,[[18,22],[22,25]])
				],
			'medium distance':[
				('oak bow',3,[[10,15],[16,19]]),
				('magic staff',2.5,[[7,9],[13,16]])
				],
			'light distance':[
				('orm bow',1.75,[[6,7],[8,10]])
				]}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""foods=[food_name1,food_name2,...]"""
foods=['cream pie','beef rost','ratatouille','pancakes','fruit salad',
		'ceasar salad']