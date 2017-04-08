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

class Character(Ability,Equipment):
	def __init__ (self,life_points,max_life_points,mana_points,max_mana_points,
					stamina_points,max_stamina_points,experience,level,style):
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

	def show_caracs(self):
		return [self.life_points,self.mana_points,
					self.stamina,self.level,self.experience, self.work]
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
		return "death"
	
class Foe(Character):
	def __init__(self,life_points,max_life_points,mana_points,max_mana_points,
					stamina_points,max_stamina_points,level,style):
		Character.__init__(self,life_points,max_life_points,mana_points,
							max_mana_points,stamina_points,max_stamina_points,0,level,style)
	def drop_loot(self, character_who_killed):
		from random import randint
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
