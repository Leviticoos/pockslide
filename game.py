import numpy as np

import pocksward as pk

#Keep this as long as lenses.py is being edited TODO delete once done
from importlib import reload  # Python 3.4+
pk = reload(pk)

#Define chekcks and main play

offOne = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],n=10)
defOne = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
offTwo = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
offThree = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
defTwo = pk.Check([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
goal = pk.Check([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) 

def playMain(playerA, playerB, playerC, gameState, fairgroundGoalVct)
    #First throw
    actVct = playerA.think(gameState)
    firstOffense = offOne.run([1,1,1,1], actVct, playerA.getSklVct())
    outData = [playerA, ]
    
    if firstOffense == False:
        outData.a
    else:
 
        firstDefense = defOne.run(actVct, playerB.think(gameState), playerB.getSklVct())
