import numpy as np
import random as random
    
class boolCheck:
    def __init__(self, skillTransform,timeMean, timeB, n=1, helpText=''):
        '''
        Define a check, which is a base unit of a play. Takes in a skill transform, which will map an action vector to different skills, and possibly 
        n is an intager that represents how many chances you have to succseed. This is a way of letting low chances be more likely. 
        helpText, which can be your notes on what this check is.
        
        Conceptually, a check is a single pass/fail unit of the sport. The player will set their action vector, and 
        '''
        self.playTrans = np.array(skillTransform)
        self.n = int(n)
        self.help = helpText
        self.timeMean = timeMean
        self.timeB = timeB

    def help(self):
        return self.help
    
    def run(self, playVtr, actVtr, sklVtr, time, verbose=False):
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
        random.seed(time)
        roll = random.random()
        
        if roll<probN:
            check = True
        else:
            check = False
        
        if verbose:
            return check, probN, roll, adjActVtr
        else:
            return check
    def waitTime(self, time):
        random.seed(time)
        return random.expovariate(1/self.timeMean)+self.timeB

