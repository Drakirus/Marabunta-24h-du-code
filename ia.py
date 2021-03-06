import operator
from utils import *
from wrapper import Protocol
from Comment import comment, bcolors
import time
from random import randint

# import Protocol

ANT_ECLAIREUR = 0
ANT_RAMASSEUR = 1
PH_NEED_RECHARGE = 30
STAMINA_NEED_EAT = 100
DISTANCE_NEED_PUT_PH = 90


def antIA(ant):
	# ANT PROGRAM

	#  time.sleep(1)

	if ant.type == ANT_ECLAIREUR:
		comment("ANT_ECLAIREUR", bcolors.OKGREEN)
		lastIdPaht = []
		lastIdPaht.append(0)
		for ph in ant.arrSeePheromone:
			lastIdPaht.append(ph["type"])
		idPathStart = max(lastIdPaht)

		if ant.stamina < STAMINA_NEED_EAT and ant.food > 0:
			ant.say("ant-eat")
			ant.eat(1)
			return

		gotFood     = (ant.m2 == 1 or ant.m2 == 2)
		needMove = (ant.m2 == 1)

		if idPathStart > ant.m1 and not gotFood:
			ant.say("SUICIDE")
			ant.suicide()
			return


		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.say("ON BOUFFE, ON NEED DE LA STAMINA")
			ant.suicide()
			return

		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		nearest = compareKey("area", phs, operator.eq, "NEAR")
		needRefuel = compareKey("persistance", nearest, operator.lt, PH_NEED_RECHARGE)



		#  if len(needRefuel) > 0:
			#  ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			#  ant.rechargePheromone(needRefuel[0]["id"])
			#  return

		# farPh = la phs la plus loin
		# HOME RETURN


		id_min = 0
		type_min = 99999999999
		for ph in ant.arrSeePheromone:
			if type_min > ph["type"]:
				id_min = ph["id"]
				type_min = ph["type"]
		if gotFood:

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'FAR':
				ant.say("ON SE DIRIGE VERS LE BERCAIL")
				ant.moveTo(ant.arrSeeNest[0]["id"])
				return

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'NEAR':
				ant.say("BERCAIL")
				ant.nest(ant.arrSeeNest[0]["id"])
				return

			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")

			if needMove:
				ant.setMemory(ant.m1, 2)
				ant.moveTo(id_min)
			else :

				ant.setMemory(ant.m1, 1)
				nearestPhero = [ x for x in ant.arrSeePheromone if x["area"] == "NEAR"]


				if not nearestPhero:
					ant.setMemory(ant.m1, 2)
					ant.moveTo(id_min)
				else:

					a = minMaxKey("dist",nearestPhero,min)
					ant.rechargePheromone(a)

			ant.commitMemory()
			return

		# partie calcul min distance
		ant.say("test")
		phs = [ x for x in phs if x["dist"] < DISTANCE_NEED_PUT_PH ]
		ant.say("phs" + str(phs))

		if not phs:
			ant.say("ON A BESOIN DE PLACER UN PHEROMONE, INIT")
			ant.putPheromone(idPathStart + 1)
			return


		#  ant.say("idPathStart" + str(idPathStart))
		#  ant.say("arrSeePheromone" + str(ant.arrSeePheromone))


		ant.say("arrSeeFood" + str(ant.arrSeeFood))
		if ant.arrSeeFood:

			nearestFoodSrc = [ x for x in ant.arrSeeFood if x["area"] == 'NEAR']

			if nearestFoodSrc:
				ant.say("ON RECUPERE DE LA BOUFFE")
				ant.collect(nearestFoodSrc[0]["id"],  min(nearestFoodSrc[0]["amount"], ant.FOOD_MAX) - 1)
				ant.setMemory(idPathStart + 10, 2)
				ant.commitMemory()
				return

			else:
				ant.say("ON SE DIRIGE VERS LA BOUFFE")
				ant.moveTo(ant.arrSeeFood[0]["id"])
				return


		#  s = sorted(ant.arrSeePheromone, key = lambda x: (x["persistance"], x["type"]))
		#  if s and randint(0, 1000) < 2:
			#  ant.moveTo(s[0]["id"])
			#  return

		#  ant.say("arrSeePheromone ==" + str(ant.arrSeePheromone))
		ant.explore()
		ant.say("ON A RIEN TROUVE, ON EXPLORE")

		return

	elif ant.type == ANT_RAMASSEUR:
		comment("ANT_RAMASSEUR", bcolors.OKGREEN)

		lastIdPaht = []
		lastIdPaht.append(0)
		for ph in ant.arrSeePheromone:
			lastIdPaht.append(ph["persistance"])
		idPathStart = max(lastIdPaht)
		comment("idPathStart: " + str(idPathStart))


		gotFood     = (ant.m2 == 1 or ant.m2 == 2)
		needMove = (ant.m2 == 1)

		#  if not gotFood:
			#  ant.say("SUICIDE")
			#  ant.suicide()
			#  return

		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.say("ON BOUFFE, ON NEED DE LA STAMINA")
			ant.eat(1)
			return

		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		nearest = compareKey("area", phs, operator.eq, "NEAR")
		needRefuel = compareKey("persistance", nearest, operator.lt, PH_NEED_RECHARGE)



		#  if len(needRefuel) > 0:
			#  ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			#  ant.rechargePheromone(needRefuel[0]["id"])
			#  return

		# farPh = la phs la plus loin
		# HOME RETURN


		id_min = 0
		pers_min = 99999999999
		for ph in ant.arrSeePheromone:
			if pers_min > ph["persistance"]:
				id_min = ph["id"]
				pers_min = ph["persistance"]

		if gotFood:

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'FAR':
				ant.say("ON SE DIRIGE VERS LE BERCAIL")
				ant.moveTo(ant.arrSeeNest[0]["id"])
				return

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'NEAR':
				ant.say("BERCAIL")
				ant.nest(ant.arrSeeNest[0]["id"])
				return

			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")

			if needMove:
				ant.setMemory(ant.m1, 2)
				ant.moveTo(pers_min)
			else :

				ant.setMemory(ant.m1, 1)
				nearestPhero = [ x for x in ant.arrSeePheromone if x["area"] == "NEAR"]


				if not nearestPhero:
					ant.setMemory(ant.m1, 2)
					ant.moveTo(pers_min)
				else:

					a = minMaxKey("dist",nearestPhero,min)
					ant.rechargePheromone(a)



		ant.say("arrSeeFood" + str(ant.arrSeeFood))
		if ant.arrSeeFood:

			nearestFoodSrc = [ x for x in ant.arrSeeFood if x["area"] == 'NEAR']

			if nearestFoodSrc:
				ant.say("ON RECUPERE DE LA BOUFFE")
				ant.collect(nearestFoodSrc[0]["id"],  min(nearestFoodSrc[0]["amount"], ant.FOOD_MAX))
				ant.setMemory(ant.m1, 2)
				ant.commitMemory()
				return

			else:
				ant.say("ON SE DIRIGE VERS LA BOUFFE")
				ant.moveTo(ant.arrSeeFood[0]["id"])
				return

		ant.moveTo(id_min)
		return


	return

