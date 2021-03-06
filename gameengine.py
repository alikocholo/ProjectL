# SoftEng autumn 2017
# Uppsala university
# Author: Henrik Thorsell
# Group L

import random

def isPositionFree(gameState, move):
    """
    Check if the move 'move' is valied within the gamestate 'gameState'
    """
    return gameState[move] == ' '

def getEmptySquares(gameState):
    """
    Returns the indexes of the empty squares in the represented gamestate of gameState argument.
    """
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
    """
    Returns the index of the first empty square in the represented gamestate of the gameState argument.
    """
    for i in range(1,10):
        if isPositionFree(gameState, i):
            return i

def getMinimaxMove(gameState, playerMarker):
    """
    Call with the board game as gameState and playerMarker as either O or X, representing the
    player about to make a turn.
    Returns the best move to make according to the implemented version of the minimax algorithm.
    Also returns the value of the move according to the implemented algorithm.
    """
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
    """
    A wrapper function that only removes the best move according to the called function,
    instead of returning both the move and the value of the move.
    """
    a,b = getMinimaxMove(gameState,playerMarker)
    return b

def getRekd():
    """
    Randomly returns True or False
    """
    # randomly returns True or False
    return bool(random.getrandbits(1))

def getAIMove(gameState, playerMarker, difficultyOption):
    """
    Calls the appropriate AI-move-calculating-function depending on difficultyOption
    with the playerMarker as the player making the move in the game gameState.
    Returns the index of the square for the playerMaker to play.
    """
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

def playAIvsAI(playerOne, playerTwo):
    """
    Checks the AI-players difficulties and returns the winner. Hard always beats medium and easy,
    medium always beats easy and when two AIs of equal difficulty meet the winner is random.
    This function eliminates the need of pitting the AI against each other, wasting the players
    time and resources. May or may not be used according to the specifications.
    """
    if playerOne[1] ==  playerTwo[1]:
        return random.choice([playerOne, playerTwo])
    elif playerOne[1] == 'hard':
        return playerOne
    elif playerTwo[1] == 'hard':
        return playerTwo
    elif playerOne[1] == 'medium':
        return playerOne
    elif playerTwo[1] == 'medium':
        return playerTwo
    else:
        print("Undefined behavoir in playAivsAI")
        return "Undefined behaviour in playAIvsAI"
