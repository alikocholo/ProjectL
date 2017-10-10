import getch
# Uppsala univerity
# Software Engineering and Project Management autumn 2017
# Group L
# Author: Casper Strömberg, Henrik Thorsell

# TODO:
# 4. Kiko mentioned on todays meeting (19/9/2017) that displaying some help-text when pushin 'h' could be implemented. Now the text
#    is always displayed. The solution isn't as pretty, but maybe it'll work. Should be discussed at least?

from gameengine import getAIMove, isGameWon, isPositionFree, playAIvsAI
import random
import curses

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
    if move is not None:
        gameState[move] = playerMarker
    else:
        return "ERROR! Move was None in performMove function call in tactoe.py"
    
def printMoves(moves): 
    for i in range(0, 3):
        print(moves[i*3:i*3+3])

def getAIDifficulty():
    """
    Let the player select the AI
    difficulty. If the input is invalid
    prompt the player for a new option.
    """

    optionsShort = ['e','m','h']
    options = ['easy', 'medium', 'hard']

    while True:
          print('Select AI difficulty: ')
          print('Easy provides no adviersity, hard is undefeatable.')
          print('Medium randomly choses between easy and hard.')
          print('e - easy, m - medium, h - hard.')  
          selection = getch.getch()
          if (selection in optionsShort):
              # Return the corresponding element in options using optionsShort
              # (so entering 'e' returns 'easy', etc.)
              return options[optionsShort.index(selection)]
          else:
              print ('Invalid selection, please try again!')
        
def getPlayerMove(gameState, turn):
    """
    Let the player type in their move.
    If the move is illegal or invalid, 
    prompt the player for a new move.
    """
    esc = '\x1b'
    if turn == 'playerOne':
        moves = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
    else:
        moves = ['y', 'u', 'i', 'h', 'j', 'k', 'b', 'n', 'm']
    while True:
        print('Select the next move using')
        printMoves(moves)
        print('or press ESC to quit.')
        try:
            move = getch.getch()
            move = move.lower()
            if move == esc:
                return None
            elif (move in moves) and (isPositionFree(gameState, int(moves.index(move) + 1))):
                return int(moves.index(move) + 1)
            else:
                print('Illegal or invalid move. Try again!')
        except:
            print('Illegal or invalid move. Try again!')

def printGameState(gameState, movesLeft, turn, playerNames, round):
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
    if round != 0:
        print('  :: Round {}: {} vs {}'.format(round, playerNames[0], playerNames[1]))
    print('  :: Player 1: ' + str(playerNames[0]))
    print('  :: Stones left: ' + str(movesLeft[0]))
    print('                                                             :: Player 2: ' + str(playerNames[1]))
    print('                                                             :: Stones left: ' + str(movesLeft[1]))
    print('')
    print('                                         Player ' + playerTurn + '\'s turn') #print players turn
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
        print('Enter your name:')
        playerNames.insert(0, input())
        playerNames.insert(1, "The Robot Overlord (AI)")
    else:
        return "ERROR! YA BLEW IT!" #todo: implement some reasonable error handling here
    if playerNames[0] == '':
        playerNames[0] = 'One'
    if playerNames[1] == '':
        playerNames[1] = 'Two'
    return playerNames

