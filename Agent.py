from Environment import Environment
from BacktrackingSolver import BacktrackingSolver
from LocalSeachSolver import SimulatedAnnealing


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

    def solveWithBacktracking(self):
        return BacktrackingSolver().solve(self.currentEnvironment.getBoard(), 0)

    def solveSimulatedAnnealing(self, temp):
        return SimulatedAnnealing().solve(self.currentEnvironment.getBoard(), temp)


if __name__ == "__main__":
    print("Enter desired board difficulty [\"Easy\", \"Med\",\"Hard\",\"Evil\"]:")
    difficulty = input()
    print("Enter board number [1-5]:")
    boardNumber = input()
    a = Agent()
    a.initializeEnvironment(difficulty, boardNumber)
    # print(a.solveWithBacktracking())
    sum = 0
    run = 100
    for step in range(2000, 20000, 1000):
        for i in range(run):
            sum += a.solveSimulatedAnnealing(step)[2]
        print("Initial Temp: " + str(step) + "Average: " + str(sum/run))
        sum = 0
