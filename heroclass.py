#heroclass.py
from grottengenerator import *
from spawn import *
from wumpusclass import *

class Hero():
	def __init__(self,naam,locatieheld):
		self.naam = naam
		self.pijlen = 3
		self.gold = 0
		self.locatieheld = [locatieheld[0],locatieheld[1]]
		self.winst = False
		
	def returnlocatieheld(self):
		return self.locatieheld
		
	def goudgevonden(self):
		self.goud = self.goud + 1
		return self.goud
	
	def goudaantal(self):
		return self.goud
		
	def pijlaantal(self):
		return self.pijlen
	
	def schieten(self,wumpuslocatie):
		self.pijlxcoor = self.locatieheld[0]
		self.pijlycoor = self.locatieheld[1]
		self.richting = ""
		if self.richting == "links":
				self.pijlxcoor = self.pijlxcoor - 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.richting == "rechts":
				self.pijlxcoor = self.pijlxcoor + 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.richting == "omhoog":
				self.pijlycoor = self.pijlycoor - 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.richting == "omlaag":
				self.pijlycoor = self.pijlycoor + 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
		


def main():
	spawnplaatsSelf, spawnplaatsWumpus = spawn()    
	grot = Grottengenerator(spawnplaatsSelf, spawnplaatsWumpus)
	held = Hero('Stan',grot.returnherocoords())
	wumpus = Wumpus([1,1],held.returnlocatieheld)
	print(held.returnlocatieheld())
	
main()
