
#import Levi libraries
import pocksward as pk

#Keep this as long as lenses.py is being edited TODO delete once done
from importlib import reload  # Python 3.4+
pk = reload(pk)

class Coach:
    '''IDK What a coach will do yet'''
    def __init__(name, birthDay):
        self.name = name
        self.dob = birthDay
        self.rosterNN = ""
        self.emoteNN = ""

    def giveBrains(self, models, weights, random, overRide=False):
        #first, make sure there is no exsisting brain we are overriding TODO add possible overide
        if self.rosterNN != "" and self.emoteNN != "":
            #if models is an empyt do-dad, create a random NN
            if models == []:
                self.rosterNN = pk.NN(8,24,2)
                self.emoteNN = pk.NN(8,24,2)
                return True
            #take the different models and genetic them together.
            else:
                return False
                
            
