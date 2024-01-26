import numpy as np


class Fairground:
    def __init__(self, name, goalVct, halfLength):
        self.name = name
        self.goalVct = np.array(goalVct)
        self.halfLength = halfLength

    def getGoalVct(self):
        return self.goalVct
    def getName(self):
        return self.name
    def getHalfLength(self):
        return self.halfLength