def getGameMode():
    """
    Prompts the user to choose game mode. 0 is PvP, 1 is PvAI, 2 is AIvsAI. 
    """
    gameModes = ['0','1','2']
    print('Please choose player vs player, player vs AI or AI vs AI: ')
    print('Input 0 for PvP, 1 for PvAI and 2 for AIvsAI')
    gameMode = input()
    while True:
        if (gameMode in gameModes):
            return gameMode
        else:
            print('Please select a valid game mode!')
            print('Enter 0 for PVP, 1 for PvAI and 2 for AIvsAI')
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
    if gameMode == '3':
        print("Please select first and second ai difficulties")
        firstAIdifficulty = getAIDifficulty()
        secondAIdifficulty = getAIDifficulty()
        return playAIvsAI(['AI one', firstAIdifficulty], ['AI two', secondAIdifficulty])
    if gameMode == '1': #If mode is AI, it is randomly chosen who starts
        firstMove = ['playerOne', 'playerTwo']
        turn = random.choice(firstMove)
        if turn == 'playerTwo':
            movesLeft = [['X','X','X','X'],['O','O','O','O','0']]
        print("Getting AI difficulty")
        difficultyOption = getAIDifficulty()
        print("Ai difficulty was: " + difficultyOption)


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
            if move == None:
                break
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
                    # Player twos turn. Do the same thing as player one. If Game mode is set to PvsAI (1),
                    #instead call the function for AI to make a move.
            printGameState(gameState, movesLeft, turn, playerNames)
            if (gameMode == '1'):
                move = getAIMove(gameState, playerTwoMarker, difficultyOption) # Change this function call to whatever
                                                                               #game-engine we decide to integrate with.
            else:
                move = getPlayerMove(gameState, turn)
            performMove(gameState, playerTwoMarker, move, movesLeft)
            printGameState(gameState, movesLeft, turn, playerNames)
            if isGameWon(gameState, playerTwoMarker):
                if gameMode == '1':
                    print("The Robot Overlord (AI) won!")
                else:
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

def loopExternal(playerOne, playerTwo, gameMode, round=0):

    # set up a clear board, player stones indicators, let playerOne start and initiate
    #the game
    gameState = [' '] * 10 # Set up the game state represented as a list. '  ' is an empty square on the board
    # indices represents the position of the board (index 1 = top let, index 2 = top mid etc.
    playerNames = [playerOne[0], playerTwo[0]]
    playerOneMarker = 'X'
    playerTwoMarker = 'O'
    movesLeft = [['X','X','X','X','X'],['O','O','O','O']]
    turn = 'playerOne'
    if gameMode == '1':
        difficultyOption = 'easy'

    gameIsPlaying = True
    result = None
    while gameIsPlaying:
        if turn == 'playerOne':
            # Player ones turn. First print the gameState, then get a valid move from the player
            # finally change the gameState according to the player move, check and handle result
            printGameState(gameState, movesLeft, turn, playerNames, round)
            if playerOne[1] == 'human': # If the player is human, get their move.
                move = getPlayerMove(gameState, turn)
            else: # if the player is ai, call the Ai function with playerOne[1] = difficulty
                move = getAIMove(gameState, playerOneMarker, playerOne[1])
            if move == None:
                break
            
            performMove(gameState, playerOneMarker, move, movesLeft)
            printGameState(gameState, movesLeft, turn, playerNames, round)
            if isGameWon(gameState, playerOneMarker):
                print('Player one (' + str(playerNames[0]) + ') won!')
                result = 'playerOne'
                gameIsPlaying = False
            else:
                if isGameStateFull(gameState):
                    print("Its a draw!")
                    result = 'draw'
                    break
                else:
                    turn = 'playerTwo'
        else:
                    # Player twos turn. Do the same thing as player one. If Game mode is set to PvsAI (1),
                    #instead call the function for AI to make a move.
            printGameState(gameState, movesLeft, turn, playerNames, round)
            if (playerTwo[1] == 'human'):
                move = getPlayerMove(gameState, turn)
            else:
                move = getAIMove(gameState, playerTwoMarker, playerTwo[1])
            performMove(gameState, playerTwoMarker, move, movesLeft)
            printGameState(gameState, movesLeft, turn, playerNames, round)
            if isGameWon(gameState, playerTwoMarker):
                print("Player two won!")
                result = 'playerTwo'
                gameIsPlaying = False
            else:
                if isGameStateFull(gameState):
                    print("Its a draw!")
                    result = 'draw'
                    break
                else:
                    turn = 'playerOne'
    return result
