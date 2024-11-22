import numpy as np


class Fairground:
    '''
    The Fairground is the field or stadium of the game of Pocksward.
    For all intents and purposes, it's a 1D 'golf course' with a heightmap,
    Aethermap, and Planar map. Hitters can choose if they want to hit in Aetherspace or Planarspace
    '''
    def __init__(self, name, planeFunct, aetherFunct, heightFunct):
        '''
        The Fairground is the field or stadium of the game of Pocksward.
        Name is a string that is the fields name.
        planeFunct, aetherFunct, and heighFunct are all 1-D functions that will return a field value for a given position x
        
        '''
        self.name = name
        self.plane = planeFunct
        self.aether = aetherFunct
        self.height = heightFunct

    def getName(self):
        return self.name
    
    def getPlanarValue(self, x):
        return self.plane(x)
    
    def getAetherValue(self, x):
        return self.aether(x)
    
    def getHeightDiff(self, x0, x1):
        return self.height(x1) - self.height(x0)