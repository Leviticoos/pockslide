#Leviticus Rhoden's Pocksward library
#Classes for players, coaches, teams, and data storage
#Functions for simulating game steps
#Class for packaging game steps into games


import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
import random


#Game Code

class Check:
    def __init__(self, skillTransform,timeScale,n=1, helpText=''):
        '''
        Define a check, which is a base unit of a play. Takes in a skill transform, which will map an action vector to different skills, and possibly 
        n is an intager that represents how many chances you have to succseed. This is a way of letting low chances be more likely. 
        helpText, which can be your notes on what this check is.
        
        Conceptually, a check is a single pass/fail unit of the sport. The player will set their action vector, and 
        '''
        self.playTrans = np.array(skillTransform)
        self.n = int(n)
        self.help = helpText
        self.scale = timeScale

    def help(self):
        return self.help
    
    def run(self, playVtr, actVtr, sklVtr, verbose=False):
        '''
        playVtr is a 1D vector that defines the current play vector. If it's a thrown ball, think of it as how it was thrown. It will be modified per the check's play Transform Vector. Must be n long.
        actVtr is a 1D vector, same length as above, that defines the action the player is making
        sklVtr is a 1D vector, length n, that defines how good a player is at different tasks. 
        
        If verbose is false, returns bool value of if check was sucsess (True) or a failure (False)
        If verbose is True, good luck Charlie
        '''
        adjPlayVtr = np.array(playVtr).dot(self.playTrans)
        adjActVtr = np.multiply(np.array(actVtr), np.array(sklVtr))
        prob = adjPlayVtr.dot(np.array(adjActVtr))
        probN = 1-(1-prob)**self.n
        roll = random()
        
        if roll<probN:
            check = True
        else:
            check = False
        
        if verbose:
            return check, probN, roll, adjActVtr
        else:
            return check
    def waitTime(self):
        return exponential(self.scale)

class continuousCheck():
    def __init__(self, meanVct, meanScaler, meanB, sigmaVct, sigmaScaler, sigmaB):
        '''
        Continuous Check gives us a building block for actions that give a continuos result (like how long a hit was), instead of just sucseed/fail
        mean of action = meanScaler * (meanVct dot player skill vector) + meanB
        '''
        self.meanVct = np.array(meanVct)
        self.meanScaler = meanScaler
        self.meanB = meanB
        self.sigmaVct = np.array(sigmaVct)
        self.sigmaScaler = sigmaScaler
        self.sigmaB = sigmaB

    def run(self, sklVct):
        mean = self.meanScaler * (self.meanVct.dot(np.array(sklVct))) + self.meanB
        sigma = self.sigmaScaler * (self.sigmaVct.dot(np.array(sklVct))) + self.sigmaB
        return np.random.normal(mean, sigma)
        

class Game:
    def __init__(self, t):
        self.t = t
        
    def run():
        self.t = 0

#Peaple Code

class Player:
    '''Player is a class that contains the player's skill vector, nerual net, TODO'''

    def __init__(self, name, sklVect, sitAware, sitAct):
        #Define behavior controling variables
        self.name = name
        self.skillVector = np.array(sklVect)
        self.sitAware = np.array(sitAware)
        self.sitAct = np.array(sitAct)

        #define empty data set
        self.stats = [] #2D array arguments: Year, Team, Launches, unitsFromLaunches, Swats, unitsFromSwats, 

    def getName(self):
        return self.name

    def getSklVct(self):
        #gives players skill vector
        return self.skillVector
    
    def think(self):
        #takes in the state of the game (tbd) and uses a baby N.N. to determine what action player will try to preform
        
        actVector = normalize(v)
        return actVector
    

class Coach:
    '''IDK What a coach will do yet'''


class Team:
    '''Team is a class that contains a coach, a list of players (5), stats, and a N.N. to control personel decisions'''
    def __init__(self, coach, players, stats=np.zeros(10)):
        self.coach = coach
        self.players = players
        self.stats = stats
    
    def setOrder(self):
        newPlayers = []

        #TODO add re-ordering code
        for i in self.players:
            newPlayers.append(i)

        self.players = newPlayers

    def getOrder(self):
        return self.players
        
    def fireCoach(self, newCoach):
        self.coach = newCoach
        
    def updateStats(self, newStats):
        self.stats.append(newStats)


#MISC entities

class Fairground:
    def __init__(self, name, goalVct):
        self.name = name
        self.goalVct = np.array(goalVct)

    def getGoalVct(self):
        return self.goalVct
    def getName(self):
        return self.name
    
def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm