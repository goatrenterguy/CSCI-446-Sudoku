from Environment import Environment
from BacktrackingSolver import BacktrackingSolver


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
        return BacktrackingSolver(self.currentEnvironment.getBoard()).solve()


if __name__ == "__main__":
    print("Enter desired board difficulty [\"Easy\", \"Med\",\"Hard\",\"Evil\"]:")
    difficulty = input()
    print("Enter board number [1-5]:")
    boardNumber = input()
    a = Agent()
    a.initializeEnvironment(difficulty, boardNumber)
    print(a.solveWithBacktracking())
