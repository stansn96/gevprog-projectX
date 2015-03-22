#heroclass.py
from grottengenerator import *
from spawn import *
from wumpusclass import *

class Hero():
	def __init__(self,naam):
		self.naam = naam
		self.pijlen = 3
		self.gold = 0
		self.locatieheld = [locatieheld[0],locatieheld[1]]
		self.winst = False
		self.plaatsen()
		
	def plaatsen(self):
		self.xcoor = randrange(1,6)
		self.ycoor = randrange(1,5)
		self.updatepositie()
	
	def herplaatsen(self):
		self.xcoor = randrange(1,6)
		self.ycoor = randrange(1,5)
		if (self.xcoor, self.ycoor) == self.wumpuspositie:
			self.herplaatsen()
		else:
			self.updatepositie()
			
	def returnxylocatieheld(self):
		return self.xcoor, self.ycoor
		
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
		self.pijlxcoor = self.xcoor
		self.pijlycoor = self.ycoor
		self.pijlrichting = ""
		if self.pijlrichting == "links":
				self.pijlxcoor = self.pijlxcoor - 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.pijlrichting == "rechts":
				self.pijlxcoor = self.pijlxcoor + 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.pijlrichting == "omhoog":
				self.pijlycoor = self.pijlycoor - 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
					
		if self.pijlrichting == "omlaag":
				self.pijlycoor = self.pijlycoor + 1
				if (self.pijlxcoor,self.pijlycoor) == wumpuslocatie:
					self.winst = True
				else: 
					wumpus.respawnwumpus()
		
		def __str__(self):
			return "Naam van de held: {} Positie(x,y) {} Aantal goud: {} Aantal pijlen: {}".format(self.naam,self.positie,self.goud,self.pijlen)
			
		def updatepositie():
			self.positie = (self.xcoor,self.ycoor)
			return self.positie
		


def main():   
	held = Hero('Stan',grot.returnherocoords())
	heldplaats = held.plaatsen()
	wumpus = Wumpus(heldplaats)
	grot = Grottengenerator(heldplaats, wumpus.plaatsen())
	
	wumpus = Wumpus([1,1],held.returnlocatieheld)
	print(held.returnlocatieheld())
	
main()
