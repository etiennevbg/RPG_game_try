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
		if attacker_character.intelligence<intelligence_min:
			return "intelligence too low"
		else:
			attacker_character.lose_mana(self.mana_required)
			damaged_dealt=int(random.randint(self.damage_range[0],self.damage_range[1])*1.25*(attacker_character.intelligence+1)-(defender_character.will+1)*1.5)
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
		if launcher_character.intelligence<intelligence_min:
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
	def attack(self,attacker_character,defender_character):
		if self.strength_min>attacker_character.strength:
			return "strength too low"
		elif self.agility_min>attacker_character.agility:
			return "agility too low"
		elif self.endurance_min>attacker_character.endurance:
			return "endurance too low"
		elif self.stamina_required>attacker_character.stamina_points:
			return "stamina too low"
		elif type_of_weapon!=None:
			if type_of_weapon!=attacker_character.weapon.range:
				return " wrong weapon"
		attacker_character.stamina_points-=self.stamina_required
		normal_damages=attacker_character.weapon.damage_range
		new_damages=[normal_damages[0]+self.damage_range_add[0],normal_damages[1]+self.damage_range_add[1]]
		attacker_character.weapon.damage_range=new_damages
		state_of_attack=plain_attack(attacker_character,defender_character)
		attacker_character.weapon.damage_range=normal_damages
		return state_of_attack


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
firstaid=Healing_spell('first aid',5,8,15,2)
firstaid_extended=Healing_spell('first aid extended',15,113,15,2)
healing=Healing_spell('healing',5,15,40,4)
healing_extended=Healing_spell('healing extended',15,20,40,4)
restoration=Healing_spell('restoration',5,25,80,7)
restoration_extended=Healing_spell('restoration extended',5,30,80,7)

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