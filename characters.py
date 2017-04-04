"""Here we are going to create several classes
	of characters available for the player,
	and also every work the player can do"""
	

class Character():
	def __init__ (self,life_points,mana_points,level,
					work,style,stats):
		self.life_points=life_points
		self.mana_points=mana_points
		self.level=level
		self.work=work
		self.style=style
		self.stats=stats

	def show_caracs(self):
		return [self.life_points,self.mana_points,
					self.level,self.work]

	def show_stats(self):
		return self.stats


