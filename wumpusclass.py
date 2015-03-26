#wumpusclass.py
from grottengenerator import *
from spawn import *
from random import *

"""Class voor het aanmaken van de Wumpus"""
class Wumpus():
	def __init__(self, locatieheld):
		self.xposheld = locatieheld[0]
		self.yposheld = locatieheld[1]
		self.plaatswumpus()
		
	def getplaatswumpus(self):
		return self.xpos, self.ypos
		
	def plaatswumpus(self):
		self.xpos= randrange(1,6)
		self.ypos=randrange(1,5)
		spawnplaatsWumpus = (self.xpos,self.ypos)
		"""Check of de wumpus wel 2 stappen van de hero af gespawnt wordt"""
		while abs(self.xpos - self.xposheld) <2:
			self.xpos= randrange(1,6)
		while abs(self.ypos - self.yposheld) <2:     
			self.ypos=randrange(1,5)
		self.updatepositie()
		
	"""Functie voor het bewegen van de Wumpus bij gemist schot, wordt dus niet gebruikt"""	
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
		if self.xpos == 0:
			self.xpos = 5
		if self.xpos == 6:
			self.xpos = 1
		if self.ypos == 0:
			self.ypos = 4
		if self.ypos == 5:
			self.ypos = 1
		self.updatepositie()
			
	def returnlocatiewumpus(self):
		return [self.xpos,self.ypos]
		
	def jagen(self,locatieheld):
		"""Wumpus via snelst mogelijke route laten jagen op de hero"""
		self.xposheld, self.yposheld = locatieheld
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
				
		if self.xpos < 1:
			self.xpos = 5
		if self.xpos > 5:
			self.xpos = 1
		if self.ypos < 1:
			self.ypos = 5
		if self.ypos > 5:
			self.ypos = 1
		
		self.updatepositie()
		
	def updatepositie(self):
		self.wumpuspositie = (self.xpos,self.ypos)
		return self.wumpuspositie
		
