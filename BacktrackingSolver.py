from random import choice


def printBoard(board):
    for y in board:
        print(y)


def isSolved(board):
    for y in board:
        for x in y:
            if x == 0:
                return False
    return True


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


def getPossibleValues(board):
    possibleValues = [[[] for _ in range(9)] for _ in range(9)]
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for v in range(1, 10):
                    if possible(board, y, x, v):
                        possibleValues[y][x].append(v)
    return possibleValues


class ForwardCheckingBacktrackingSolver:

    def __init__(self):
        self.logicSteps = None
        self.solvedBoard = None

    def solve(self, board, logicSteps=0):
        possibleValues = getPossibleValues(board)
        logicSteps += 1
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    try:
                        testInput = choice(possibleValues[y][x])
                        board[y][x] = testInput
                        if isSolved(board):
                            self.logicSteps = logicSteps
                            self.solvedBoard = board
                        logicSteps += self.solve(board, logicSteps)[0]
                    except IndexError:
                        return logicSteps, board
        return logicSteps, board


class SimpleBacktrackingSolver:

    def __init__(self):
        self.logicSteps = None
        self.solvedBoard = None

    def solve(self, board, logicSteps=0):
        if not isSolved(board):
            logicSteps += 1
            for y in range(9):
                for x in range(9):
                    if board[y][x] == 0:
                        for testInput in range(1, 10):
                            if possible(board, y, x, testInput):
                                board[y][x] = testInput
                                logicSteps += self.solve(board, logicSteps)[0]
                                if not isSolved(board):
                                    board[y][x] = 0
                        return logicSteps, board
        return logicSteps, board
