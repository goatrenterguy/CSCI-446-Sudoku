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

    #   Method to initialize an environment
    def initializeEnvironment(self, difficultly, boardNumber):
        self.currentEnvironment = Environment(difficultly, boardNumber)

    #   Method to solve the current environments board with simple backtracking
    def solveWithSimpleBacktracking(self):
        return SimpleBacktrackingSolver().solve(copy.deepcopy(self.currentEnvironment.getBoard()), 0)

    #   Method to solve the current environments board with forward checking backtracking
    def solveWithForwardCheckingBacktracking(self):
        return ForwardCheckingBacktrackingSolver().solve(copy.deepcopy(self.currentEnvironment.getBoard()), 0)

    #   Method to solve the current environments board with a simulated annealing algorithm
    def solveSimulatedAnnealing(self, temp, tau):
        return SimulatedAnnealing().solve(copy.deepcopy(self.currentEnvironment.getBoard()), temp, tau)


if __name__ == "__main__":
    difficulties = ["Easy", "Med", "Hard", "Evil"]
    print("Enter desired board difficulty [\"Easy\", \"Med\",\"Hard\",\"Evil\"]:")
    difficulty = input()
    print("Enter board number [1-5]:")
    boardNumber = input()
    a = Agent()
    runs = 100

    # Compare backtracking solvers average attempts
    # for dif in difficulties:
    #     for nums in range(1, 6):
    #         a.initializeEnvironment(dif, nums)
    #         fcAverage = 0
    #         btAverage = 0
    #         for run in range(runs):
    #             fcAverage += a.solveWithForwardCheckingBacktracking()[0]
    #             btAverage += a.solveWithSimpleBacktracking()[0]
    #         print("Simple Backtracking Average Steps (Diff: " + dif + ", Num: " + str(nums) + "): " + str(btAverage / runs))
    #         print("Forward Backtracking Average Steps (Diff: " + dif + ", Num: " + str(nums) + "): " + str(fcAverage / runs))
    a.initializeEnvironment(difficulty, boardNumber)
    print(a.solveSimulatedAnnealing(500, 60))
