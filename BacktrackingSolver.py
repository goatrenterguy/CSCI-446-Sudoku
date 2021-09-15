class BacktrackingSolver:

    def __init__(self, board: list):
        self.board = board
        self.logicSteps = 0

    def solve(self):
        self.logicSteps += 1
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 0:
                    for testInput in range(1, 9):
                        if self.possible(x, y, testInput):
                            self.board[x][y] = testInput
                            self.solve()
                            self.board[x][y] = 0
                    return self.board

    def possible(self, x, y, testInput):
        # check row
        for k in range(8):
            if self.board[x][k] == testInput:
                return False

        # check column
        for k in range(8):
            if self.board[k][y] == testInput:
                return False

        # check cell
        cornerX = (x // 3) * 3
        cornerY = (y // 3) * 3
        for i in range(2):
            for j in range(2):
                if self.board[cornerX + i][cornerY + j] == testInput:
                    return False

        return True
