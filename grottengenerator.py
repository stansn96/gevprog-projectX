from random import *
from spawn import spawn

"""Class voor het genereren van grotten"""
class Grottengenerator():
        def __init__(self, spawnplaatsSelf, spawnplaatsWumpus):
                self.grottenlijst = []
                self.maakgrotten()
                self.spawnplaatsSelf=spawnplaatsSelf
                self.spawnplaatsWumpus=spawnplaatsWumpus
                self.elementen()
                
        """Maak een lijst met coordinaten van de grotten aan"""        
        def maakgrotten(self):
                self.grotten = []
                for y in range(1,5):
                        for x in range(1,6):
                                self.grotten.append([(x,y), None])
                return self.grotten

        def elementen(self):
                """Voeg goud, vleermuizen en putten toe"""
                for grot in self.grotten:
                        if grot[0] != self.spawnplaatsSelf:
                                keuzeelement = randrange(0,3)
                                if randrange(0,8) == 0:
                                        if keuzeelement == 0:
                                                grot[1] = 'Goud'
                                        if keuzeelement == 1:
                                                grot[1] = 'Vleermuis'
                                        if keuzeelement == 2:
                                                grot[1] = 'Put'
                return self.grotten

        def returngrotten(self):
                return self.grotten
