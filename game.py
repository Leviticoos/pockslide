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
        postNail    = 13
        recess      = 14
        final       = 15

class Game:
             
    def __init__(self, homeTeam, awayTeam, fairground, startTimeSST):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.fg = fairground
        self.start = startTimeSST
        self.clock = startTimeSST
        self.gameState = GameStateEnum.preGame
        self.iterator = 1
        self.pylon = 1
        self.homeUp = True
        self.teamUp = self.homeTeam
        self.teamDown = self.awayTeam
        self.scores = [0,0] #first is home team, second is away

        #define Checks
        self.switchChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 1, n=10)
        self.braekChk    = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]], 1)
        self.gasChk      = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 1)
        self.hammerChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 1, n=3) 
        self.dinkChk     = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]], 1)
        self.nailChk     = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 1) 

        #Todo, game wide special events? Weather? Setup players random change?
        #or do I put that in pregame?
    
    def run(self):
        if self.gameState.value == 1:
            #pregame code
            waitTimeSuggestion = 1000*120
            #todo: set up 
            text = 'Warmimng up!'
            
            return [], text, waitTimeSuggestion
            
        elif self.gameState.value == 2:
            #slide
            u
        elif self.gameState.value == 6:
            #breather
            u
        elif self.gameState.value == 7:
            #switch
            #Get switcher for the pylon
            player = self.teamUp.getorder()[self.pylon]
            #feed the switcher the game state, get his actVct
            actVct = player.think() #TODO WITH ALEX
            #Run the check
            result = self.switchChk.run([1,1,1,1], actVct, player.getSklVct())
            #get the time for play
            waitTime = self.switchChk.time()
            self.clock += waitTime
            #branch depending on result
            stateSimmed = self.gameState
            if result:
                 self.gameState.value = 8
            else:
                 self.gameState.value = 13
            #return results
            return result, [stateSimmed, self.iterator, self.pylon, self.homeUp, self.scores, self.clock], waitTime #TODO may need to return gameState.value. will see!
        


        

