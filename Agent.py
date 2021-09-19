import copy

from Environment import Environment
from BacktrackingSolver import SimpleBacktrackingSolver, ForwardCheckingBacktrackingSolver
from LocalSeachSolver import SimulatedAnnealing


def printBoard(board):
    for y in board:
        print(y)


class Agent:

    def __init__(self):
        self.nextMove = []
        self.logicSteps = int
        self.currentEnvironment = None

    #   Check if the current environment is solved
    def isSolved(self, board: list):
        for y in board:
            for x in y:
                if x == 0:
                    return False
        return True

    #   Method to initialize an environment, if there is a current board archive it
    def initializeEnvironment(self, difficultly, boardNumber):
        self.currentEnvironment = Environment(difficultly, boardNumber)

    def solveWithSimpleBacktracking(self):
        return SimpleBacktrackingSolver().solve(copy.deepcopy(self.currentEnvironment.getBoard()))

    def solveWithForwardCheckingBacktracking(self):
        return ForwardCheckingBacktrackingSolver().solve(copy.deepcopy(self.currentEnvironment.getBoard()))

    def solveSimulatedAnnealing(self, temp, beta):
        return SimulatedAnnealing().solve(copy.deepcopy(self.currentEnvironment.getBoard(), temp, beta))


if __name__ == "__main__":
    difficulties = ["Easy", "Med", "Hard", "Evil"]
    print("Enter desired board difficulty [\"Easy\", \"Med\",\"Hard\",\"Evil\"]:")
    difficulty = input()
    print("Enter board number [1-5]:")
    boardNumber = input()
    a = Agent()
    a.initializeEnvironment(difficulty, boardNumber)
    bt = a.solveWithSimpleBacktracking()
    print("SolveBacktracking Steps: " + str(bt[0]))
    printBoard(bt[1])

    fc = a.solveWithForwardCheckingBacktracking()
    print("SolveWithForwardChecking Steps: " + str(fc[0]))
    printBoard(fc[1])
    # print(a.solveSimulatedAnnealing(2000, 5))
