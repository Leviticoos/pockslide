#Leviticus Rhoden's Pocksward library
#Classes for players, coaches, teams, and data storage
#Functions for simulating game steps
#Class for packaging game steps into games


import numpy as np
import matplotlib.pyplot as plt


#Game Code

class Game:


#Peaple Code

class Player:
    '''Player is a class that contains the player's skill vector, nerual net, TODO'''

    def __init__(self, sklVect, sitAware, sitAct):
        #Define behavior controling variables
        self.skillVector = np.array(sklVect)
        self.sitAware = np.array(sitAware)
        self.sitAct = np.array(sitAct)

        #define empty data set
        self.stats = [] #2D array arguments: Year, Team, Launches, unitsFromLaunches, Swats, unitsFromSwats, 

    def sklVector(self):
        #gives players skill vector
        return self.sklVector
    
    def think(self, gameState):
        #takes in the state of the game (tbd) and uses a baby N.N. to determine what action player will try to preform
        sitConcept = self.sitAware.dot(gameState)
        actVector = self.sitAct.dot(sitConcept)
        return actVector
    

class Coach:
    '''IDK What a coach will do yet'''


class Team:
    '''Team is a class that contains a coach, a list of players (5), stats, and a N.N. to control personel decisions'''


