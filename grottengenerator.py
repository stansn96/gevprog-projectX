from random import *
from spawn import *

class Grottengenerator():
	def __init__(self, plaatsSelf, plaatsWumpus):
		self.grottenlijst = []
		self.plaatsSelf = plaatsSelf
		self.plaatsWumpus = plaatsWumpus
		self.maakgrotten()
		self.grotstructuur()
		self.elementen()
		
	def maakgrotten(self):
		grotnummers = range(20)
		self.grotten = []
		for i in grotnummers:
			self.grotten.append([])
		return self.grotten
		
	def grotstructuur(self):
		self.grotten[0] = [1,[1,4,7], None]
		self.grotten[1] = [2,[0,2,9], None]
		self.grotten[2] = [3,[1,3,11], None]
		self.grotten[3] = [4,[2,4,13], None]
		self.grotten[4] = [5,[0,3,5], None]
		self.grotten[5] = [6,[4,6,14], None]
		self.grotten[6] = [7,[5,7,16], None]
		self.grotten[7] = [8,[0,6,8], None]
		self.grotten[8] = [9,[7,9,17], None]
		self.grotten[9] = [10,[1,8,10], None]
		self.grotten[10] = [11,[9,11,18], None]
		self.grotten[11] = [12,[2,10,12], None]
		self.grotten[12] = [13,[11,13,19], None]
		self.grotten[13] = [14,[3,12,14], None]
		self.grotten[14] = [15,[5,13,15], None]
		self.grotten[15] = [16,[14,16,19], None]
		self.grotten[16] = [17,[6,15,17], None]
		self.grotten[17] = [18,[8,16,18], None]
		self.grotten[18] = [19,[10,17,19], None]
		self.grotten[19] = [20,[12,15,18], None]
		return self.grotten
		
	def elementen(self):
		"""Voeg goud, vleermuizen en putten toe"""
		for grot in self.grotten:
			if grot[0] != self.plaatsSelf:
				keuzeelement = randrange(0,3)
				if randrange(0,11) <= 2:
					if keuzeelement == 0:
						grot[2] = 'goud'
					if keuzeelement == 1:
						grot[2] = 'vleermuizen'
					if keuzeelement == 2:
						grot[2] = 'put'
		return self.grotten

def main():
	plaatsSelf, plaatsWumpus = spawn()
	grot = Grottengenerator(plaatsSelf,plaatsWumpus)
	lijst = grot.elementen()
	print(lijst)
	
main()
