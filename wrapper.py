import sys
from ant import Ant
from nest import Nest
from Comment import comment



# sys.stdout.flush()




class Protocol:

	@classmethod
	def exit(cls):
		print("END")

	@classmethod
	def readInput(cls):
		firstLine = input()
		name = firstLine.split()[1]

		obj = None
		if name == 'ANT':
			obj = cls.readAnt()
		elif name == 'NEST':
			obj = cls.readNest()

		return [name, obj]

	@classmethod
	def readAnt(cls):
		line = input().split()
		ant = Ant()
		while line[0] != 'END':
			cmd = line[0]
			args = line[1:]
			if cmd == 'TYPE':
				t = int(args[0])
				ant.setType(t)

			elif cmd == 'MEMORY':
				m1, m2 = [int(v) for v in args]
				ant.setMemory(m1, m2)

			elif cmd == 'ATTACKED':
				ant.setAttacked()

			elif cmd == 'STAMINA' :
				stamina = int(args[0])
				ant.setStamina(stamina)

			elif cmd == 'STOCK':
				food = int(args[0])
				ant.setFood(food)

			elif cmd == 'SEE_PHEROMONE':
				ident, zone, dist, typePheromone, persistance = args
				ident = int(ident)
				dist = int(dist)
				typePheromone = int(typePheromone)
				persistance = int(persistance)
				ant.setSeePheromone(ident, zone, dist, typePheromone, persistance)

			elif cmd == 'SEE_ANT':
				ident, zone, dist, friend, stamina = args
				ident = int(ident)
				dist = int(dist)
				stamina = int(stamina)
				ant.setSeeAnt(ident, zone, dist, friend, stamina)

			elif cmd == 'SEE_NEST':
				ident, zone, dist, friend = args
				ident = int(ident)
				dist = int(dist)
				ant.setSeeNest(ident, zone, dist, friend)

			elif cmd == 'SEE_FOOD':
				ident, zone, dist, amount = args
				ident = int(ident)
				dist = int(dist)
				amount = int(amount)
				ant.setSeeFood(ident, zone, dist, amount)


			line = input().split()
		return ant

	@classmethod
	def readNest(cls):
		line = input().split()
		nest = Nest()
		while line[0] != 'END':
			cmd = line[0]
			args = line[1:]
			if cmd == 'STOCK':
				qtt = args[0]
				qtt = int(qtt)
				nest.setFood(qtt)

			elif cmd == 'MEMORY':
				tab_mem = [int(v) for v in args]
				nest.setMemory(tab_mem)

			elif cmd == 'ANT_COUNT':
				typ, qtt = [int(v) for v in args]
				nest.setAntCount(typ, qtt)

			elif cmd == 'ANT_IN':
				typ, m1, m2 = [int(v) for v in args]
				nest.setAntIn(typ, m1, m2)

			line = input().split()

		return nest

if __name__ == '__main__':
	t, obj = Protocol.readInput()
	comment(str(obj))
	comment(str(t))
	print("ANT_NEW 4")
	Protocol.exit()
