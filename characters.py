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
	

class Character(Ability):
	def __init__ (self,life_points,max_life_points,mana_points,max_mana_points,
					experience,level,work,style):
		self.life_points=life_points
		self.max_life_points=max_life_points
		self.mana_points=mana_points
		self.max_mana_points=max_mana_points
		self.level=level
		self.experience=experience
		self.work=work
		self.style=style
		Ability.__init__(self)

	def show_caracs(self):
		return [self.life_points,self.mana_points,
					self.level,self.experience, self.work]
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
	
class Foe(Character):
	def __init__(self,life_points,max_life_points,mana_points,max_mana_points,
					level,style):
		Character.__init__(self,life_points,max_life_points,mana_points,
							max_mana_points,0,level,None,style)