class Planet:
    '''planet is a class'''

    def __init__(self, name, dayLength, mass, averageDistance, angleAtZero, seasonList):
        self.name = name
        self.dayT = dayLength
        self.mass = mass
        self.r = averageDistance
        self.yearT = 0 #TODO with keppler
        self.angle0 = angleAtZero
    
    def getPosition(self, t):
        return 0