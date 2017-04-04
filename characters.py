"""Here we are going to create several classes
	of characters available for the player,
	and also every work the player can do"""
	

class Character():
	def __init__ (self,life_points,mana_points,experience,
					level,work,style,stats):
		self.life_points=life_points
		self.mana_points=mana_points
		self.level=level
		self.experience=experience
		self.work=work
		self.style=style
		self.stats=stats

	def show_caracs(self):
		return [self.life_points,self.mana_points,
					self.level,self.experience, self.work]
	def show_stats(self):
		return self.stats

	def lose_lp(self,nbr):
		new_nbr_of_life_points=self.life_points-nbr
		self.life_points=new_nbr_of_life_points
	def gain_lp(self,nbr):
		new_nbr_of_life_points=self.life_points+nbr
		self.life_points=new_nbr_of_life_points
	def lose_mana(self,nbr):
		new_nbr_of_mana_points=self.mana_points-nbr
		self.mana_points=new_nbr_of_mana_points
	def gain_mana(self,nbr):
		new_nbr_of_mana_points=self.mana_points+nbr
		self.mana_points=new_nbr_of_mana_points
	def gain_exp(self,value):
		self.experience+=value
	def level_up(self, nbr=1):
		self.level+=nbr
	
