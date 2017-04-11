import characters
import objects
import fights
import random
import copy

"""from a dictionnary, let's initialize the instances
	foes, attacks and objects using from 0 to all arguments"""

def create_foe(foe_name,level=None):
	caracterisation_foe=copy.deepcopy(characters.foes[foe_name])
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
	foe_name=foe_name.split()
	name=foe_name[0]
	#  let's now create the instance
	foe=characters.Foe(name,max_life_points,max_life_points,max_mana_points,max_mana_points,
							max_stamina_points,max_stamina_points,level,None)
	foe.change_strength(abilities[0])
	foe.change_agility(abilities[1])
	foe.change_endurance(abilities[2])
	foe.change_intelligence(abilities[3])
	foe.change_will(abilities[4])
	foe.change_luck(abilities[5])
	#  let's now equip the foe with pieces of armour
	if foe_name[1]=='low':
		category_of_foe='light'
	elif foe_name[1]=='medium':
		category_of_foe='medium'
	elif foe_name[1]=='high':
		category_of_foe='heavy'
	number_elements_of_armour=random.randint(1,5)
	while True:
		torso_equipment=create_armour(category_of_foe,'torso')
		foe.add_in_inventory(torso_equipment)
		torso_equipment.equip_armour(foe)
		number_elements_of_armour-=1
		if number_elements_of_armour==0:
			break
		leg_equipment=create_armour(category_of_foe,'leg')
		foe.add_in_inventory(leg_equipment)
		leg_equipment.equip_armour(foe)
		number_elements_of_armour-=1
		if number_elements_of_armour==0:
			break
		foot_equipment=create_armour(category_of_foe,'foot')
		foe.add_in_inventory(foot_equipment)
		foot_equipment.equip_armour(foe)
		number_elements_of_armour-=1
		if number_elements_of_armour==0:
			break
		arm_equipment=create_armour(category_of_foe,'arm')
		foe.add_in_inventory(arm_equipment)
		arm_equipment.equip_armour(foe)
		number_elements_of_armour-=1
		if number_elements_of_armour==0:
			break
		head_equipment=create_armour(category_of_foe,'head')
		foe.add_in_inventory(head_equipment)
		head_equipment.equip_armour(foe)
		number_elements_of_armour-=1
		if number_elements_of_armour==0:
			break
	#  let's give a weapon to the foe
	weapon=create_weapon(category_of_foe)
	foe.add_in_inventory(weapon)
	weapon.equip_weapon(foe)
	#  now let's put loots in its inventory
	number_of_objects=random.randint(0,4)
	for i in range(number_of_objects):
		choice_of_object=random.randint(0,9)
		if choice_of_object==0:
			new_object=create_weapon()
			foe.add_in_inventory(new_object)
		elif choice_of_object==1:
			new_object=create_armour()
			foe.add_in_inventory(new_object)
		else:
			new_object=create_consumable()
			foe.add_in_inventory(new_object)
	return foe

def create_armour(category_of_armour=None,type_of_armour=None):
	if category_of_armour==None:
		category_of_armours=("light","medium","heavy")
		choice_of_category=random.randint(0,len(category_of_armours)-1)
		category_of_armour=category_of_armours[choice_of_category]
	if type_of_armour==None:
		type_of_armours=("head","arm","torso","leg","foot")
		choice_of_type=random.randint(0,len(type_of_armours)-1)
		type_of_armour=type_of_armours[choice_of_type]
	armour_key="{} {}".format(category_of_armour,type_of_armour)
	caracterisation_armour=copy.deepcopy(objects.armours[armour_key])
	choice_of_armour=random.randint(0,len(caracterisation_armour)-1)
	armour_chosen=caracterisation_armour[choice_of_armour]
	name=armour_chosen[0]
	weight=armour_chosen[1]
	protection=random.randint(armour_chosen[2][0],armour_chosen[2][1])
	if category_of_armour=='light':
		strength_min=0
		endurance_min=0
	elif category_of_armour=='medium':
		strength_min=2
		endurance_min=3
	elif category_of_armour=='heavy':
		strength_min=4
		endurance_min=6
	return objects.Armour(name,weight,type_of_armour,protection,
							strength_min,endurance_min)

