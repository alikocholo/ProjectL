import getch
# Uppsala univerity
# Software Engineering and Project Management autumn 2017
# Group L
# Author: Casper Strömberg, Henrik Thorsell

# TODO:
#
# 1. Currently the way to control the game is by 1-9, this should be changed to two sets of letters, one for each
#    player. Also the input should only take one character, as you currently have to confirm your selection by
#    hitting enter. This functionality has to be removed if the players are going to be able to play smoothy.
#  - Letters implemented but enter is still required. (we need https://pypi.python.org/pypi/getch) to be able to get that functionallity.
#
# 4. Kiko mentioned on todays meeting (19/9/2017) that displaying some help-text when pushin 'h' could be implemented. Now the text
#    is always displayed. The solution isn't as pretty, but maybe it'll work. Should be discussed at least?

from gameengine import getAIMove

def playAgain():
    """
    prompts the player if they want to play again. 
    returning true of false. 
    if something other than y or n is provided as input
    the function keeps calling input() asking for new input until it matches either case.
    """
    while True:
        print('Do you want to play another game? (y/n)')
        option = input().lower()
        if option == 'y':
            return True
        elif option == 'n':
            return False
        else:
            print('Please answer yes (y), or no (n).')

def isGameStateFull(gameState):
    """
    Check if the game state is filled and thus no more moves are possible.
    If an empty space is found, returns false immediately, if the state is checked and none is found return true
    """
    for i in range(1, 10):
        if isPositionFree(gameState, i):
            return False
    return True
        
def performMove(gameState, playerMarker, move, movesLeft):
    """
    Markes the move in the game state using players letter
    """
    if (playerMarker == 'X'):
        movesLeft[0].pop() #pop first element, such as removing one marker from the moves left
    else:
        movesLeft[1].pop() #remove first element, such as to remove one marker from the moves left
    gameState[move] = playerMarker
    
def printMoves(moves): 
    for i in range(0, 3):
        print(moves[i*3:i*3+3])

def getPlayerMove(gameState, turn):
    """
    Let the player type in their move.
    If the move is illegal or invalid, 
    prompt the player for a new move.
    """

    if turn == 'playerOne':
        moves = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
    else:
        moves = ['y', 'u', 'i', 'h', 'j', 'k', 'b', 'n', 'm']
    while True:
        print('Select the next move using')
        printMoves(moves)
        move = getch.getch()
        if (move in moves) and (isPositionFree(gameState, int(moves.index(move) + 1))):
            return int(moves.index(move) + 1)
        else:
            print('Illegal or invalid move. Try again!')

def isPositionFree(gameState, move):
    """
    Check if the move 'move' is valied within the gamestate 'gameState'
    """
    return gameState[move] == ' '

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

def printGameState(gameState, movesLeft, turn, playerNames):
    """
    Prints the game state in the terminal.
    gameState is a list representing the game state by 9 slots, one for
    each position on the board. as illustrated here:
    [1 2 3]
    [4 5 6]
    [7 8 9]
    """
    padding = "                                          " # set amount of space to pad the printed output
    if turn == 'playerOne':
        playerTurn = playerNames[0]
    else: playerTurn = playerNames[1]

    print('  :: Player 1: ' + str(playerNames[0]))
    print('  :: Stones left: ' + str(movesLeft[0]))
    print('                                                             :: Player 2: ' + str(playerNames[1]))
    print('                                                             :: Stones left: ' + str(movesLeft[1]))
    print('')
    print('                                         Player ' + playerTurn + 's turn') #print players turn
    print('')
    print(padding+'     |   |')
    print(padding+'   ' + gameState[1] + ' | ' + gameState[2] + ' | ' + gameState[3])
    print(padding+'     |   |')
    print(padding+'---------------')
    print(padding+'     |   |')
    print(padding+'   ' + gameState[4] + ' | ' + gameState[5] + ' | ' + gameState[6])
    print(padding+'     |   |')
    print(padding+'---------------')
    print(padding+'     |   |')
    print(padding+'   ' + gameState[7] + ' | ' + gameState[8] + ' | ' + gameState[9])
    print(padding+'     |   |')
    return

def getPlayerNames(gameMode):
    """
    if game mode is set to 0, get the names of player one and two, if the mode is set to 1
    get the name of the only player. if there gameMode is something else (this should not
    happen) implement some error handling.
    The function should be called with playerNames as an empty list
    """
    playerNames = []
    if gameMode == '0':
        print('Enter the name of player one:')
        playerNames.insert(0, input())
        print('Enter the name of player two:')
        playerNames.insert(1, input())
    elif gameMode == '1':
        print('Enter the name of player one:')
        playerNames.insert(0, input())
        playerNames.insert(1, "The Robot Overlord (AI)")
    else:
        return "ERROR! YA BLEW IT!" #todo: implement some reasonable error handling here
    return playerNames

def getGameMode():
    """
    Prompts the user to choose game mode. 0 is PvP and 1 is PvAI. 
    """
    gameModes = ['0','1']
    print('Please choose player vs player or player vs AI: ')
    print('Input 0 for PvP and 1 for PvAI(not yet implemented)')
    gameMode = input()
    while True:
        if (gameMode in gameModes):
            return gameMode
        else:
            print('Please select a valid game mode!')
            print('Enter 0 for PVP or 1 for PvAI(not yet implemented)')
            gameMode = input()

def loop():
    # set up a clear board, player stones indicators, let playerOne start and initiate the game
    gameState = [' '] * 10 # Set up the game state represented as a list. '  ' is an empty square on the board
    # indices represents the position of the board (index 1 = top let, index 2 = top mid etc.
    playerOneMarker = 'X'
    playerTwoMarker = 'O'
    movesLeft = [['X','X','X','X','X'],['O','O','O','O']]
    turn = 'playerOne'
    gameMode = getGameMode() # Gets game mode from the user, 0 is PvP and 1 is PvAI.

    #if (gameMode == '1'): # prompt the user for new game if AI is selected, as AI not yet implemented
    #    print('AI not yet implemented!')
    #    return

    playerNames = getPlayerNames(gameMode)

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'playerOne':
            # Player ones turn. First print the gameState, then get a valid move from the player
            # finally change the gameState according to the player move, check and handle result.
            printGameState(gameState, movesLeft, turn, playerNames)
            move = getPlayerMove(gameState, turn)
            performMove(gameState, playerOneMarker, move, movesLeft)
            printGameState(gameState, movesLeft, turn, playerNames)
            if isGameWon(gameState, playerOneMarker):
                print('Player one (' + str(playerNames[0]) + ') won!')
                gameIsPlaying = False
            else:
                if isGameStateFull(gameState):
                    print("Its a draw!")
                    break
                else:
                    turn = 'playerTwo'
        else:
                    # Player twos turn. Do the same thing as player one. If Game mode is set to PvsAI (1), instead call the function for AI to make a move.
            printGameState(gameState, movesLeft, turn, playerNames)
            if (gameMode == '1'):
                move = getAIMove(gameState, playerTwoMarker) # Change this function call to whatever game-engine we decide to integrate with.
            else:
                move = getPlayerMove(gameState, turn)
            performMove(gameState, playerTwoMarker, move, movesLeft)
            printGameState(gameState, movesLeft, turn, playerNames)
            if isGameWon(gameState, playerTwoMarker):
                print("Player two won!")
                gameIsPlaying = False
            else:
                if isGameStateFull(gameState):
                    print("Its a draw!")
                    break
                else:
                    turn = 'playerOne'
                        
    if not playAgain():
        return
        
    loop()
