"""  Creation of the system of fights   """

"""Definition of classes for attacks and fight skills"""

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
	distance_foes=attacker_character.distance_to_instance(defender_character)
	if distance_foes>attacker_character.weapon.range:
		return 'distance too great'
	damage_min=8.0
	damage_max=40.0
	damage_weapon_min=4.0
	damage_weapon_max=35.0
	strength_min=1.0
	strength_max=9.0
	protection_min=5
	protection_max=80
	factor_strength=1/strength_min*(damage_min/damage_weapon_min+(damage_max/damage_weapon_max-damage_min*strength_max/(damage_weapon_min*strength_min))/(strength_max/strength_min-protection_min/protection_max))
	factor_protection=(damage_max/damage_weapon_max-damage_min*strength_max/(damage_weapon_min*strength_min))/(protection_max*strength_max/strength_min-protection_min)
	damaged_dealt=int(random.randint(damage[0],damage[1])*((factor_strength*(attacker_character.strength))-factor_protection*defender_character.body_protection))
	if damaged_dealt<1:
		damaged_dealt=1
	chance_to_touch=1-0.01*defender_character.agility+0.005*attacker_character.agility
	success=chance_to_touch>random.random()
	if success:
		defender_character.lose_lp(damaged_dealt)
		if defender_character.life_points<=0:
			death=defender_character.die()
			return death
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
		if attacker_character.intelligence<self.intelligence_min:
			return "intelligence too low"
		else:
			attacker_character.lose_mana(self.mana_required)
			damage_min=15.0
			damage_max=120.0
			damage_spell_min=6.0
			damage_spell_max=40.0
			intell_min=1.0
			intell_max=10.0
			will_min=1.0
			will_max=10.0
			factor_intelligence=1/intell_min*(damage_min/damage_spell_min+(damage_max/damage_spell_max-damage_min*intell_max/(damage_spell_min*intell_min))/(intell_max/intell_min-will_min/will_max))
			factor_will=(damage_max/damage_spell_max-damage_min*intell_max/(damage_spell_min*intell_min))/(will_max*intell_max/intell_min-will_min)
			damaged_dealt=int(random.randint(self.damage_range[0],self.damage_range[1])*((factor_intelligence*attacker_character.intelligence)-(defender_character.will*factor_will)))
			defender_character.lose_lp(damaged_dealt)
			if defender_character.life_points<=0:
				death=defender_character.die()
				return death

class Healing_spell(Spell):
	def __init__(self,name,distance,mana_required,life_points_gained,intelligence_min=0):
		Spell.__init__(self,name,distance,mana_required,None,intelligence_min)
		self.life_points_gained=life_points_gained
	def use_spell(self,launcher_character,receiver_character):
		if launcher_character.mana_points<self.mana_required:
			return "mana too low"
		if launcher_character.intelligence<self.intelligence_min:
			return "intelligence too low"
		else:
			life_points_restored=int(self.life_points_gained*0.75*(launcher_character.intelligence+1))
			receiver_character.gain_lp(life_points_restored)
			if receiver_character.life_points>receiver_character.max_life_points:
				receiver_character.life_points=receiver_character.max_life_points

class Alternative_attack(Special_attack):
	def __init__(self,name,distance,stamina_required,damage_range_add,type_of_weapon=None,
					strength_min=0,agility_min=0,endurance_min=0):
		Special_attack.__init__(self,name,distance)
		self.stamina_required=stamina_required
		self.damage_range_add=damage_range_add
		self.strength_min=strength_min
		self.agility_min=agility_min
		self.endurance_min=endurance_min
		self.type_of_weapon=type_of_weapon
	def attack(self,attacker_character,defender_character):
		if self.strength_min>attacker_character.strength:
			return "strength too low"
		elif self.agility_min>attacker_character.agility:
			return "agility too low"
		elif self.endurance_min>attacker_character.endurance:
			return "endurance too low"
		elif self.stamina_required>attacker_character.stamina_points:
			return "stamina too low"
		elif self.type_of_weapon!=None:
			if self.type_of_weapon!=attacker_character.weapon.range:
				return "wrong weapon"
		attacker_character.stamina_points-=self.stamina_required
		normal_damages=attacker_character.weapon.damage_range
		new_damages=[normal_damages[0]+self.damage_range_add[0],normal_damages[1]+self.damage_range_add[1]]
		attacker_character.weapon.damage_range=new_damages
		state_of_attack=plain_attack(attacker_character,defender_character)
		attacker_character.weapon.damage_range=normal_damages
		return state_of_attack

