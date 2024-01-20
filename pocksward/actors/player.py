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
        v1 = random.random()
        v2 = random.random()
        v3 = random.random()
        v4 = random.random()
        actVector = normalize([v1, v2, v3, v4])
        return actVector
    
    def changeSklVct(self, sklMod):
        self.skillVector = normalize(np.add(self.skillVector, np.array(sklMod)))
  