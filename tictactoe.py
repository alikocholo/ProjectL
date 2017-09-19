# Uppsala univerity
# Software Engineering and Project Management autumn 2017
# Group L
# Author: Henrik Thorsell


# TODO:

#
# 5. Implement som way for the player to get help as Kiko suggested on todays meeting (19/9/2017). Perhaps always
#    check the input and if it ever is 'h', print some cleverly formatted help text.
#
# 6. Currently the way to control the game is by 1-9, this should be changed to two sets of letters, one for each
#    player. Also the input should only take one character, as you currently have to confirm your selection by
#    hitting enter. This functionality has to be removed if the players are going to be able to play smoothy.
#
# 7. Implement the time out for when the player takes to long to make a choice during their turn.
#
# 8. If a player presses the button too quickly in succession the first press is registered, the second should prompt
#    a text stating that the player is going to fast (or something similar?)
#
# 9. The print-function should be changed according to our prototype we showed Kiko, displaying the commands the
#    player can use.

def playAgain():

    while True:
        print('Do you want to play another game? (y/n)')
        option = raw_input().lower()
        if option == 'y':
            option = True
            break
        elif option == 'n':
            option = False
            break
        else:
            print('Please answer yes (y), or no (n).')
    return option

    # Asks the player if they want to play another game. Returns True or False.
    #print("Do you want to play another game? (Y/N)")
    #temp = raw_input().lower() #<- raw_input() used for python 2.x (I think), should be replaced with input() for 3.x
    #return (temp == 'y') #This should be "return (raw_input().lower() == 'y') or something similar"


def isGameStateFull(gameState):
    # Check if the game state is filled and thus no more moves are possible.
    # If an empty space is found, returns false immediately, if the state is checked and none is found return true
    for i in range(1, 10):
        if isPositionFree(gameState, i):
            return False
    return True
        
def performMove(gameState, playerMarker, move, movesLeft):
    # Markes the move in the game state using players letter
    if (playerMarker == 'X'):
        movesLeft[0].pop() #pop first element, such as removing one marker from the moves left
    else:
        movesLeft[1].pop() #remove first element, such as to remove one marker from the moves left
    gameState[move] = playerMarker

def getPlayerMove(gameState):
    # Let the player type in their move. If the move is illegal or invalid, prompt the player for a new move.

    moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        print('Select the next move using (1-9): ')
        move = raw_input()
        if (move in moves) and (isPositionFree(gameState, int(move))):
            return int(move)
        else:
            print('Illegal or invalid move. Try again!')

def isPositionFree(gameState, move):
    # Check if the move 'move' is valied within the gamestate 'gameState'
    return(gameState[move] == ' ')

def isGameWon(gS, pM):
    # Check if the gamestate (gS) contains three of the given marker (pM) in a row.
    return ((gS[1] == pM and gS[2] == pM and gS[3] == pM) or #top
            (gS[4] == pM and gS[5] == pM and gS[6] == pM) or #middle
            (gS[7] == pM and gS[8] == pM and gS[9] == pM) or #bottom
            (gS[1] == pM and gS[4] == pM and gS[7] == pM) or #down left
            (gS[2] == pM and gS[5] == pM and gS[8] == pM) or #down middle
            (gS[3] == pM and gS[6] == pM and gS[9] == pM) or #down right
            (gS[3] == pM and gS[5] == pM and gS[7] == pM) or #diagonal 1
            (gS[1] == pM and gS[5] == pM and gS[9] == pM))   #diagonal 2

def printGameState(gameState, movesLeft):
    # Prints the game state in the terminal.
    # gameState is a list representing the game state by 9 slots, one for
    # each position on the board. as illustrated here:
    # [1 2 3]
    # [4 5 6]
    # [7 8 9]

    if turn == 'playerOne':
        playerTurn = playerNames[0]
    else: playerTurn = playerNames[1]

    print('  :: Player 1: ' + str(playerNames[0]) + ' stones left: ' + str(movesLeft[0]))
    print('  :: Player 2: ' + str(playerNames[1]) + ' stones left: ' + str(movesLeft[1]))
    print('')
    print('Player ' + playerTurn + 's turn') #print players turn
    print('')
    print('   |   |')
    print(' ' + gameState[1] + ' | ' + gameState[2] + ' | ' + gameState[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameState[4] + ' | ' + gameState[5] + ' | ' + gameState[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameState[7] + ' | ' + gameState[8] + ' | ' + gameState[9])
    print('   |   |')
    return

def getPlayerNames(gameMode, playerNames):
    # if game mode is set to 0, get the names of player one and two, if the mode is set to 1
    # get the name of the only player. if there gameMode is something else (this should not
    # happen) implement some error handling.
    # The function should be called with playerNames as an empty list
    if gameMode == '0':
        print('Enter the name of player one:')
        playerNames.insert(0, raw_input())
        print('Enter the name of player two:')
        playerNames.insert(1, raw_input())
    elif gameMode == '1':
        print('Enter the name of player one:')
        playerNames.insert(0, raw_input())
    else:
        return "ERROR! YA BLEW IT!" #todo: implement some reasonable error handling here

def getGameMode():
    # Prompts the user to choose game mode. 0 is PvP and 1 is PvAI. 
    gameModes = ['0','1']
    print('Please choose player vs player or player vs AI: ')
    print('Input 0 for PvP and 1 for PvAI(not yet implemented)')
    gameMode = raw_input()
    while True:
        if (gameMode in gameModes):
            return gameMode
        else:
            print('Please select a valid game mode!')
            print('Enter 0 for PVP or 1 for PvAI(not yet implemented)')
            gameMode = raw_input()

print("Lets play!")
while True:
    # set up a clear board, player stones indicators, let playerOne start and initiate the game
    gameState = [' '] * 10 # Set up the game state represented as a list. '  ' is an empty square on the board
                           # indices represents the position of the board (index 1 = top let, index 2 = top mid etc.
    playerOneMarker = 'X'
    playerTwoMarker = 'O'
    movesLeft = [['X','X','X','X','X'],['O','O','O','O']]
    turn = 'playerOne'

    playerNames = []
    gameMode = getGameMode() # Gets game mode from the user, 0 is PvP and 1 is PvAI.

    if (gameMode == '1'): # prompt the user for new game if AI is selected, as AI not yet implemented
        print('AI not yet implemented!')
        break

    getPlayerNames(gameMode, playerNames)

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'playerOne':
            # Player ones turn. First print the gameState, then get a valid move from the player
            # finally change the gameState according to the player move, check and handle result.
            printGameState(gameState, movesLeft)
            move = getPlayerMove(gameState)
            performMove(gameState, playerOneMarker, move, movesLeft)
            printGameState(gameState, movesLeft)
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
            # Player twos turn. Do the same thing as player one.
            printGameState(gameState, movesLeft)
            move = getPlayerMove(gameState)
            performMove(gameState, playerTwoMarker, move, movesLeft)
            printGameState(gameState, movesLeft)
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
        break
