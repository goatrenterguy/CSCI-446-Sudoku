import math
from random import choice


class SimulatedAnnealing:
    def __init__(self):
        self.solved = False
        self.initialBoard = None

    def solve(self, board):
        self.initialBoard = board
        board = self.generateRandomNumInBlocks(board)
        print(board)
        print(self.costFunction(board))
        updates = 0
        while self.annealingSchedule(200, .9, updates) != 0:
            nextBoard = next(board)
    #         Randomly move the variables inside their blocks
    #           calculate the change in cost with costFunciton()
    #               if the change in cost is greater then 0
    #                     current board becomes neighbor board
    #               else
    #                      if probabilty keep anyway

    #   Swap two of the cells in each box
    def nextState(self, board):
        one = choice(range(9))
        two = choice(range(9))
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                initialBlock = self.getNumbersInBlock(row, col, self.initialBoard)
                while one == two and board[initialBlock[one][0]][initialBlock[one][1]] != 0 and board[initialBlock[two][0]][initialBlock[two][1]] != 0:
                    one = choice(range(9))
                    two = choice(range(9))
                # Swap swap
                board[initialBlock[one][0]][initialBlock[one][1]], board[initialBlock[two][0]][initialBlock[two][1]] = board[initialBlock[two][0]][initialBlock[two][1]], board[initialBlock[one][0]][initialBlock[one][1]]
        return board

    def generateRandomNumInBlocks(self, board):
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    block = self.getNumbersInBlock(y, x, board)
                    numbers = []
                    for i in block:
                        numbers.append(board[i[0]][i[1]])
                    board[y][x] = choice([i for i in range(1, 10) if i not in numbers])
        return board

    def annealingSchedule(self, initialTemp, coolingRate, updates):
        return (initialTemp * coolingRate) / (coolingRate + updates)

    def getNumbersInBlock(self, row, col, board):
        blocks = [[] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                blocks[((y // 3) * 3) + (x // 3)].append((y, x))
        block = blocks[((row // 3) * 3) + (col // 3)]
        return block

    def costFunction(self, board):
        cost = 0
        # count duplicates in the row
        for y in board:
            for x in range(9):
                for z in range(x + 1, 9):
                    if y[x] == y[z]:
                        cost += 1
        # Transpose board
        tBoard = [list(x) for x in list(zip(board))]
        # Count duplicates in columns
        for y in tBoard[0]:
            for x in range(9):
                for z in range(x + 1, 9):
                    if y[x] == y[z]:
                        cost += 1
        return cost



    def schedule(self, board):
        pass
