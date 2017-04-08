import characters
import objects
import random

"""from a dictionnary, let's initialize the instances
	foes, attacks and objects using from 0 to all arguments"""

"""foes={name:level_range,abilitity_ranges}"""
foes={"ogre low level":([1,3],[[2,5],[1,4],[1,5],[0,2],[0,2],[0,3]]),
		"ogre medium level":([4,7],[[4,8],[4,7],[3,6],[2,4],[2,4],[1,5]])}

def create_foe(foe_name,level=None):
	caracterisation_foe=foes[foe_name]
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
	print (abilities)
