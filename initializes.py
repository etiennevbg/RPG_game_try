import characters
import objects
import random
import copy

"""from a dictionnary, let's initialize the instances
	foes, attacks and objects using from 0 to all arguments"""

def create_foe(foe_name,level=None):
	caracterisation_foe=copy.deepcopy(foes[foe_name])
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

def create_armour(category_of_armour=None,type_of_armour=None):
	if category_of_armour==None:
		choice_of_category=random.randint(0,len(category_of_armours)-1)
		category_of_armour=category_of_armours[choice_of_category]
	if type_of_armour==None:
		choice_of_type=random.randint(0,len(type_of_armours)-1)
		type_of_armour=type_of_armours[choice_of_type]
	armour_key="{} {}".format(category_of_armour,type_of_armour)
	caracterisation_armour=copy.deepcopy(armours[armour_key])
	choice_of_armour=random.randint(0,len(caracterisation_armour)-1)
	armour_chosen=caracterisation_armour[choice_of_armour]
	name=armour_chosen[0]
	weight=armour_chosen[1]
	protection=random.randint(armour_chosen[2][0],armour_chosen[2][1])
	if category_of_armour=='light':
		strength_min=0
		endurance_min=0
	elif category_of_armour=='medium':
		strength_min=1
		endurance_min=2
	elif category_of_armour=='heavy':
		strength_min=3
		endurance_min=5
	return objects.Armour(name,weight,type_of_armour,protection,
							strength_min,endurance_min)


"""foes={name:level_range,abilitity_ranges}"""
foes={"ogre low level":([1,3],[[2,5],[1,4],[1,5],[0,2],[0,2],[0,3]]),
		"ogre medium level":([4,7],[[4,8],[4,7],[3,6],[2,4],[2,4],[1,5]])}


type_of_armours=("head","arm","torso","leg","foot")
category_of_armours=("light","medium","heavy")

"""armours={'category type':[
							(name1,weight1,protection_range1),
							(name2,weight2,protection_range2)
							]}"""
armours={'heavy head':[
				("iron helmet",2,[5,10]),
				("bronze helmet",2.5,[8,12])
				],
			'medium head':[
				("reenforced cap",1.25,[4,6])
				],
			'light head':[
				('iron crown',0.5,[2,4]),
				('gold crown',0.75,[3,5]),
				('fur chapka',0.25,[1,3])
				],
			'heavy arm':[
				],
			'medium arm':[
				],
			'light arm':[
				],
			'heavy torso':[
				],
			'medium torso':[
				],
			'light torso':[
				],
			'heavy leg':[
				],
			'medium leg':[
				],
			'light leg':[
				],
			'heavy foot':[
				],
			'medium foot':[
				],
			'light foot':[
				]}
