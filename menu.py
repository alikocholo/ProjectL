# SoftEng autumn 2017
# Uppsala universty
# Author: Henrik Thorsell
# Group L

from tactoe import loopExternal
import random
from random import shuffle

def startGameFunction(playerOneName, playerTwoName, gameMode, round=0):
    """
    Set the called function to whichever function your game platform uses
    """
    return loopExternal(playerOneName, playerTwoName, gameMode, round)


def startGame(playerOneName, playerTwoName):
    """
    Runs a game of tic tac toe with the arguments as player names. They must be strings.
    Returns the game result which is either the name of the winning player or 'draw'.
    If the game was a draw, replay the game until a winner is returned. After three games
    a winner is randomly chosen by 'cointoss'.
    """
    
    # Run the first game
    gameResult = startGameFunction(playerOneName, playerTwoName)
    gameCounter = 1

    # If there was a draw run two more games, end as soon as a winner is found
    while(gameCounter < 4 & gameResult == 'draw'):
        gameResult = starGameFunction(playerOneName, playerTwoName, gameMode)
        gameCounter += 1

    # If there is no winner after three games, randomly pick one
    if (gameCounter == 3 & gameResult == 'draw'):
        randomCoin = bool(random.getrandbits(1))
        if randmomCoin:
            gameResult = playerOneName
        else:
            gameResult = playerTwoName
    
    # Return the name of the winning player
    return gameResult
        
def printMenu():
    """
    Prints the main menu to the terminal
    """
    print('Welcome to the Group L Tic tac toe game!')
    print('Please select from the following options:')
    print('[T] - play a tournament')
    print('[P] - play one game')
    print('[ESC] - quit')
    return

def getMenuOption(validOptions):
    """
    Gets an option from the player. If it isn't a correct option, prompt for new input
    util it is correct. Return the option.
    """
    option = input("Please select an option: ").upper()
    while (option not in validOptions): 
            option = input("Please select a valid option: ")
    return option

def getGameMode():
    validOptions = ['0','1','q']
    option = input("Do you want to play vs player or AI? '0' for player, '1' for AI.")
    while(option not in validOptions):
        option = input("Please enter a valid input, '0', '1' or 'q': ")
    return option

def menuOptionAgain():
    validOptions = ['y','n']
    again = input("Would you like to play again? Y/N ").lower()
    while again not in validOptions:
        again = input("Please provide valid input. Y/N ").lower()
        if again == validOptions[0]:
            return True
        else:
            return False

def menuOptionOneGame():
    gameMode = getGameMode()
    playerOneName = input("Please enter the name of player one: ")
    playerTwoName = 'temp'
    print('game mode is: ' + gameMode)
    if gameMode == '1':
        playerTwoName = 'The robot overlord'
        result = startGameFunction(playerOneName, playerTwoName, gameMode)
        return menuOptionAgain(),result
    else:
        playerTwoName = input("Please enter the name of player two: ")
        result = startGameFunction(playerOneName, playerTwoName, gameMode)
        return menuOptionAgain(),result

def getPlayerNames(noPlayers):
    playerNames = []
    for i in range(int(noPlayers)):
        nameInput = input("Please enter the name of player " + str(i+1) + ": ")
        for playerNameElement in playerNames:
            if nameInput in playerNameElement:
                nameInput = input('Please enter a unique name: ')
        playerNames.append([nameInput,'human'])
    return playerNames

def tournamentRound(playerNames):
    winners = []
    if len(playerNames) <= 1:
        return playerNames
    else:
        shuffle(playerNames)
        numberOfRounds = len(playerNames)/2
        for i in range(int(numberOfRounds)):
            playerOne = playerNames.pop()
            playerTwo = playerNames.pop()
            if playerOne[1] == 'ai' or playerTwo[1] == 'ai':
                gameMode = 1
            else:
                gameMode = 0
            result = startGameFunction(playerOne[0], playerTwo[0], gameMode, i+1)
            if result == 'draw':
                gameCounter = 1
                while gameCounter < 3 and result == 'draw':
                    result = startGameFunction(playerOne[0], playerTwo[0], gameMode, i+1)
                    gameCounter += 1
            if result == 'draw':
                if bool(random.getrandbits(1)):
                    winners.append(playerOne)
                else:
                    winners.append(playerTwo)
            else:
                if result == 'playerOne':
                    winners.append(playerOne)
                elif result == 'playerTwo':
                    winners.append(playerTwo)
                else:
                    return 'ERROR'
    print('Players moving on in the tournament: {}'.format(winners))
    return winners

def menuOptionTournament():
    validnoPlayers = ['1','2','3','4','5','6','7','8']
    print('Select how many players you are: ')
    print('(The game supports 1-8 players)')
    noPlayers = input()
    while noPlayers not in validnoPlayers:
        noPlayers = input("Please provide a valid no players: ")
    
    if noPlayers == '1':
        playerOneName = input("Please enter the name of player one: ")
        result = startGameFunction(playerOneName, 'The robot tournament overlord', '1')
        print("The winner of the tournament was: " + result)
        return menuOptionAgain(),result

    elif noPlayers == '2':
        playerOneName = input("Please enter the name of player one: ")
        playerTwoName = input("Please enter the name of player two: ")
        result = startGameFunction(playerOneName, playerTwoName, '0')
        print("The winner of the tournament was: " + result)
        return menuOptionAgain(),result
    else:
        playerNames = getPlayerNames(noPlayers)
        if (len(playerNames) % 2 != 0):
            playerNames.append(['Robot overlord deluxe','ai'])
        shuffle(playerNames)
        round = tournamentRound(playerNames)
        while len(round) > 1:
            round = tournamentRound(round)
        result = round[0][0]
        print('The winner was: ' + result)
        return False,round[0][0]
    
def menuOption():
    printMenu()
    validOptions = ['P', 'T', '\x1b']
    option = getMenuOption(validOptions)
    if option == validOptions[0]:
        again,result = menuOptionOneGame()
        while again:
            again,result = menuOptionOneGame()
        if not again:
            menuOption()
    elif option == validOptions[1]:
        again,result = menuOptionTournament()
        print('The winner of the tournament (mainmenuprint): ' + result)
        menuOption()
    elif option == validOptions[2]:
        #call function for quit
        print('quit')
        return
    else:
        print('this else-case in menuOptions() shouldnt be reached')
        return

def main():
    menuOption()
    return

main()
