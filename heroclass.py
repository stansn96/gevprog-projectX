#heroclass.py
from grottengenerator import *
from spawn import *
from wumpusclass import *

class Hero():
	def __init__(self,naam):
		self.naam = naam
		self.pijlen = 3
		self.goud = 0
		self.winst = False
		self.dood = False
		self.plaatsen()
		
	def plaatsen(self):
		self.xcoor = randrange(1,6)
		self.ycoor = randrange(1,5)
		self.updatepositie()
	
	def herplaatsen(self,wumpuspositie):
		self.xcoor = randrange(1,6)
		self.ycoor = randrange(1,5)
		if (self.xcoor, self.ycoor) == wumpuspositie:
			self.herplaatsen()
		else:
			self.updatepositie()
	
	def herplaatsen1(self,wumpuspositie):
		self.xcoor = randrange(1,6)
		self.ycoor = randrange(1,5)
		if (self.xcoor, self.ycoor) == wumpuspositie:
			self.herplaatsen1()
		else:
			return self.xcoor, self.ycoor
		
	def returnlocatieheld(self):
		return self.positie
		
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
		
	def moveup(self):
		self.ycoor -= 1  # due to inverted coordinates of UI
		if self.ycoor < 1:
			self.ycoor = 4
		self.updatepositie()

	def moveright(self):
		self.xcoor += 1
		if self.xcoor > 5:
			self.xcoor = 1
		self.updatepositie()

	def movedown(self):
		self.ycoor += 1  # due to inverted coordinates of UI
		if self.ycoor > 4:
			self.ycoor = 1
		self.updatepositie()

	def moveleft(self):
		self.xcoor -= 1
		if self.xcoor < 1:
			self.xcoor = 5
		self.updatepositie()
			
	def updatepositie(self):
		self.positie = (self.xcoor,self.ycoor)
		return self.positie




