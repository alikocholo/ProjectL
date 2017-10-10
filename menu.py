# SoftEng autumn 2017
# Uppsala universty
# Author: Henrik Thorsell
# Group L

from tactoe import loopExternal
import random
from random import shuffle
from tactoe import getAIDifficulty

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
    """
    Gets a game mode option from the player, either 0 for vs another player or 1 for vs AI.
    """
    validOptions = ['0','1','q']
    option = input("Do you want to play vs player or AI? '0' for player, '1' for AI.")
    while(option not in validOptions):
        option = input("Please enter a valid input, '0', '1' or 'q': ")
    return option

def menuOptionAgain():
    """
    Asks the player to play again, repeatedly asking until either 'y' or 'n' is provided.
    """
    validOptions = ['y','n']
    again = input("Would you like to play again? Y/N ").lower()
    while again not in validOptions:
        again = input("Please provide valid input. Y/N ").lower()
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
    playerOne = []
    playerTwo = []
    playerOne.append(input("Please enter the name of player one: "))
    playerOne.append('human')
    print('game mode is: ' + gameMode)
    if gameMode == '1':
        playerTwo.append('The robot overlord') #If PvAI this is the name of the AI player.
        playerTwo.append(getAIDifficulty()) #standard difficulty
        result = startGameFunction(playerOne, playerTwo, gameMode) #Play a round.
        return menuOptionAgain(),result #Return the bool if the player wants to play again &
        #result
    else:
        playerTwo.append(input("Please enter the name of player two: ")) #If PvP, get the second
        #player name
        playerTwo.append('human')
        result = startGameFunction(playerOne, playerTwo, gameMode) #Play the game,
        #return the result and the answer to the question of the player wants to play again.
        return menuOptionAgain(),result

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
        if type(playerNames) != list:
            return winners
        shuffle(playerNames) #Randomize the order so poping two players randomly seeds the match
        numberOfRounds = len(playerNames)/2
        for i in range(int(numberOfRounds)):
            playerOne = playerNames.pop()
            playerTwo = playerNames.pop()
            aiDifficulties = ['easy', 'normal', 'hard']
            print("Deciding game mode in tournamentRound function")
            if playerOne[1] in aiDifficulties or playerTwo[1] in aiDifficulties:
                print("Setting gameMode = 1 (ai) in menu function")
                gameMode = '1'
            else:
                print("Setting gameMode = 0 (pvp) in menu function")
                gameMode = '0'
            result = startGameFunction(playerOne, playerTwo, gameMode, i+1)
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
                if result == 'playerOne':
                    winners.append(playerOne)
                elif result == 'playerTwo':
                    winners.append(playerTwo)
                else:
                    return 'ERROR'
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
        if result != None:
            print("The winner of the tournament was: " + result)
        else:
            print("There is no winner, the tournament was aborted")
        return menuOptionAgain(),result
    else:
        playerNames = getPlayerNames(noPlayers)
        if (len(playerNames) % 2 != 0):
            playerNames.append(['Robot overlord gold','hard'])
        if (len(playerNames) % 4 != 0):
            playerNames.append(['Robot overlord silver', 'medium'])
            playerNames.append(['Robot overlord bronze', 'easy'])
        shuffle(playerNames)
        round = tournamentRound(playerNames)
        while len(round) > 1:
            round = tournamentRound(round)
        if round == []:
            return False, None
        result = round[0][0]
        print('The winner was: ' + result)
        return False,round[0][0]
    
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
        if result != None:
            print('The winner of the tournament (mainmenuprint): ' + result)
        else:
            print('Exiting to the main menu...')
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
