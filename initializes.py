import characters
import objects
import random
import copy

"""from a dictionnary, let's initialize the instances
	foes, attacks and objects using from 0 to all arguments"""

def create_foe(foe_name,level=None):
	caracterisation=foes[foe_name]
	caracterisation_foe=copy.deepcopy(caracterisation)
	if level!=None:
		if level<caracterisation_foe[0][0]:
			level=caracterisation_foe[0][0]
		elif level>caracterisation_foe[0][1]:
			level=caracterisation_foe[0][1]
	else:
		level=random.randint(caracterisation_foe[0][0],caracterisation_foe[0][1])
	value_of_abilities=level*4
	#  we now make the repartition of abilitiy values
	value_of_ability_min=0
	value_of_ability_max=0
	for increment in range (6):
		value_of_ability_min+=caracterisation_foe[1][increment][0]
		value_of_ability_max+=caracterisation_foe[1][increment][1]
	for increment in range(6):
		value_for_this_ability=random.randint(caracterisation_foe[1][increment][0],caracterisation_foe[1][increment][1])
		if value_of_abilities-value_for_this_ability>value_of_ability_max:
			value_for_this_ability=caracterisation_foe[1][increment][1]
		elif value_of_abilities-value_for_this_ability<value_of_ability_min:
			value_for_this_ability=caracterisation_foe[1][increment][0]
		value_of_ability_min-=caracterisation_foe[1][increment][0]
		value_of_ability_max-=caracterisation_foe[1][increment][1]
		value_of_abilities-=value_for_this_ability
		caracterisation_foe[1][increment]=value_for_this_ability
	abilities=caracterisation_foe[1]
	#  add other characteristics
	max_life_points=50+25*abilities[0]
	max_mana_points=20+10*abilities[4]
	max_stamina_points=10+2*abilities[2]
	non_space=True
	number=0
	while non_space:
		number+=1
		if foe_name[number]==' ':
			non_space=False
	name=foe_name[:number]
	#  let's now create the instance
	foe=characters.Foe(name,max_life_points,max_life_points,max_mana_points,max_mana_points,
							max_stamina_points,max_stamina_points,level,None)
	foe.change_strength(abilities[0])
	foe.change_agility(abilities[1])
	foe.change_endurance(abilities[2])
	foe.change_intelligence(abilities[3])
	foe.change_will(abilities[4])
	foe.change_luck(abilities[5])
	return foe

"""foes={name:level_range,abilitity_ranges}"""
foes={"ogre low level":([1,3],[[2,5],[1,4],[1,5],[0,2],[0,2],[0,3]]),
		"ogre medium level":([4,7],[[4,8],[4,7],[3,6],[2,4],[2,4],[1,5]])}
