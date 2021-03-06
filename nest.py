from Comment import comment
from utils import *

class Nest:

	def say(self, msg):
		comment(msg)

	def __init__(self, ):
		#Protocol.readAnt()


		#self.food
		self.memory = []
		self.arrAntType = []
		self.arrAnt = []


	def __str__(self):
		return "Food : " + str(self.food) + " -- Memory : " + str(self.memory) + " -- AntType : " + str(self.arrAntType) +  " -- Ant : " + str(self.arrAnt) + " --"


	## INFORMATION

	def setFood(self, food):
		self.food = food

	def setMemory(self, memory):
		self.memory = memory

	def setMemoryLocation(self, index, memory):
		self.memory[index] = memory

	def setAntCount(self, t, quantity):
		self.arrAntType.append({"type" : t, "quantity" : quantity})

	def setAntIn(self, t, m1, m2):
		self.arrAnt.append({"type" : t, "m1" : m1, "m2" : m2})


	## ACTIONS

	def newAnt(self, t):
		self.setAntIn(t,0,0)
		print ("ANT_NEW " + str(t))

	def antOut(self, t, food, m0, m1):
		print ("ANT_OUT " + str(t) + " " + str(food) + " " + str(m0) + " " + str(m1))

	def commitMemory(self):
		arr = [str(s) for s in self.memory]
		print ("SET_MEMORY " + " ".join(arr))

	## Other

	def getAntCount(self, t):
		return compareKey("type",self.arrAntType,operator.eq,t)[0].get("quantity",0)
