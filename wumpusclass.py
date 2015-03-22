#wumpusclass.py
from grottengenerator import *
from spawn import *
from random import *

class Wumpus():
	def __init__(self, locatieheld):
		self.locatieheld = locatieheld
		self.xhero = locatieheld[0]
		self.yhero = locatieheld[1]
		
	def plaatswumpus(self):
		self.xpos= randrange(1,6)
		self.ypos=randrange(1,5)
		spawnplaatsWumpus = (self.xpos,self.ypos)
		while abs(self.xpos - self.xhero) <2:
			self.xpos= randrange(1,6)
		while abs(self.ypos - self.yhero) <2:     
			self.ypos=randrange(1,5)
		self.updatepositie()
		
	def movewumpus(self):
		randomgetal = randrange(1,5)
		if randomgetal == 1:
			self.xpos = self.xpos +1
		if randomgetal == 2:
			self.xpos = self.xpos -1
		if randomgetal == 3:
			self.ypos = self.ypos +1
		if randomgetal == 4:
			self.ypos = self.ypos -1
		self.updatepositie()
			
	def returnlocatiewumpus(self):
		return [self.xpos,self.ypos]
		
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
		
		
	def updatepositie():
		self.wumpuspositie = (self.xpos,self.ypos)
		return self.wumpuspositie
		
def main():
	wumpus1 = Wumpus((1,1),(2,4))
	wumpus1.jagen((2,4))
	
main()
