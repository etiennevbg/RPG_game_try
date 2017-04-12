import initializes
import fights
import time

a=float(time.clock())
ogre1=initializes.create_foe("ogre low level")
b=float(time.clock())
spider=initializes.create_foe("spider low level")


ogre1.set_to_position(10,12)
undetected=True
i=0
surprise=True
while surprise:
	while undetected:
		start_fight=fights.begin_fight(ogre1,spider)
		i+=1
		if start_fight!="undetected":
			attacker=ogre1
			print("\nogre1 is the attacker\n")
			defender=spider
			print ('detection happened at the {} round\n'.format(i))
			break
		start_fight=fights.begin_fight(spider,ogre1)
		if start_fight!="undetected":
			attacker=ogre1
			print("spider is the attacker\n")
			defender=spider
			print ('detection happened at the {}th round\n'.format(i))
			break
	undetected=False
	print("defender has {} hp".format(defender.life_points))
	fight1=fights.keep_fighting(attacker,defender)
	print(fight1)
	print("defender has {} hp\n".format(defender.life_points))
	if defender.die()=="death":
		surprise=False
		break
	print("attacker has {} hp".format(attacker.life_points))
	fight2=fights.keep_fighting(defender,attacker)
	print(str(fight2))
	print("attacker has {} hp\n\n".format(attacker.life_points))
	if attacker.die()=="death":
		surprise=False
		break
print(ogre1.die(),spider.die())

