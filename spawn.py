#spawn.py
from random import *

def spawn():
	spawnplaatsSelf = randrange(1,21)
	spawnplaatsWumpus = randrange(1,21)
	if spawnplaatsWumpus == spawnplaatsSelf:
		spawnplaatsWumpus = randrange(1,21)
	return spawnplaatsSelf,spawnplaatsWumpus


