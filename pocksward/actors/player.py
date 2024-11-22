#import modules for all sub-.py files
import numpy as np
import random as random

class Player:
    '''Player is a class that contains all the definition of a pocksward player.'''

    def __init__(self, name, pitchNN, pitchSpeed, viewExponent, blockNN, blockSpeed, polarizeNN, hitNN, hitSkl, ageRate = 1, age = 0):
        '''
        Player is a class that contains all the definition of a pocksward player.
        name is a string that holds a players name
        stats is a numpy array containing the stats of a player by half year (before and after trade day), in the following format for each half-year
            [Year, Team, Pitch attepmts, Pitch successes, mean of Aetherization, std of Aetherization, Block atmpts, Block succsesse, avg movement on block, hit ]
        '''
        #import initiation vars
        self.name = name
        self.pitchNN = pitchNN
        self.pitchSpd = pitchSpeed
        self.blockNN = blockNN
        self.blockSpd = blockSpeed
        self.polarizeNN = polarizeNN
        self.hitNN = hitNN
        self.hitSkl = hitSkl
        self.ageRate = ageRate
        self.age = age

        #define empty data set
        self.stats = [] 

    def getName(self):
        return self.name
    
    def pitch(self, gameState, coachThought, fairground, x)
  