def boolStep(playVct, actVct, sklVct, check, trueState, falseState, startTime):
    '''
    This function defines a boolean step in a game, where a player object player performs an action against QuantCheck object check.
    If this check passes, or returns true, this returns the next game state enum trueState
    '' but if failed, falseState
    Check is a QuantCheck object'''

    #Run the check
    result = check.run(playVct, actVct, sklVct, startTime)
    #get the time for play
    waitTime = check.waitTime(startTime)
    endTime = startTime + waitTime
    #define outputs
        #Game state simmed (hard coded), result of sim, game Vector
    #branch depending on result
    if result:
            nextState = trueState
    else:
            nextState = falseState
    #return results
    return result, nextState, actVct, endTime