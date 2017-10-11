# SoftEng autumn 2017
# Uppsala universty
# Author: Henrik Thorsell
# Group L

import getch
import copy
from tactoe import loopExternal
import random
from random import shuffle
from tactoe import getAIDifficulty
from gameengine import playAIvsAI

def startGameFunction(playerOne, playerTwo, gameMode, round=0):
    """
    Set the called function to whichever function your game platform uses
    """
    return loopExternal(playerOne, playerTwo, gameMode, round)


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
    print("Please select an option: ")
    option = getch.getch().upper()
    while (option not in validOptions): 
            print("Please select a valid option: ")
            option = getch.getch().upper()
    return option

def getGameMode():
    """
    Gets a game mode option from the player, either 0 for vs another player, 1 for vs computer or 2 for computer vs computer.
    """
    validOptions = ['0','1','2','q']
    print("Do you want to play vs player or the computer?")
    print("'0' for vs player, '1' for vs computer, '2' for computer vs computer")
    option = getch.getch().lower()
    while(option not in validOptions):
        print("Please enter a valid input, '0', '1', '2' or 'q': ")
        option = getch.getch().lower()
    return option

def menuOptionPlayAgain():
    """
    Asks the player to play again, repeatedly asking until either 'y' or 'n' is provided.
    """
    validOptions = ['y','n']
    print("Would you like to play again? Y/N ")
    again = getch.getch().lower()
    while again not in validOptions:
        print("Please provide a valid input. Y/N ")
        again = getch.getch().lower()
    if again == validOptions[0]:
        return True
    else:
        return False
    

def menuOptionOneGame():
    """
    This function handles the logic if a player in the menu chooses to play one game.
    After the game is finished the player is asked to play again, and the result of the first
    game together with a boolean that represents if the player wishes another game or not.
    """
    gameMode = getGameMode() #Ask if the player wants PvP or PvAI.
    if gameMode == 'q':
        return None
    playerOne = []
    playerTwo = []
    if gameMode == '2': # AI vs AI option
        firstAIDifficulty = getAIDifficulty()
        secondAIDifficulty = getAIDifficulty()
        playerOne.append('Robot overlord 1')
        playerOne.append(firstAIDifficulty)
        playerTwo.append('Robot overlord 2')
        playerTwo.append(secondAIDifficulty)
        #make AIs play each other
        play = True
        while play:
            result = playAIvsAI(playerOne, playerTwo)
            play = menuOptionPlayAgain()
        return False, result
    if gameMode == '1':
        playerOne.append(input("Please enter the name of player one: "))
        playerOne.append('human')
        playerTwo.append('The robot overlord') #If PvAI this is the name of the AI player.
        playerTwo.append(getAIDifficulty())
        play = True
        while play:
            result = startGameFunction(playerOne, playerTwo, gameMode)
            play = menuOptionPlayAgain()
        return play, result
    else:
        playerOne.append(input("Please enter the name of player one: "))
        playerOne.append('human')
        playerTwo.append(input("Please enter the name of player two: ")) #If PvP, get the second
        #player name
        playerTwo.append('human')
        play = True
        while play:
            result = startGameFunction(playerOne, playerTwo, gameMode)
            play = menuOptionPlayAgain()
        return play, result

def getPlayerNames(noPlayers):
    """
    Prompts the names of 'noPlayers' amount of players (for the tournament mode). Returns a list
    of tuples where the first element is the player name and the second is a string indicating
    it is the name for a human player.
    """
    playerNames = []
    for i in range(int(noPlayers)):
        nameInput = input("Please enter the name of player " + str(i+1) + ": ")
        for playerNameElement in playerNames:
            if nameInput in playerNameElement:
                nameInput = input('Please enter a unique name: ')
        playerNames.append([nameInput,'human'])
    return playerNames

