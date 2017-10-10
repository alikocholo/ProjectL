# SoftEng autumn 2017
# Uppsala university
# Author: Henrik Thorsell
# Group L

#TODO
#use getch() before choosing game mode (for user friendliness)
import random

def isPositionFree(gameState, move):
    """
    Check if the move 'move' is valied within the gamestate 'gameState'
    """
    return gameState[move] == ' '

def getEmptySquares(gameState):
    emptySquares = []
    for i in range (1,10):
        if isPositionFree(gameState, i):
            emptySquares.append(i)
    return emptySquares

def isGameWon(gS, pM):
    """
    Check if the gamestate (gS) contains three of the given marker (pM) in a row.
    """
    return ((gS[1] == pM and gS[2] == pM and gS[3] == pM) or #top
            (gS[4] == pM and gS[5] == pM and gS[6] == pM) or #middle
            (gS[7] == pM and gS[8] == pM and gS[9] == pM) or #bottom
            (gS[1] == pM and gS[4] == pM and gS[7] == pM) or #down left
            (gS[2] == pM and gS[5] == pM and gS[8] == pM) or #down middle
            (gS[3] == pM and gS[6] == pM and gS[9] == pM) or #down right
            (gS[3] == pM and gS[5] == pM and gS[7] == pM) or #diagonal 1
            (gS[1] == pM and gS[5] == pM and gS[9] == pM))   #diagonal 2

def getNextAvailableMove(gameState, playerMarker):
    for i in range(1,10):
        if isPositionFree(gameState, i):
            return i

def getMinimaxMove(gameState, playerMarker):
    # Remember, this is how the game state looks:
    # [1 2 3
    #  3 4 5
    #  7 8 9]
    # Its representation is: [unused,'X','O','X',' ',' ','X','O',' ',' ']
    # So index 1 equals square 1 in the matrix above.

    emptySquares = getEmptySquares(gameState) # Which positions should the AI choose from
    emptySquaresLength = len(emptySquares) # How many positions can the AI choose from
    results = []

    # Check if the moves have made either player one or two won
    if isGameWon(gameState, 'X') or isGameWon(gameState, 'O'):
        if playerMarker == 'X':
            return -1,-1 #(x won, no next move)
        elif playerMarker == 'O':
            return 1,-1 #(O won, no next move)
        else:
            return "Error! incorrect playerMarker"
        
    # Check if the moves have created a draw
    if emptySquaresLength == 0:
        return 0,-1 #((draw, no next move)

    # If the board is empty, grab the center square!
    elif emptySquaresLength == 9:
        return 0,5
            
    nextPlayer = 'X' if playerMarker == 'O' else 'O' # Set up the marker for the next turn

    # Loop through the list of empty squares, and for each empty square:
    # Place the available marker and recursively run the function again
    # with the newly formed game state. Restore the state after each function call.
    for i in emptySquares:
        gameState[i] = playerMarker
        ret, move = getMinimaxMove(gameState, nextPlayer)
        results.append(ret)
        gameState[i] = ' '
    
    # Either return the best move, for the player 'X', who aims to maximize the score
    if playerMarker == 'X':
        maxElement = max(results)
        return (maxElement, emptySquares[results.index(maxElement)])

    # Or return the best move, for the player 'O', who aims to minimize the scores
    elif playerMarker == 'O':
        minElement = min(results)
        return (minElement, emptySquares[results.index(minElement)])
    else:
        return "Incorrect player marker!"

def getMinimaxAIMove(gameState, playerMarker):
    a,b = getMinimaxMove(gameState,playerMarker)
    return b

def getRekd():
    # randomly returns True or False
    return bool(random.getrandbits(1))

def getAIMove(gameState, playerMarker, difficultyOption):
    if difficultyOption == 'easy':
        return getNextAvailableMove(gameState, playerMarker)
    if difficultyOption == 'medium':
        rekd = getRekd() # flip a coin to decide difficulty
        if rekd:
            return getAIMove(gameState, playerMarker, 'hard')
        else:
            return getAIMove(gameState, playerMarker, 'easy')
    if difficultyOption == 'hard':
        return getMinimaxAIMove(gameState, playerMarker)
    else:
        return None
