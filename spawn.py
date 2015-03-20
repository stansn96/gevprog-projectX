#spawn.py
from random import *

def spawn():
    xhero= randrange(1,6)
    yhero=randrange(1,5)
    spawnplaatsSelf = (xhero,yhero)
    xwumpus= randrange(1,6)
    ywumpus=randrange(1,5)
    spawnplaatsWumpus = (xwumpus,ywumpus)
    while abs(xwumpus - xhero) <2:
        xwumpus= randrange(1,6)
    while abs(ywumpus - yhero) <2:     
        ywumpus=randrange(1,5)
    spawnplaatsWumpus = (xwumpus,ywumpus)
    return spawnplaatsSelf,spawnplaatsWumpus
    

