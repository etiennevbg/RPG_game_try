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
		self.consumed_inventory=[]
		self.gold=0
	def add_in_inventory(self,Object):
		new_weight=self.weight+Object.weight
		if new_weight>self.weight_max:
			return 'impossible'
		else:
			self.weight=new_weight
			self.inventory.append(Object)
	def add_in_consumed_inventory(self,food):
		self.consumed_inventory.append(food)
	def drop(self,Object):
		for obj in self.inventory:
			if obj.name==Object.name:
				self.weight-=Object.weight
				self.inventory.remove(obj)
	def drop_consumed(self,Object):
		for obj in self.consumed_inventory:
			if obj.name==Object.name:
				self.consumed_inventory.remove(obj)
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
	def distance_to_instance(self,other_instance):
		return sqrt((self.x-other_instance.x)**2+(self.y-other_instance.y)**2)
	def collision(self,other_instance):
		if self.distance_to_instance(other_instance)<0.5:
			return True

class Quest_book():
	def __init__(self):
		self.quest_book=[]
	def add_quest(self,quest):
		self.quest_book.append(quest)
	def realize_condition_quest(self,quest,condition):
		if quest in self.quest_book:
			i=self.quest_book.index(quest)
			if condition in quest.quest_conditions:
				j=quest.quest_conditions.index(condition)
				self.quest_book[i].quest_conditions[j]=True
	def accomplished_quest(self,quest):
		if quest in self.quest_book:
			for condition in quest.quest_conditions:
				if condition!=True:
					return 'quest unfinished'
			quest.quest_accomplished=True
			return quest.quest_reward

class Character(Ability,Equipment,Skills,Position,Quest_book):
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
		Quest_book.__init__(self)
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
	def detection_of_foe(self,main_character):
		distance_foe=self.distance_to_instance(main_character)
		if distance_foe<30:
			"""detection_chance=[[proba1,distance1],[proba2,distance2]...]"""
			detection_chance=[[0.9,5],[0.5,10],[0.25,15],[0.1,20],[0.01,25]]
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

class Quest():
	def __init__(self,name,description,conditions,reward):
		self.quest_name=name
		self.quest_description=description
		self.quest_conditions=conditions
		#  reward as (experience,gold,equipment=None)
		self.quest_reward=reward
		self.quest_accomplished=False
	def __repr__(self):
		return self.quest_name
	def give_quest(self,character):
		character.add_quest(self)

class NPC(Quest,Position):
	def __init__(self,name,reply,style,quest_name=None,quest_description=None,
					quest_conditions=None, quest_reward=None):
		self.name=name
		self.reply=reply
		self.style=style
		Quest.__init__(self,quest_name,quest_description,quest_conditions,quest_reward)
		Position.__init__(self)
	def talk(self):
		return(self.reply)
	def new_quest(self,quest):
		self.quest_name=quest.quest_name
		self.quest_description=quest.quest_description
		self.quest_conditions=quest.quest_conditions
		self.quest_reward=quest.quest_reward
		self.quest_accomplished=False

class Merchant(NPC,Equipment):
	def __init__(self,name,reply,style,quest_name=None,quest_description=None,
					quest_conditions=None, quest_reward=None):
		NPC.__init__(self,name,reply,style,quest_name,quest_description,
					quest_conditions, quest_reward)
		Equipment.__init__(self,1000)
		self.gold=random.randint(700,1000)
	def exchange(self,character):
		return (self.gold,self.inventory,character.gold,character.inventory)



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""foes={name:level_range,abilitity_ranges}"""
foes={"ogre low level":([1,3],[[2,5],[1,4],[1,5],[0,2],[0,2],[0,3]]),
		"ogre medium level":([4,7],[[4,8],[4,7],[3,6],[2,4],[2,4],[1,5]]),
		"spider low level":([1,3],[[1,4],[2,5],[1,5],[0,1],[0,3],[0,3]]),
		"spider medium level":([4,7],[[2,5],[6,8],[3,6],[1,4],[3,5],[1,4]])}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""