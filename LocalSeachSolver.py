import math
from random import choice


class SimulatedAnnealing:
    def __init__(self):
        self.solved = False

    def solve(self, board):
        board = self.generateRandomNumInBlocks(board)
        print(board)
        print(self.costFunction(board))

    def generateRandomNumInBlocks(self, board):
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    block = self.getNumbersInBlock(y, x, board)
                    board[y][x] = choice([i for i in range(1, 10) if i not in block])
        return board

    def getNumbersInBlock(self, row, col, board):
        blocks = [[] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                blocks[((y // 3) * 3) + (x // 3)].append(board[y][x])
        block = blocks[((row // 3) * 3) + (col // 3)]
        return block

    def costFunction(self, board):
        cost = 0
        # count duplicates in the row
        for y in board:
            for x in y:
                for z in range(9):
                    if x == z:
                        cost += 1
        # Transpose board
        tBoard = [list(x) for x in list(zip(board))]
        # Count duplicates in columns
        for y in tBoard:
            for x in y:
                for z in range(9):
                    if x == z:
                        cost += 1
        return cost



    def schedule(self, board):
        pass
