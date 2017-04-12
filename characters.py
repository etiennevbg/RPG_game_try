"""Here we are going to create several classes
	of characters available for the player,
	and also every work the player can do"""


class Ability():
	def __init__(self,strength=0,agility=0,endurance=0,intelligence=0,will=0,luck=0):
		self.strength=strength
		self.agility=agility
		self.endurance=endurance
		self.intelligence=intelligence
		self.will=will
		self.luck=luck
	def change_strength(self,value):
		self.strength+=value
	def change_agility(self,value):
		self.agility+=value
	def change_endurance(self,value):
		self.endurance+=value
	def change_intelligence(self,value):
		self.intelligence+=value
	def change_will(self,value):
		self.will+=value
	def change_luck(self,value):
		self.luck+=value
	
class Equipment():
	def __init__(self,weight_max=50):
		self.head_equipment=None
		self.arm_equipment=None
		self.torso_equipment=None
		self.leg_equipment=None
		self.foot_equipment=None
		self.weapon=None
		self.left_hand=None
		self.weight_max=weight_max
		self.weight=0
		self.inventory=[]
		self.gold=0
	def add_in_inventory(self,Object):
		new_weight=self.weight+Object.weight
		if new_weight>self.weight_max:
			return 'impossible'
		else:
			self.weight=new_weight
			self.inventory.append(Object)
	def drop(self,Object):
		for obj in self.inventory:
			if obj.name==Object.name:
				self.weight-=Object.weight
				self.inventory.remove(obj)
	def show_inventory(self):
		return(self.inventory)
	def gain_gold(self, value):
		self.gold+=value
	def show_wealth(self):
		return self.gold

class Skills():
	def __init__(self):
		self.list_of_spells=[]
		self.list_of_healing_spells=[]
		self.list_of_attacks=[]
	def add_spell(self,spell):
		for increment in range(len(self.list_of_spells)):
			if self.list_of_spells[increment].name==spell.name :
				return None
		self.list_of_spells.append(spell)
	def add_healing_spell(self,healing_spell):
		for increment in range(len(self.list_of_healing_spells)):
			if self.list_of_healing_spells[increment].name==healing_spell.name :
				return None
		self.list_of_healing_spells.append(healing_spell)
	def add_attack(self,alternative_attack):
		for increment in range(len(self.list_of_attacks)):
			if self.list_of_attacks[increment].name==alternative_attack.name :
				return None
		self.list_of_attacks.append(alternative_attack)
	def show_skills(self):
		return(self.list_of_spells,self.list_of_healing_spells,self.list_of_attacks)

from math import sqrt
class Position():
	def __init__(self,x=0,y=0,speed=1):
		self.x=x
		self.y=y
		self.speed=speed
	def go_to(self,x,y):
		distance_to_run=sqrt((x-self.x)**2+(y-self.y)**2)
		if distance_to_run<1:
			return "destination reached"
		else:
			new_x=self.speed*(x-self.x)/float(distance_to_run)
			new_y=self.speed*(y-self.y)/float(distance_to_run)
			self.x+=new_x
			self.y+=new_y
	def set_to_position(self,x,y):
		self.x=x
		self.y=y

class Character(Ability,Equipment,Skills,Position):
	def __init__ (self,name,life_points,max_life_points,mana_points,max_mana_points,
					stamina_points,max_stamina_points,experience,level,style):
		self.name=name
		self.life_points=life_points
		self.max_life_points=max_life_points
		self.mana_points=mana_points
		self.max_mana_points=max_mana_points
		self.stamina_points=stamina_points
		self.max_stamina_points=max_stamina_points
		self.level=level
		self.experience=experience
		self.body_protection=0
		self.work=None
		self.style=style
		Ability.__init__(self)
		Equipment.__init__(self)
		Skills.__init__(self)
		Position.__init__(self)
	def __repr__(self):
		return self.name

	def show_caracs(self):
		return [self.life_points,self.mana_points,
					self.stamina_points,self.level,self.experience, self.work]
	def show_abilities(self):
		return [self.strength,self.agility,self.endurance,
				self.intelligence,self.will,self.luck]
	def lose_lp(self,nbr):
		self.life_points-=nbr
	def gain_lp(self,nbr):
		self.life_points+=nbr
	def lose_mana(self,nbr):
		self.mana_points-=nbr
	def gain_mana(self,nbr):
		self.mana_points+=nbr
	def gain_exp(self,value):
		self.experience+=value
	def level_up(self, nbr=1):
		self.level+=nbr
	def die(self):
		if self.life_points<=0:
			return "death"

import random
class Foe(Character):
	def __init__(self,name,life_points,max_life_points,mana_points,max_mana_points,
					stamina_points,max_stamina_points,level,style):
		Character.__init__(self,name,life_points,max_life_points,mana_points,
							max_mana_points,stamina_points,max_stamina_points,0,level,style)
	def drop_loot(self, character_who_killed):
		max_loot=len(self.inventory)
		number_of_loot=int(randint(0,max_loot)*0.5*(character_who_killed.luck+1))
		if number_of_loot>max_loot:
			number_of_loot=max_loot
		loots=[]
		iterable=0
		while iterable<number_of_loot:
			new_length_of_inventory=len(self.inventory)
			j=randint(0,new_length_of_inventory-1)
			loot=self.inventory[j]
			loots.append(loot)
			self.drop(self.inventory[j])
			iterable+=1
		return (self.gold,loots)
	def distance_to_foe(self,main_character):
		return sqrt((self.x-main_character.x)**2+(self.y-main_character.y)**2)
	def detection_of_foe(self,main_character):
		distance_foe=self.distance_to_foe(main_character)
		if distance_foe<30:
			"""detection_chance=[[proba1,distance1],[proba2,distance2]...]"""
			detection_chance=[[0.9,5],[0.7,10],[0.45,15],[0.20,20],[0.05,25]]
			detected=0
			for i in range(len(detection_chance)):
				element_of_non_detection=1
				for j in range(len(detection_chance)):
					if j!=i:
						element_of_non_detection*=(distance_foe-detection_chance[j][1])/float(detection_chance[i][1]-detection_chance[j][1])
				detected+=detection_chance[i][0]*element_of_non_detection
			probability_of_non_detection=random.random()
			if detected>probability_of_non_detection:
				return "detected"


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""foes={name:level_range,abilitity_ranges}"""
foes={"ogre low level":([1,3],[[2,5],[1,4],[1,5],[0,2],[0,2],[0,3]]),
		"ogre medium level":([4,7],[[4,8],[4,7],[3,6],[2,4],[2,4],[1,5]])}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""