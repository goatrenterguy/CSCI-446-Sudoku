from Environment import Environment
from BacktrackingSolver import BacktrackingSolver


class Sensor:
    @staticmethod
    def getState(environment: Environment):
        return environment.getBoard()


class Actuator:
    @staticmethod
    def setCell(coords: tuple, environment: Environment):
        environment.setCell(coords)


class Agent:
    def __init__(self):
        self.sensor = Sensor()
        self.actuator = Actuator()
        self.nextMove = []
        self.logicSteps = int
        self.archivedEnvironments = []
        self.currentEnvironment = None

    #   Check if the current environment is solved
    def isSolved(self):
        for y in self.sensor.getState(self.currentEnvironment):
            for x in y:
                if x == 0:
                    return False
        return True

    #   Method to initialize an environment, if there is a current board archive it
    def initializeEnvironment(self, difficultly, boardNumber):
        if self.currentEnvironment is not None:
            self.archivedEnvironments.append(self.currentEnvironment)
        self.currentEnvironment = Environment(difficultly, boardNumber)


class Main:
    agent = Agent()
    agent.initializeEnvironment("Easy", 1)
    solver = BacktrackingSolver(Solver(agent, agent.sensor, agent.actuator))

Main()
