# SoftEng autumn 2017
# Uppsala university
# Author: Henrik Thorsell
# Group L

def getAIMove(gameState, playerMarker):
    return makeRandomMove(gameState)

def makeRandomMove(gameState):
    for i in range(1,10):
        if isPositionFree2(gameState, i):
            return i

def isPositionFree2(gameState, move):
    """
    Check if the move 'move' is valied within the gamestate 'gameState'
    """
    return gameState[move] == ' '
