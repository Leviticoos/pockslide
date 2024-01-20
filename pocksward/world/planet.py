class Planet:
    '''planet is a class'''

    def __init__(self, name, dayLength, mass, averageDistance, angleAtZero, seasonList):
        self.name = name
        self.dayT = dayLength
        self.mass = mass
        self.r = averageDistance
        self.yearT = TODO CALC WITH KEPLER
        self.angle0 = angleAtZero
    
    def getPosition(self, t):
        