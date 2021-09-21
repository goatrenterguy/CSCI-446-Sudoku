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


class BacktrackingAC:

    def __init__(self, board):
        self.logicSteps = 0
        self.solvedBoard = None
        self.cells = []
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    self.cells.append(Cell(x, y))

    def solve(self, board):
        if isSolved(board):
            return self.logicSteps, board
        self.logicSteps += 1
        for cell in self.cells:
            cell.legalValues(board)
        minCell = self.cells[0]
        for cell in self.cells:
            if len(minCell.values) >= len(cell.values) and cell.value == 0 and len(minCell.values) > 0:
                if cell.value == 0 and len(cell.values) == 0:
                    return
                minCell = cell

        for value in self.cells[self.cells.index(minCell)].values:
            # print("Testing ", value, " in ", "(", minCell.x, ", ", minCell.y, ") from ", minCell.values)
            board[minCell.y][minCell.x] = value
            self.cells[self.cells.index(minCell)].value = value
            # self.cells[self.cells.index(minCell)].values.remove(value)
            if isSolved(board):
                self.solvedBoard = board
            self.solve(board)
            if not isSolved(board):
                board[minCell.y][minCell.x] = 0
                self.cells[self.cells.index(minCell)].value = 0
        return self.logicSteps, self.solvedBoard


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.values = []
        self.value = 0

    def legalValues(self, board):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if self.value != 0:
            # print("My value is set")
            self.values.remove(self.value)
            #    self.values = [self.value]
            return
        # else:

        # check row
        for k in range(9):
            if board[self.y][k] in self.values:
                self.values.remove(board[self.y][k])

        # check column
        for k in range(9):
            if board[k][self.x] in self.values:
                self.values.remove(board[k][self.x])

        # check cell
        cornerX = (self.x // 3) * 3
        cornerY = (self.y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[cornerY + i][cornerX + j] in self.values:
                    self.values.remove(board[cornerY + i][cornerX + j])


def getPossibleValues(board):
    """
    Calculates all possible values that can be entered into the each cell
    :param board: 2D list that contains the sudoku board
    :return: Tuple that contains the list of possibilities for each cell and a boolean if the board inputted can be solved
    """
    # Initialize 3D list
    possibleValues = [[[] for _ in range(9)] for _ in range(9)]
    # Initialize if the board is solvable
    stillPossible = True
    # Nested for loop to iterate through every cell in the board
    for y in range(9):
        for x in range(9):
            # Check if the boards value is zero that means it can be changed
            if board[y][x] == 0:
                # Loop though values 1-9
                for v in range(1, 10):
                    # See if the current value v is one of the possible solutions
                    if possible(board, y, x, v):
                        possibleValues[y][x].append(v)
                # If the length of the array in a cell is zero
                # when its cells value is zero then the board is not solvable
                if len(possibleValues[y][x]) == 0:
                    stillPossible = False
            else:
                # Mark the cells that can not be edited with a -1 (Used for debuggin)
                possibleValues[y][x].append(-1)
    return possibleValues, stillPossible


class ForwardCheckingBacktrackingSolver:

    def solve(self, board: list, logicSteps: int = 0) -> tuple:
        """
        Method to solve sudoku with a forward checking backtracking algorithm
        :param board: 2D list that contains the board
        :param logicSteps: The number of recursive calls
        :return: The number of recursive calls, the board and if it is solvable
        """
        # Get a all possible solution for every cell on the board
        allPossible = getPossibleValues(board)
        # Extract the list from the tuple
        possibleValues = allPossible[0]
        # Extract the boolean from tuple
        solvable = allPossible[1]
        # If board is not solvable return
        if solvable:
            # Increment recursive call count
            logicSteps += 1
            # Iterate through each cell in the board
            for y in range(9):
                for x in range(9):
                    # Check if cell is editable
                    if board[y][x] == 0:
                        try:
                            while True:
                                # Randomly select a possible value for that cell
                                testInput = choice(possibleValues[y][x])
                                board[y][x] = testInput
                                # Recursive call to find next value or see if current does not work
                                nextState = self.solve(board)
                                # Increment logic steps based on recursive depth of call
                                logicSteps += nextState[0]
                                # If value makes another cell unsolvable set cell back to zero
                                # and remove the attempted number from possibilities
                                if not nextState[2]:
                                    board[y][x] = 0
                                    possibleValues[y][x].remove(testInput)
                                    # If there are no possibilities for that cell go back another step
                                    if len(possibleValues[y][x]) == 0:
                                        return logicSteps, board, False
                                else:
                                    # If value is found break out of while
                                    break
                        except IndexError:
                            # If cell has no possible return not solvable
                            return logicSteps, board, False
        return logicSteps, board, solvable


class SimpleBacktrackingSolver:

    def solve(self, board, logicSteps=0):
        if not isSolved(board):
            logicSteps += 1
            for y in range(9):
                for x in range(9):
                    if board[y][x] == 0:
                        for testInput in range(1, 10):
                            if possible(board, y, x, testInput):
                                board[y][x] = testInput
                                logicSteps += self.solve(board)[0]
                                if not isSolved(board):
                                    board[y][x] = 0
                        return logicSteps, board
        return logicSteps, board
