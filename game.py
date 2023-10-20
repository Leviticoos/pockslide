#import big libraries
import numpy as np
from enum import Enum

#import Levi libraries
import pocksward as pk

#Keep this as long as lenses.py is being edited TODO delete once done
from importlib import reload  # Python 3.4+
pk = reload(pk)

#Define main play, and the checks and State enum Class needed

class GameStateEnum(Enum):
        preGame     = 1
        slide       = 2
        clink       = 3
        postClink   = 4
        changeSides = 5
        breather    = 6
        switch      = 7
        braek       = 8
        gas         = 9
        hammer      = 10
        dink        = 11
        nail        = 12
        recess      = 13
        final       = 14

class Game:
    
    #define Checks
    switchChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], n=10)
    braekChk    = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
    gasChk      = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    hammerChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], n=3) 
    dinkChk     = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
    nailChk     = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) 
             
    def __init__(self, homeTeam, awayTeam, fairground, startTimeSST):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.fg = fairground
        self.start = startTimeSST
        self.clock = startTimeSST
        self.gameState = GameStateEnum.preGame
        self.iterator = 1
        self.inning = 1
        self.teamUp = self.homeTeam
        self.teamDown = self.awayTeam
        self.scores = [0,0] #first is home team, second is away
        self.gameVector = [self.gameState, self.iterator, self.inning, , self.scores] #not sure if this is needed?
        #Todo, game wide special events? Weather? Setup players random change?
        #or do I put that in pregame?
    
    def run(self):
        if self.gameState.value == 1:
            #pregame code
            
            
        elif self.gameState.value == 2:
            #slide
            u
        elif self.gameState.value == 6:
            #breather
        elif self.gameState.value == 7:
            #switch
            #Get switcher for the inning
            playerA = self.teamUp.getorder()[self.inning]
            #feed the switcher the game state, get his actVct
            actVct = playerA.think(gameState)
            
            
            
    #First throw
    actVct = playerA.think(gameState)
    firstOffense = offOne.run([1,1,1,1], actVct, playerA.getSklVct())
    outData = [playerA, ]
    
    if firstOffense == False:
        outData.a
    else:
 
        firstDefense = defOne.run(actVct, playerB.think(gameState), playerB.getSklVct())
