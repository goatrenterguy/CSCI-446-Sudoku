class BacktrackingSolver:

    def __init__(self):
        self.logicSteps = None
        self.solvedBoard = None

    def solve(self, board, logicSteps=0):
        logicSteps += 1
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for testInput in range(1, 10):
                        #print("Testing value: " + str(testInput) + " at coordinates (" + str(y) + "," + str(x) + ")")
                        if self.possible(board, y, x, testInput):
                            board[y][x] = testInput
                            # print(logicSteps)
                            # print("steps: " + str(logicSteps), " board is solved= ", self.isSolved(board))
                            # self.printBoard(board)
                            if self.isSolved(board):
                                self.logicSteps = logicSteps
                                self.solvedBoard = board
                            self.solve(board, logicSteps)
                            if not self.isSolved(board):
                                board[y][x] = 0
                return self.logicSteps, self.solvedBoard
        #input("Here is the first solution. Continue to look for more?")
        #quit()

    def possible(self, board, y, x, n):
        # check row
        for k in range(9):
            if board[y][k] == n:
                return False

        # check column
        for k in range(9):
            if board[k][x] == n:
                return False

        # check cell
        cornerX = (x // 3) * 3
        cornerY = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[cornerY + i][cornerX + j] == n:
                    return False
        return True

    def isSolved(self, board):
        for y in board:
            for x in y:
                if x == 0:
                    return False
        return True

    def printBoard(self, board):
        for y in board:
            print(y)
