def BoolStep(player, check, trueState, falseState, startTime, playVct = False):
    '''
    This function defines a boolean step in a game, where a player object player performs an action against QuantCheck object check.
    If this check passes, or returns true, this returns the next game state enum trueState
    '' but if failed, falseState
    Check is a QuantCheck object'''

    actVct = player.think() #TODO WITH ALEX
    #update play vector
    if playVct == False:
        playVct = actVct
    #Run the check
    result = check.run(playVct, actVct, player.getSklVct())
    #get the time for play
    waitTime = check.waitTime()
    endTime = startTime + waitTime
    #define outputs
        #Game state simmed (hard coded), result of sim, game Vector
    #branch depending on result
    if result:
            nextState = trueState
    else:
            nextState = falseState
    #return results
    return nextState, endTime