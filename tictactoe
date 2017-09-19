# Uppsala univerity
# Software Engineering and Project Management autumn 2017
# Group L
# Author: Henrik Thorsell


# TODO:
# 1. When a player tries to place a marker on an existing position the game should force the player to
#    chose a new position. Currently it just removes the old one and replaces it with the new marker.
#
# 2. The game should display the ammount of markers left for each player. This should be done by updating
#    the print-function.
#
# 3. The game should propmt the player to choose between vs AI or another player. Currently the default is vs another
#    player. This should probably be done at the start by asking the player for input and then branch the execution.
#    No AI is to be implemented so perhaps just some tbi-stuff there.
#
# 4. The game should ask the player or players for their names and display then together with the game state. This
#    should be by asking the player at the start, store the names in a list and refactor the print-function to take
#    the list as an additional argument, use it to print.
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
    # Asks the player if they want to play another game. Returns True or False.
    print("Do you want to play another game? (Y/N)")
    temp = raw_input().lower() #<- raw_input() used for python 2.x (I think), should be replaced with input() for 3.x
    return (temp == 'y') #This should be "return (raw_input().lower() == 'y') or something similar"

def isGameStateFull(gameState):
    # Check if the game state is filled and thus no more moves are possible.
    # If an empty space is found, returns false immediately, if the state is checked and none is found return true
    for i in range(1, 10):
        if isPositionFree(gameState, i):
            return False
    return True
        
def performMove(gameState, playerMarker, move):
    # Markes the move in the game state using players letter
    gameState[move] = playerMarker

def getPlayerMove(gameState):
    # Let the player type in their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isPositionFree(gameState, int(move)):
        print('Select the next move using (1-9): ')
        move = input()
        print("Returning move: " + str(move))
        return(move)

def isPositionFree(gameState, move):
    # Check if the move 'move' is valied within the gamestate 'gameState'
    return gameState[move] == ' '

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

def printGameState(gameState):
    # Prints the game state in the terminal.
    # gameState is a list representing the game state by 9 slots, one for
    # each position on the board. as illustrated here:
    # [1 2 3]
    # [4 5 6]
    # [7 8 9]
    print('   |   |')
    print(' ' + gameState[7] + ' | ' + gameState[8] + ' | ' + gameState[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameState[4] + ' | ' + gameState[5] + ' | ' + gameState[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameState[1] + ' | ' + gameState[2] + ' | ' + gameState[3])
    print('   |   |')
    return

print("Lets play!")
while True:
    # set up a clear board, player stones indicators, let playerOne start and initiate the game
    gameState = [' '] * 10
    playerOneMarker = 'X'
    playerTwoMarker = 'O'
    turn = 'playerOne'
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'playerOne':
            # Player ones turn. First print the gameState, then get a valid move from the player
            # finally change the gameState according to the player move, check and handle result.
            printGameState(gameState)
            move = getPlayerMove(gameState)
            performMove(gameState, playerOneMarker, move)
            printGameState(gameState)
            if isGameWon(gameState, playerOneMarker):
                print("Player one won!")
                gameIsPlaying == False
                break
            else:
                if isGameStateFull(gameState):
                    print("Its a draw!")
                    break
                else:
                    turn = 'playerTwo'
        else:
            # Player twos turn. Do the same thing as player one.
            move = getPlayerMove(gameState)
            performMove(gameState, playerTwoMarker, move)
            
            if isGameWon(gameState, playerTwoMarker):
                printGameState(gameState)
                print("Player two won!")
                gameIsPlaying == False
                break
            else:
                if isGameStateFull(gameState):
                    printGameState(gameState)
                    print("Its a draw!")
                    break
                else:
                    turn = 'playerOne'
                    
    if not playAgain():
        break