NB_ANT_CREATED = 0
KILL_AT_PH = 1

def nestIA(nest):
	# NEST PROGRAM

	comment(str(nest), bcolors.OKBLUE)

	if nest.memory[KILL_AT_PH] == 0:
		nest.memory[KILL_AT_PH] = 70
		nest.commitMemory()

	if nest.arrAnt:
		comment("capitalize create rama", bcolors.OKGREEN)
		nest.memory[KILL_AT_PH] = int(nest.arrAnt[0]["m1"] * 1.3)
		nest.commitMemory()
		nest.newAnt(ANT_RAMASSEUR)
		return


	if nest.arrAntType:
		nest.antOut(nest.arrAntType[0]["type"], 3, nest.memory[KILL_AT_PH], 0)
		return

	if nest.memory[NB_ANT_CREATED] < 1:
		comment("capitalize create ant", bcolors.OKGREEN)
		nest.memory[NB_ANT_CREATED] += 2
		nest.commitMemory()
		nest.newAnt(ANT_ECLAIREUR)
		return

	elif randint(0, 200) < 1:
		comment("random create ant", bcolors.OKGREEN)
		nest.memory[NB_ANT_CREATED] = 1
		nest.memory[KILL_AT_PH] = int(nest.memory[KILL_AT_PH]+1 * 1.5)
		nest.commitMemory()
		nest.newAnt(ANT_ECLAIREUR)
		return

	#  elif randint(0, 10) < 1:
		#  comment("random create ant", bcolors.OKGREEN)
		#  nest.memory[NB_ANT_CREATED] = 1
		#  nest.memory[KILL_AT_PH] = int(nest.memory[KILL_AT_PH]+1 * 1.5)
		#  nest.commitMemory()
		#  nest.newAnt(ANT_RAMASSEUR)
		#  return


while True:
	nameEntity, entity = Protocol.readInput()
	comment(nameEntity)
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)

	Protocol.exit()