"""Beginning of fights with foes"""

def begin_fight(foe,main_character):
	if foe.detection_of_foe(main_character)=="detected":
		distance_main_character=foe.distance_to_instance(main_character)
		non_attacked=True
		foe_skills=foe.show_skills()
		response=""
		while non_attacked:
			if foe_skills[2]!=[]:
				for increment in range(len(foe_skills[2])):
					special_attack=foe_skills[2][increment]
					if special_attack.distance>distance_main_character:
						result=special_attack.attack(foe,main_character)
						if result==None or result=="miss" or result=="death":
							response="{} attacked {} with {}".format(foe,main_character,special_attack)
							break
			if response!="":
				break
			if foe_skills[0]!=[]:
				for increment in range(len(foe_skills[0])):
					spell=foe_skills[0][increment]
					if spell.distance>distance_main_character:
						result=spell.use_spell(foe,main_character)
						if result==None or result=="death":
							response="{} attacked {} with {}".format(foe,main_character,spell)
							break
			if response!="":
				break
			attack=plain_attack(foe,main_character)
			if attack!="distance too great":
				response="{} attacked {} with {}".format(foe,main_character,foe.weapon)
				break
			foe.go_to(main_character.x,main_character.y)
			response="{} gets closer to {}".format(foe,main_character)
			break
		return response
	return "undetected"

