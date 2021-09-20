import copy
import math
import random
from random import choice


class SimulatedAnnealing:
    def __init__(self):
        self.initialBoard = None

    def solve(self, board, temp, tau):
        self.initialBoard = copy.deepcopy(board)
        board = self.generateRandomNumInBlocks(board)
        updates = 1
        T = self.annealingScheduleTwo(temp, tau, updates)
        while T > .4:
            nextBoard = self.nextState(copy.deepcopy(board))
            costDelta = self.costFunction(board) - self.costFunction(nextBoard)
            if costDelta > 0:
                board = nextBoard
                if self.costFunction(board) == 0:
                    return board, self.costFunction(board), updates
            elif random.random() < math.exp(costDelta / T):
                board = nextBoard
            print("Cost Delta: " + str(costDelta) + " Probability: " + str(math.exp(costDelta / T)) + " Temp: " + str(T))
            updates += 1
            T = self.annealingScheduleTwo(temp, tau, updates)
        return board, self.costFunction(board), updates

    #   Swap two of the cells in each box
    def nextState(self, board):
        one = choice(range(9))
        two = choice(range(9))
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                initialBlock = self.getNumbersInBlock(row, col, self.initialBoard)
                while one == two or self.initialBoard[initialBlock[one][0]][initialBlock[one][1]] != 0 or self.initialBoard[initialBlock[two][0]][initialBlock[two][1]] != 0:
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

    def annealingScheduleTwo(self, initialTemp, coolingRate, updates):
        return initialTemp/(1 + (coolingRate * math.log(1 + updates, 10))) - 1

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

    def printBoard(self, board):
        for y in board:
            print(y)
