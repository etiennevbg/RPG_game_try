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