def keep_fighting(foe,main_character):
	inventory=foe.show_inventory()
	no_action=True
	for consumed_food in foe.consumed_inventory:
		consumed_food.end_effect(foe)
	response=""
	while no_action:
		if foe.life_points<0.25*foe.max_life_points:
			for potion in inventory:
				name_of_potion=potion.name.split()
				if name_of_potion[0]=='health':
					potion.use(foe)
					response="{} uses the {}".format(foe,potion)
					return response
		if foe.life_points<0.5*foe.max_life_points:
			for food in inventory:
				for element in objects.foods:
					if food.name==element:
						food.eat(foe)
						response="{} eats {}, restore {} health points and {}".format(foe,food,food.life_points_gained,food.side_effect)
						return response
		if foe.mana_points<0.2*foe.max_mana_points:
			for potion in inventory:
				name_of_potion=potion.name.split()
				if name_of_potion[0]=='mana':
					potion.use(foe)
					response="{} uses the {}".format(foe,potion)
					return response
		if foe.stamina_points<2:
			for potion in inventory:
				name_of_potion=potion.name.split()
				if name_of_potion[0]=='stamina':
					potion.use(foe)
					response="{} uses the {}".format(foe,potion)
					return response
		choice_of_attack=random.randint(1,12)
		foe_skills=foe.show_skills()
		distance_main_character=foe.distance_to_instance(main_character)
		if foe.life_points<0.25*foe.max_life_points:
			if foe_skills[1]!=[]:
				for increment in range(len(foe_skills[1])-1,0,-1):
					healing_spell=foe_skills[1][increment]
					result=healing_spell.use_spell(foe,foe)
					if result==None :
						response="{} used {} to restore {} health points".format(foe,healing_spell,healing_spell.life_points_gained)
						return response
		if choice_of_attack==1 or choice_of_attack==2 or choice_of_attack==3:
			if foe_skills[2]!=[]:
				for increment in range(len(foe_skills[2])):
					special_attack=foe_skills[2][increment]
					if special_attack.distance>distance_main_character:
						life_points_of_character_initial=main_character.life_points
						result=special_attack.attack(foe,main_character)
						life_points_of_character_final=main_character.life_points
						if result==None or result=="miss" or result=="death":
							damage_dealt=life_points_of_character_initial-life_points_of_character_final
							response="{} attacked {} with {} and dealt {} damages".format(foe,main_character,special_attack,damage_dealt)
							return response
		if choice_of_attack==4 or choice_of_attack==5:
			if foe_skills[0]!=[]:
				for increment in range(len(foe_skills[0])):
					spell=foe_skills[0][increment]
					if spell.distance>distance_main_character:
						life_points_of_character_initial=main_character.life_points
						result=spell.use_spell(foe,main_character)
						life_points_of_character_final=main_character.life_points
						if result==None or result=="death":
							damage_dealt=life_points_of_character_initial-life_points_of_character_final
							response="{} attacked {} with {} and dealt {} damages".format(foe,main_character,spell,damage_dealt)
							return response
		life_points_of_character_initial=main_character.life_points
		attack=plain_attack(foe,main_character)
		life_points_of_character_final=main_character.life_points
		if attack!="distance too great":
			damage_dealt=life_points_of_character_initial-life_points_of_character_final
			response="{} attacked {} with {} and dealt {} damages".format(foe,main_character,foe.weapon,damage_dealt)
			return response
		foe.go_to(main_character.x,main_character.y)
		response="{} gets closer to {}".format(foe,main_character)
		return response
	return response		





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""								""""""list of Spells""""""                             """
fireflamme=Spell('fire flamme',15,8,[12,15],2)
fireball=Spell('fire ball',18,12,[16,20],4)
firemeteor=Spell('fire meteor',18,20,[25,35],7)
shock=Spell('shock',25,5,[6,10],2)
lightbolt=Spell('light bolt',20,15,[18,22],5)
lightnings=Spell('lightnings',20,20,[28,32],8)
frost=Spell('frost',8,10,[14,18],3)
iceprison=Spell('ice prison',5,25,[30,38],8)

""""""""""""""""""""""""""""""""""""
firstaid=Healing_spell('first aid',5,8,30,2)
firstaid_extended=Healing_spell('first aid extended',15,13,30,2)
healing=Healing_spell('healing',5,15,70,4)
healing_extended=Healing_spell('healing extended',15,20,70,4)
restoration=Healing_spell('restoration',5,25,130,7)
restoration_extended=Healing_spell('restoration extended',5,30,130,7)

""""""""""""""""""""""""""""""""""""
type_of_spells=['fire','electricity','ice']

""""""""""""""""""""""""""""""""""""
spells={'fire':[fireflamme,fireball,firemeteor],
		'electricity':[shock,lightbolt,lightnings],
		'ice':[frost,iceprison],
		'healing':[firstaid,firstaid_extended,healing,healing_extended,restoration,restoration_extended]}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""						""""""list of Alternative Attacks""""""                         """
jump=Alternative_attack('jump attack',5,2,[5,5],'mele',1,0,1)
doublejump=Alternative_attack('double jump',10,3,[5,5],'mele',2,1,3)
triplejump=Alternative_attack('triple jump',15,4,[5,5],'mele',3,2,4)
leap_of_faith=Alternative_attack('leap of faith',15,6,[10,10],'mele',5,3,6)
blow=Alternative_attack('weapon blow',1,1,[3,6],2,0,0)
strongblow=Alternative_attack('strong blow',1,2,[5,8],4,1,1)
powerfulblow=Alternative_attack('powerful blow',1,3,[8,10],6,2,3)
fire_ignition=Alternative_attack('fire ignition',25,2,[3,4],None,0,2,1)
piercing_arrows=Alternative_attack('piercing arrows',25,2,[3,3],0,1,0)
long_range_arrows=Alternative_attack('long-range arrows',40,4,[4,4],2,4,1)

""""""""""""""""""""""""""""""""""""
type_of_attacks=['jump','mele blow','essence','arrows']

""""""""""""""""""""""""""""""""""""
alternative_attacks={'jump':[jump,doublejump,triplejump,leap_of_faith],
					'mele blow':[blow,strongblow,powerfulblow],
					'essence':[fire_ignition],
					'arrows':[piercing_arrows,long_range_arrows]}

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""