def create_weapon(category_of_weapon=None,range_of_weapon=None):
	if category_of_weapon==None:
		category_of_weapons=("light","medium","heavy")
		choice_of_category=random.randint(0,len(category_of_weapons)-1)
		category_of_weapon=category_of_weapons[choice_of_category]
	if range_of_weapon==None:
		range_of_weapons=['mele','distance']
		choice_of_range=random.randint(0,len(range_of_weapons)-1)
		range_of_weapon=range_of_weapons[choice_of_range]
	weapon_key="{} {}".format(category_of_weapon,range_of_weapon)
	caracterisation_weapon=copy.deepcopy(objects.weapons[weapon_key])
	choice_of_weapon=random.randint(0,len(caracterisation_weapon)-1)
	weapon_chosen=caracterisation_weapon[choice_of_weapon]
	name=weapon_chosen[0]
	weight=weapon_chosen[1]
	min_attack=random.randint(weapon_chosen[2][0][0],weapon_chosen[2][0][1])
	max_attack=random.randint(weapon_chosen[2][1][0],weapon_chosen[2][1][1])
	damage_range=[min_attack,max_attack]
	if range_of_weapon=='mele':
		distance=1
		intelligence_min=0
		if category_of_weapon=='light':
			strength_min=1
			agility_min=0
		elif category_of_weapon=='medium':
			strength_min=3
			agility_min=2
		elif category_of_weapon=='heavy':
			strength_min=6
			agility_min=4
	elif range_of_weapon=='distance':
		distance=25
		strength_min=0
		if category_of_weapon=='light':
			agility_min=1
			intelligence_min=0
		elif category_of_weapon=='medium':
			agility_min=3
			intelligence_min=2
		elif category_of_weapon=='heavy':
			agility_min=6
			intelligence_min=4
	return objects.Weapon(name,weight,distance,damage_range,
							strength_min,agility_min,intelligence_min)

def create_consumable(consumable_type=None,side_effect=None):
	if consumable_type==None:
		choice_of_consumable=random.randint(0,8)
		if choice_of_consumable==0:
			consumable_type='health potion'
		elif choice_of_consumable==1:
			consumable_type='mana potion'
		elif choice_of_consumable==2:
			consumable_type='stamina potion'
		else:
			consumable_type='food'
	if consumable_type=='health potion':
		life_points_gained=random.randint(1,6)*25
		weight=life_points_gained/100
		return objects.Potion("health potion ({})".format(life_points_gained),
								weight,life_points_gained,0,0)
	if consumable_type=='mana potion':
		mana_points_gained=random.randint(1,6)*10
		weight=mana_points_gained/40
		return objects.Potion("mana potion ({})".format(mana_points_gained),
								weight,0,mana_points_gained,0)
	if consumable_type=='stamina potion':
		stamina_points_gained=random.randint(1,6)*3
		weight=stamina_points_gained/12
		return objects.Potion("stamina potion ({})".format(stamina_points_gained),
								weight,0,0,stamina_points_gained)
	if consumable_type=='food':
		life_points_gained=random.randint(1,4)*5
		weight=life_points_gained/20
		if side_effect==None:
			gain_lose=random.randint(0,4)
			if gain_lose==0:
				gain_lose='gain'
			else:
				gain_lose='lose'
			effect=['strength','agility','endurance','intelligence','will','luck',
						'max_life_points','max_mana_points','max_stamina_points']
			choice_of_effect=random.randint(0,len(effect)-1)
			effect_chosen=effect[choice_of_effect]
			value_of_effect=random.randint(1,3)
			if effect_chosen=="max_life_points":
				value_of_effect=value_of_effect*15
			elif effect_chosen=="max_mana_points":
				value_of_effect=value_of_effect*10
			elif effect_chosen=="max_stamina_points":
				value_of_effect=value_of_effect*3
			number_of_rounds=random.randint(1,5)
			side_effect="{} {} {} for {} round(s)".format(gain_lose,value_of_effect,
															effect_chosen,number_of_rounds)
		name=objects.foods[random.randint(0,len(objects.foods)-1)]
		return objects.Food(name,weight,life_points_gained,side_effect)

def create_set_of_spells(character,number_of_spells=None,category_of_spells=None):
	if number_of_spells==None:
		number_of_spells=random.randint(0,3)
	spells_left=0
	while spells_left <number_of_spells:
		if category_of_spells==None:
			no_category=True
			category_of_spells=fights.type_of_spells[random.randint(0,len(fights.type_of_spells)-1)]
		else:
			no_category=False
		new_spells=copy.deepcopy(fights.spells[category_of_spells])
		number_spells_initial=len(character.list_of_spells)
		new_spell_index=0
		while len(character.list_of_spells)==number_spells_initial:
			if new_spell_index==len(new_spells):
				spells_left-=1
				category_of_spells=None
				break
			character.add_spell(new_spells[new_spell_index])
			new_spell_index+=1
		if no_category:
			category_of_spells=None
		spells_left+=1

def create_set_of_attacks(character,number_of_attacks=None,category_of_attacks=None):
	if number_of_attacks==None:
		number_of_attacks=random.randint(0,4)
	attacks_left=0
	while attacks_left <number_of_attacks:
		if category_of_attacks==None:
			no_category=True
			category_of_attacks=fights.type_of_attacks[random.randint(0,len(fights.type_of_attacks)-1)]
		else:
			no_category=False
		new_attacks=copy.deepcopy(fights.alternative_attacks[category_of_attacks])
		number_attacks_initial=len(character.list_of_attacks)
		new_attack_index=0
		while len(character.list_of_attacks)==number_attacks_initial:
			if new_attack_index==len(new_attacks):
				attacks_left-=1
				category_of_attacks=None
				break
			character.add_attack(new_attacks[new_attack_index])
			new_attack_index+=1
		if no_category:
			category_of_attacks=None
		attacks_left+=1

