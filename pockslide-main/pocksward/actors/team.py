#import modules for all sub-.py files
import numpy as np

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
