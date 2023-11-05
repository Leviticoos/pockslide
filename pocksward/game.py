#import big libraries
import numpy as np
from enum import Enum

#import Levi libraries
import pocksward as pk

#Keep this as long as lenses.py is being edited TODO delete once done
from importlib import reload  # Python 3.4+
pk = reload(pk)

#Define main play, and the checks and State enum Class needed
class GameStep():
    ##GameStateEnum.clink, result, [self.gameState, self.iterator, self.pylon, self.homeUp, self.scores, self.place, self.clock, [player, player.getSklVct(), actVct]]
    def __init__(self, gameState)

class GameStateEnum(Enum):
        preGame     = 1
        slide       = 2
        clink       = 3
        hitch       = 16
        scrambleAdmin   = 4
        breather    = 6
        switch      = 7
        braek       = 8
        gas         = 9
        hammer      = 10
        dink        = 11
        nail        = 12
        scrumAdmin      = 13
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
        self.iterator = 0
        self.place = 0
        self.pylon = 1
        self.homeUp = False #will flip on first scrambleAdmin run
        self.teamUp = self.homeTeam
        self.teamDown = self.awayTeam
        self.scores = [0,0] #first is home team, second is away
        self.playVct = [0,0,0,0]

        #define Checks
        #scramble Chekcks
        self.slideChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 3, 1, n=3)
        self.clinkChk   = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 3, 1, n=3)
        self.hitch      = pk.continuousCheck([1,0,0,0], 10, 80, [0,1,0,0], 20, 0)
        #Scrum Checks
        self.switchChk  = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 1, n=3)
        self.braekChk   = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]], 2, 1)
        self.gasChk     = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 1)
        self.hammerChk  = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 1, n=3) 
        self.dinkChk    = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]], 2, 1)
        self.nailChk    = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 1) 

        #Todo, game wide special events? Weather? Setup players random change?
        #or do I put that in pregame?
    
    def run(self):
        if self.gameState.name == "preGame":
            waitTime = 6 #five minutes to talk
            #todo: set up random things
            
            #save output
            out = GameStateEnum.preGame, waitTime
            #advance stats
            self.gameState = GameStateEnum.scrambleAdmin
            #return output
            return out
            
        elif self.gameState.name == "slide":
            #Get slider for the pylon
            player = self.teamUp.getOrder()[self.iterator - 1]
            #feed the acting player the game state, get his actVct
            actVct = player.think() #TODO WITH ALEX
            #update play vector
            self.playVct = actVct
            #Run the check
            result = self.slideChk.run([1,1,1,1], actVct, player.getSklVct())
            #get the time for play
            waitTime = self.slideChk.waitTime()
            self.clock += waitTime
            #define outputs
                #Game state simmed (hard coded), result of sim, game Vector
            out = GameStateEnum.slide, result, [self.gameState, self.iterator, self.pylon, self.homeUp, self.scores, self.place, self.clock, [player, player.getSklVct(), actVct]]
            #branch depending on result
            if result:
                 self.gameState = GameStateEnum.clink
            else:
                 self.gameState = GameStateEnum.scrambleAdmin
            #return results
            return out
            
        elif self.gameState.name == "clink":
            #clink
            #Get clinker for the pylon
            player = self.teamUp.getOrder()[self.pylon % 5]
            #feed the acting player the game state, get his actVct
            actVct = player.think() #TODO WITH ALEX
            #Run the check (hit or miss)
            result = self.slideChk.run(self.playVct, actVct, player.getSklVct())
            #get the time for play
            waitTime = self.slideChk.waitTime()
            self.clock += waitTime
            #branch depending on result
            
            #set Results
            out = GameStateEnum.clink, result, [self.gameState, self.iterator, self.pylon, self.homeUp, self.scores, self.place, self.clock, [player, player.getSklVct(), actVct]] #TODO may need to return gameState.value. will see!
            #update state stats
            stateSimmed = self.gameState
            if result:
                 self.gameState = GameStateEnum.hitch
            else:
                 self.gameState = GameStateEnum.scrambleAdmin
                 
            return out
        
        elif self.gameState.name =="hitch":
            #see how long it flys baby!
            player = self.teamUp.getOrder()[self.pylon % 5]
            result = self.hitch.run(player.getSklVct())
            if self.homeUp:
                self.place += result
            else:
                self.place -= result
            #TODO Flesh out wait time
            waitTime = 3
            #set up output
            out = GameStateEnum.hitch, result, [self.gameState, self.iterator, self.pylon, self.homeUp, self.scores, self.place, self.clock, [0,0,0]]
            #advance gameState
            self.gameState = GameStateEnum.scrambleAdmin
            return out
        
        elif self.gameState.name == "scrambleAdmin":
            #admin game state updates scramble, and starts next "play"
            if abs(self.place) > self.fg.getHalfLength():
                self.gameState = GameStateEnum.breather
            elif self.homeUp:
                self.homeUp = False
                self.teamUp = self.awayTeam
                self.gameState = GameStateEnum.slide
            else:
                self.homeUp = True
                self.teamUp = self.homeTeam
                if self.iterator < 5:
                    self.iterator += 1
                    self.gameState = GameStateEnum.slide
                else:
                    self.iterator = 1
                    self.gameState = GameStateEnum.breather
            
            return GameStateEnum.scrambleAdmin, 0, 0
                    
        elif self.gameState.name == "breather":
            #breather
            #reset values
            self.iterator = 0
            #check side the large pock has landed, determining sides for the next inning
            if self.place >= 0:
                self.teamUp = self.homeTeam
                self.teamDown = self.awayTeam
                self.homeUp = True
            else:
                self.teamUp = self.awayTeam
                self.teamDown = self.homeTeam
                self.homeUp = False
            #see if they went sward
            if abs(self.place) > self.fg.getHalfLength():
                if self.homeUp:
                    self.scores[0] += 20
                else:
                    self.scores[1] += 20
                out = GameStateEnum.breather
                self.gameState = GameStateEnum.recess
                return out
            #TODO make some random thing happen for announcers?
            #THis could be its own thing huh, talk at meeting about it.
            
            out = self.gameState, 0, 0
            self.gameState = GameStateEnum.switch
            self.place = 0
            return out
        
        elif self.gameState == GameStateEnum.switch:
            return "SWITCH CATCH"
        
        

        

