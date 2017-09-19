import unittest
import tictactoe

#TODO:
# 1. Mainloop in tictactoe.py needs to be moved to another file
#    so the automated tests can be run.
# 
# 2. Depending om indexing design decisions, change testGameWon to reflect that
#
# 3. Implement test for 
#    [q,w,e]     [t,y,u]            [1,2,3]    [0,1,2]
#    [a,s,d] and [g,h,j] mapping to [4,5,6] or [3,4,5] depeding on designdecision
#    [z,x,c]     [b,n,m]            [7,8,9]    [6,7,8]
# 
# 4. Implement test markers left
# 5. Implement test timeout
# 6. Implement test faulty input
# 7. Since current version of code to test is python 2.something, tests are accordingly
#    update teststuff to 3.6
# 8. moar stuff

#lists are of 10 elements but index 0 never used, ' ' for first element in the list. 
#tests all possible ways of winning the game
class testGameWon(unittest.TestCase):
    
    def testEmptyGame(self):
        gameStateEmpty = [' ']*10
        self.assertEqual(tictactoe.isGameWon(gameStateEmpty, 'X'), False)
        self.assertEqual(tictactoe.isGameWon(gameStateEmpty, 'Y'), False)

    #Diagonally possible wins
    #[X,2,3] [1,2,X]
    #[4,X,6] [4,X,6]
    #[7,8,X] [X,8,9]
    def testDiagonally(self):
        gameStateXwinD = [' ','X',' ',' ',' ','X',' ',' ',' ','X']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinD, 'X'), True)
        self.assertEqual(tictactoe.isGameWon(gameStateXwinD, 'Y'), False)
        gameStateXwinD = [' ',' ',' ','X',' ','X',' ','X',' ',' ']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinD, 'X'), True)
        self.assertEqual(tictactoe.isGameWon(gameStateXwinD, 'Y'), False)

    #Horizontal possible wins
    #[X,X,X] [1,2,3] [1,2,3] 
    #[4,5,6] [X,X,X] [4,5,6] 
    #[7,8,9] [7,8,9] [X,X,X] 
    def testHorizontal(self):
        gameStateXwinH = [' ','X','X','X',' ',' ',' ',' ',' ',' ']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinH, 'X'), True)
        gameStateXwinH = [' ', ' ',' ',' ','X','X','X',' ',' ',' ']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinH, 'X'), True)
        gameStateXwinH = ['', ' ',' ',' ',' ',' ',' ','X','X','X']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinH, 'X'), True)

    #Vertically possible wins
    #[X,2,3] [1,X,3] [1,2,X]
    #[X,5,6] [4,X,6] [4,5,X]
    #[X,8,9] [7,X,9] [7,8,X]
    def testVertically(self):
        gameStateXwinV = [' ','X',' ',' ','X',' ',' ','X',' ',' ']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinV, 'X'), True)
        gameStateXwinV = [' ',' ','X',' ',' ','X',' ',' ','X',' ']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinV, 'X'), True)
        gameStateXwinV = [' ',' ',' ','X',' ',' ','X',' ',' ','X']
        self.assertEqual(tictactoe.isGameWon(gameStateXwinV, 'X'), True)
    
    #Nobody wins
    #[X,Y,X]
    #[Y,X,X]
    #[Y,X,Y]
    def testDraw(self):
        gameStateDrawn = [' ', 'X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X', 'Y']
        self.assertEqual(tictactoe.isGameWon(gameStateDrawn, 'Y'), False)
        self.assertEqual(tictactoe.isGameWon(gameStateDrawn, 'X'), False)

if __name__ == '__main__':
    unittest.main()

