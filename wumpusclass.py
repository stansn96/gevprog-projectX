#wumpusclass.py
from grottengenerator import *
from spawn import *
from random import *

class Wumpus():
	def __init__(self, locatiewumpus, locatieheld):
		self.locatiewumpus = [locatiewumpus[0],locatiewumpus[1]]
		self.xpos = locatiewumpus[0]
		self.ypos = locatiewumpus[1]
		
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
		
	def jagen(self,locatieheld):
		self.xposheld = locatieheld[0][0]
		self.yposheld = locatieheld[0][1]
		xafstand = abs(self.xpos - self.xposheld)
		yafstand = abs(self.ypos - self.yposheld)
		if self.xpos > self.xposheld:
			bewegingx = "links"
		else:
			bewegingx = "rechts"
		if self.ypos > self.yposheld:
			bewegingy = "omhoog"
		else:
			bewegingy = "omlaag"
		if xafstand > yafstand:
			if bewegingx == "links":
				self.xpos = self.xpos -1
			else:
				self.xpos = self.xpos +1
		else:
			if bewegingy == "omhoog":
				self.ypos = self.ypos -1
			else:
				self.ypos = self.ypos +1
		print(self.xpos,self.ypos)
		
def main():
	wumpus1 = Wumpus((1,1),(2,4))
	wumpus1.jagen((2,4))
	wumpus1.jagen((2,4))
	wumpus1.jagen((2.4))
	wumpus1.jagen((2.4))
	
main()
