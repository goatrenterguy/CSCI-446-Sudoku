class BacktrackingSolver:
    def __init__(self):
        self.solved = False

    def solve(self, board, logicSteps=0):
        logicSteps += 1
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for testInput in range(1, 10):
                        print(
                            "Testing value: " + str(testInput) + " at coordinates (" + str(y) + "," + str(x) + ")")
                        if self.possible(board, y, x, testInput):
                            board[y][x] = testInput

                            print("steps: " + str(logicSteps), " board is solved= ", self.isSolved(board))
                            self.printBoard(board)
                            self.solve(board, logicSteps)
                            board[y][x] = 0
                    return board, logicSteps
        return board, logicSteps
        # input("Here is the first solution. Continue to look for more?")

    @staticmethod
    def possible(board, y, x, n):
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

    @staticmethod
    def isSolved(board):
        for y in board:
            for x in y:
                if x == 0:
                    return False
        return True

    @staticmethod
    def printBoard(board):
        for y in board:
            print(y)
