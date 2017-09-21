import unittest, mock, io
from contextlib import redirect_stdout
import tactoe

# Uppsala University
# Software Engineering and Project Management autumn 2017
# Group L
# Author Linn Löfquist

#TODO:
# 
# 2. Depending om indexing design decisions, change testGameWon to reflect that
#
# 3. Implement test for 
#    [q,w,e]     [t,y,u]            [1,2,3]    [0,1,2]
#    [a,s,d] and [g,h,j] mapping to [4,5,6] or [3,4,5] depeding on designdecision
#    [z,x,c]     [b,n,m]            [7,8,9]    [6,7,8]
# 
# 6. Implement test faulty input
# 8. moar stuff
#
# update!
# 
# functions tested isGameWon, playAgain,GetPlayerNames, isGamestatefull, performMove
# functions left to test getPlayerMove(io), isPositionFree, getGameMove
# functions not tested printGameState, printMoves (printfunction no need to test)


#lists are of 10 elements but index 0 never used, ' ' for first element in the list. 
#tests all possible ways of winning the game
class testGameWon(unittest.TestCase):
    
    def testEmptyGame(self):
        gameStateEmpty = [' ']*10
        self.assertEqual(tactoe.isGameWon(gameStateEmpty, 'X'), False)
        self.assertEqual(tactoe.isGameWon(gameStateEmpty, 'Y'), False)

    #Diagonally possible wins
    #[X,2,3] [1,2,X]
    #[4,X,6] [4,X,6]
    #[7,8,X] [X,8,9]
    def testDiagonally(self):
        gameStateXwinD = [' ','X',' ',' ',' ','X',' ',' ',' ','X']
        self.assertEqual(tactoe.isGameWon(gameStateXwinD, 'X'), True)
        self.assertEqual(tactoe.isGameWon(gameStateXwinD, 'Y'), False)
        gameStateXwinD = [' ',' ',' ','X',' ','X',' ','X',' ',' ']
        self.assertEqual(tactoe.isGameWon(gameStateXwinD, 'X'), True)
        self.assertEqual(tactoe.isGameWon(gameStateXwinD, 'Y'), False)

    #Horizontal possible wins
    #[X,X,X] [1,2,3] [1,2,3] 
    #[4,5,6] [X,X,X] [4,5,6] 
    #[7,8,9] [7,8,9] [X,X,X] 
    def testHorizontal(self):
        gameStateXwinH = [' ','X','X','X',' ',' ',' ',' ',' ',' ']
        self.assertEqual(tactoe.isGameWon(gameStateXwinH, 'X'), True)
        gameStateXwinH = [' ', ' ',' ',' ','X','X','X',' ',' ',' ']
        self.assertEqual(tactoe.isGameWon(gameStateXwinH, 'X'), True)
        gameStateXwinH = ['', ' ',' ',' ',' ',' ',' ','X','X','X']
        self.assertEqual(tactoe.isGameWon(gameStateXwinH, 'X'), True)

    #Vertically possible wins
    #[X,2,3] [1,X,3] [1,2,X]
    #[X,5,6] [4,X,6] [4,5,X]
    #[X,8,9] [7,X,9] [7,8,X]
    def testVertically(self):
        gameStateXwinV = [' ','X',' ',' ','X',' ',' ','X',' ',' ']
        self.assertEqual(tactoe.isGameWon(gameStateXwinV, 'X'), True)
        gameStateXwinV = [' ',' ','X',' ',' ','X',' ',' ','X',' ']
        self.assertEqual(tactoe.isGameWon(gameStateXwinV, 'X'), True)
        gameStateXwinV = [' ',' ',' ','X',' ',' ','X',' ',' ','X']
        self.assertEqual(tactoe.isGameWon(gameStateXwinV, 'X'), True)
    
    #Nobody wins
    #[X,Y,X]
    #[Y,X,X]
    #[Y,X,Y]
    def testDraw(self):
        gameStateDrawn = [' ', 'X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X', 'Y']
        self.assertEqual(tactoe.isGameWon(gameStateDrawn, 'Y'), False)
        self.assertEqual(tactoe.isGameWon(gameStateDrawn, 'X'), False)

#tests all userinput functions
class testUserInputs(unittest.TestCase):
 
    #mocking a userinput
    @mock.patch('builtins.input', side_effect='n')
    def testPlayAgainYes(self, input):
        a = io.StringIO()
        #redirects the the output from playagain function
        with redirect_stdout(a):
            ans = tactoe.playAgain()
        self.assertEqual(ans, False)

    @mock.patch('builtins.input', side_effect='y')
    def testPlayAgainNo(self, input):
        a = io.StringIO()
        #redirects the the output from playagain function
        with redirect_stdout(a):
            ans = tactoe.playAgain()
        self.assertEqual(ans, True)

    @mock.patch('builtins.input', side_effect= ['Orjan', 'Lisa'])
    def testGetPlayerNames1(self, input):
        playernames = []
        a = io.StringIO()
        #redirects the the output from playagain function
        with redirect_stdout(a):
            actualplayers = tactoe.getPlayerNames('0')    
        self.assertEqual(actualplayers, ['Orjan', 'Lisa'])
        self.assertTrue(len(actualplayers) == 2)

    @mock.patch('builtins.input', side_effect=['examplename'])
    def testGetPlayerNames1(self, input):
        playernames = []
        a = io.StringIO()
        #redirects the the output from playagain function
        with redirect_stdout(a):
            actualplayers = tactoe.getPlayerNames('1')    
        self.assertEqual(actualplayers[0], 'examplename')
        self.assertTrue(len(actualplayers) == 2)

#tests all gamealtering functions
class testGameActions(unittest.TestCase):

    def testisGameStateFull(self):
        #when gamestate is full
        gamestate = ['X','X','O','X','O','X','O','X','O','X']
        self.assertTrue(tactoe.isGameStateFull(gamestate)) 
        gamestate = [' ','X','O','X','O','X','O','X','O','X']
        self.assertTrue(tactoe.isGameStateFull(gamestate))
        
        #when gamestate is not full
        gamestate = [' ']*10
        self.assertFalse(tactoe.isGameStateFull(gamestate))
        gamestate = [' ',' ','O','X','O','X','O','X','O','X']
        self.assertFalse(tactoe.isGameStateFull(gamestate))
        gamestate = [' ',' ','O','X','O','X','O',' ','O','X']
        self.assertFalse(tactoe.isGameStateFull(gamestate))

    def testperformMove(self):
        gameState = [' ']*10
        marker = 'X'
        movesLeft = [['X','X','X','X','X'],['O','O','O','O']]
        size = 5 # X always starts with 5 stones
        iterate = 1

        while movesLeft[0] != []:
            #every time a move is placed,check location of placement in gamestate
            #and check number markers left in movesleft
            tactoe.performMove(gameState, marker, iterate, movesLeft)
            size = size - 1
            self.assertEqual(len(movesLeft[0]),size)
            self.assertEqual(gameState[iterate], 'X')
            iterate = iterate + 1

        gameState = [' ']*10
        marker = 'Y'
        size = 4 #Y always starts with 4 stones
        iterate = 1

        while movesLeft[1] != []:
            tactoe.performMove(gameState, marker, iterate, movesLeft)
            size = size - 1
            self.assertEqual(len(movesLeft[1]),size)
            self.assertEqual(gameState[iterate], 'Y')
            iterate = iterate + 1


if __name__ == '__main__':
    unittest.main()

