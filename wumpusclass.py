#wumpusclass.py
from grottengenerator import *
from spawn import *
from random import *

class Wumpus():
	def __init__(self, locatiewumpus, locatieheld):
		self.locatiewumpus = [locatiewumpus[0],locatiewumpus[1]]
		
	def respawnwumpus(self,locatiewumpus):
		locatiewumpus = self.locatiewumpus
		spawnplaatsSelf = (xhero,yhero)
		self.xwumpus= locatiewumpus[0]
		self.ywumpus= locatiewumpus[1]
		randomgetal = randrange(1,5)
		if randomgetal == 1:
			self.xwumpus = self.xwumpus +1
		if randomgetal == 2:
			self.xwumpus = self.xwumpus -1
		if randomgetal == 3:
			self.ywumpus = self.ywumpus +1
		if randomgetal == 4:
			self.ywumpus = self.ywumpus -1
			
	def returnlocatiewumpus(self):
		return [self.xwumpus,self.ywumpus]
