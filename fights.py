#  Creation of the system of fights

import characters
import objects
import random

def plain_attack(attacker_character,defender_character):
	try:
		damage=attacker_character.weapon.damage_range
	except:
		#fight with bare hands
		hands=objects.Weapon("bare hands",0,0.75,[3,5],None)
		attacker_character.weapon=hands
		damage=attacker_character.weapon.damage_range
	damaged_dealt=int(random.randint(damage[0],damage[1])*1.25*(attacker_character.strength+1)-defender_character.body_protection)
	chance_to_touch=1-0.05*defender_character.agility+0.025*attacker_character.agility
	success=chance_to_touch>random.random()
	if success:
		defender_character.lose_lp(damaged_dealt)
	else:
		return "miss"

class Special_attack():
	def __init__(self,name,distance):
		self.name=name
		self.distance=distance
	def __repr__(self):
		return self.name

class Spell(Special_attack):
	def __init__(self,name,distance,mana_required,damage_range,intelligence_min=0):
		Special_attack.__init__(self,name,distance)
		self.mana_required=mana_required
		self.damage_range=damage_range
		self.intelligence_min=intelligence_min
	def use_spell(self,attacker_character,defender_character):
		if attacker_character.mana_points<self.mana_required:
			return "mana too low"
		else:
			attacker_character.lose_mana(self.mana_required)
			damaged_dealt=int(random.randint(self.damage_range[0],self.damage_range[1])*1.25*(attacker_character.intelligence+1)-(defender_character.will+1)*1.5)
			defender_character.lose_lp(damaged_dealt)