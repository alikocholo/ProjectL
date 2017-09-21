import unittest, mock, io
from contextlib import redirect_stdout
import tactoe

# Uppsala University
# Software Engineering and Project Management autumn 2017
# Group L
# Author Linn Löfquist

#TODO:
# 
# 1. Implement test for getPlayerMove()
#    [q,w,e]     [t,y,u]            [1,2,3]
#    [a,s,d] and [g,h,j] mapping to [4,5,6]
#    [z,x,c]     [b,n,m]            [7,8,9] 
# 
# 2. Implement test faulty input
# 3. Implement test for more edgecases
#
# 
# Functions not tested printGameState, printMoves (printfunctions I see no need to test)
# Comment: lists are of 10 elements but index 0 never used, ' ' for first element in the list. 

#Tests all possible ways of winning the game
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

#tests userinput functions
class testUserInputs(unittest.TestCase):
 
    #mock simulates userinput
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
        with redirect_stdout(a):
            ans = tactoe.playAgain()
        self.assertEqual(ans, True)

    @mock.patch('builtins.input', side_effect= ['Orjan', 'Lisa'])
    def testGetPlayerNames1(self, input):
        playernames = []
        a = io.StringIO()
        with redirect_stdout(a):
            actualplayers = tactoe.getPlayerNames('0')    
        self.assertEqual(actualplayers, ['Orjan', 'Lisa'])
        self.assertTrue(len(actualplayers) == 2)

    @mock.patch('builtins.input', side_effect=['examplename'])
    def testGetPlayerNames2(self, input):
        playernames = []
        a = io.StringIO()
        with redirect_stdout(a):
            actualplayers = tactoe.getPlayerNames('1')    
        self.assertEqual(actualplayers[0], 'examplename')
        self.assertTrue(len(actualplayers) == 2)
    
    #tests the correct choosing of pvp gamemode = 1
    @mock.patch('builtins.input', side_effect= '0')
    def testGetGameModePvp(self, input):
        a = io.StringIO()
        with redirect_stdout(a):
            actualgamemode = tactoe.getGameMode()
        self.assertEqual(actualgamemode, '0')

    #tests the correct choosing of AI gamemode = 1
    @mock.patch('builtins.input', side_effect= '1')
    def testGetGameModePvAI(self, input):
        a = io.StringIO()
        with redirect_stdout(a):
            actualgamemode = tactoe.getGameMode()
        self.assertEqual(actualgamemode, '1')

    #tests entereing wrong alt before choosing AI =1
    @mock.patch('builtins.input', side_effect= ['ö','o','3','l','5','1'])
    def testGetGameMode(self, input):
        a = io.StringIO()
        with redirect_stdout(a):
            actualgamemode = tactoe.getGameMode()
        self.assertEqual(actualgamemode, '1')

#tests gamealtering functions
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

    def testIsPositionFree(self):
        gameState = [' ',' ',' ',' ','X','X','O',' ',' ',' ']
        pos1 = tactoe.isPositionFree(gameState,1)
        pos2 = tactoe.isPositionFree(gameState,2)
        pos3 = tactoe.isPositionFree(gameState,3)
        self.assertTrue(pos1)
        self.assertTrue(pos2)
        self.assertTrue(pos3)
        
        pos4 = tactoe.isPositionFree(gameState,4)
        pos5 = tactoe.isPositionFree(gameState,5)
        pos6 = tactoe.isPositionFree(gameState,6)
        self.assertFalse(pos4)
        self.assertFalse(pos5)
        self.assertFalse(pos6)

        pos7 = tactoe.isPositionFree(gameState,7)
        pos8 = tactoe.isPositionFree(gameState,8)
        pos9 = tactoe.isPositionFree(gameState,9)
        self.assertTrue(pos7)
        self.assertTrue(pos8)
        self.assertTrue(pos9)

        #should always be false since its placement is outside board?
        edge = tactoe.isPositionFree(gameState,0)
        self.assertFalse(edge)


if __name__ == '__main__':
    unittest.main()