def tournamentRound(playerNames):
    """
    Returns a list with one tuple representing the winner of the tournament. The tuples first
    element is the name of the winning player and the second is the string 'human' or 'ai'
    indicating if the player was a human or AI player.
    """
    winners = []
    # If there is only one player left, that is the winner.
    if len(playerNames) <= 1:
        return playerNames
    # If there are several players, play elminination matches.
    else:
        shuffle(playerNames) #Randomize the order so poping two players randomly seeds the match
        numberOfRounds = len(playerNames)/2
        for i in range(int(numberOfRounds)):
            playerOne = playerNames.pop()
            playerTwo = playerNames.pop()
            aiDifficulties = ['easy', 'normal', 'hard']
            # AI vs AI
            if playerOne[1] in aiDifficulties and playerTwo[1] in aiDifficulties:
                gameMode = '3'
            # One player vs AI
            elif playerOne[1] in aiDifficulties or playerTwo[1] in aiDifficulties:                
                gameMode = '1'
            # Player vs Player
            else:
                gameMode = '0'
            result = startGameFunction(playerOne, playerTwo, gameMode, i+1)
            if result is None:
                print("The tournament was aborted!")
                return None
            if result == 'draw':
                gameCounter = 1
                while gameCounter < 3 and result == 'draw':
                    result = startGameFunction(playerOne, playerTwo, gameMode, i+1)
                    gameCounter += 1
            if result == 'draw':
                print("Flipping a coin to decide the winner after three games!")
                if bool(random.getrandbits(1)):
                    print("The winner was: " + playerOne[0])
                    winners.append(playerOne)
                else:
                    print("The winner was: " + playerTwo[0])
                    winners.append(playerTwo)
            else:
                if result == playerOne:
                    winners.append(playerOne)
                elif result == playerTwo:
                    winners.append(playerTwo)
                else:
                    return 'ERROR'
    if len(winners) > 1:
        print('Players moving on in the tournament: {}'.format(", ".join(str(winner[0]) for winner in winners)))
    return winners

def menuOptionTournament():
    """
    This function implements the tournament logic. First by from the players getting the amount
    of human participants in the tournamet, then getting their names. If the amount of players
    are just one or two, the regular single game function is called, otherwise the tournament-
    round-function is called repeatedly until everyone but one player has been eliminated.
    The remaining player is then the victor.
    """
    validnoPlayers = ['1','2','3','4','5','6','7','8']
    print('Select how many players you are: ')
    print('(The game supports 1-8 players)')
    noPlayers = getch.getch()
    while noPlayers not in validnoPlayers:
        print("Please provide a valid no players: ")
        noPlayers = getch.getch()
    
    if noPlayers == '1':
        playerOne = []
        playerTwo = []
        playerOneName = input("Please enter the name of player one: ")
        playerOne.append([playerOneName,'human'])
        AIDifficulty = getAIDifficulty()
        playerTwo.append(['The robot tournament overlord', AIDifficulty])
        play = True
        while play:
            result = startGameFunction(playerOne[0], playerTwo[0], '1', 0)
            if result is None:
                print("Tournament was aborted, no winner!")
            else:
                print("The winner of the tournament is: " + result[0])
            play = menuOptionPlayAgain()
        return play, result

    elif noPlayers == '2':
        playerOne = []
        playerTwo = []
        playerOneName = input("Please enter the name of player one: ")
        playerOne.append([playerOneName, 'human'])
        playerTwoName = input("Please enter the name of player two: ")
        playerTwo.append([playerTwoName, 'human'])
        play = True
        while play:
            result = startGameFunction(playerOne[0], playerTwo[0], '0', 0)
            if result is not None:
                print("The winner of the tournament was: " + result[0])
            else:
                print("There is no winner, the tournament was aborted")
            play = menuOptionPlayAgain()
        return play,result
    else:
        playerNames = getPlayerNames(noPlayers)
        if (len(playerNames) % 2 != 0):
            print("Please select AI difficulty for 'Robot overlord gold': ")
            goldDifficulty = getAIDifficulty()
            playerNames.append(['Robot overlord gold',goldDifficulty])
        if (len(playerNames) % 4 != 0):
            print("Please select difficulty for robot overlord silver and bronze: ")
            silverDifficulty = getAIDifficulty()
            bronzeDifficulty = getAIDifficulty()
            playerNames.append(['Robot overlord silver', silverDifficulty])
            playerNames.append(['Robot overlord bronze', bronzeDifficulty])
        play = True
        playerNamesBackup = copy.deepcopy(playerNames)
        while play:
            shuffle(playerNames)
            print(playerNames)
            round = tournamentRound(playerNames)
            print(round)
            while len(round) > 1:
                round = tournamentRound(round)
            result = round
            print("The winner of the tournament was: " + result[0][0])
            play = menuOptionPlayAgain()
            if play:
                playerNames = copy.deepcopy(playerNamesBackup)
        return False,result
                            
def menuOption():
    """
    Menu option function calls the printMenu function to print the user interface to the
    terminal, then it handles the players game mode choice and starts either the single game
    or tournament depending on which option is selected.
    """
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

        if again is None:
            print("Tournament was aborted1!")
            menuOption()
        if result is None:
            print("Tournament was aborted2!")
            menuOption()
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
