


class BacktrackingSolver:
    
    def __init__(self, agent:Agent):
        self.sensor = agent.Sensor
        self.actuator = agent.Actuator
        self.agent = agent

    def solve(self):
        self.agent.logicStep++
        self.agent.currentEnvironment = self.Solver.sensor.getState()
        for x in range(8):
            for y in range(8):
                if self.agent.currentEnvironment[x][y] == 0:
                    for testInput in range(1,9):
                        if possible(x, y, testInput):
                            self.agent.currentEnvironment[x][y] = testInput
                            solve()
                            self.agent.currentEnvironment[x][y] = 0
                    return

    def possible(self, x, y, n):
        # check row
        for k in range(8):
            if self.agent.currentEnvironment[x][k] == testInput:
                return false

        # check column
        for k in range(8):
            if self.agent.currentEnvironment[k][y] == testInput:
                return false

        # check cell
        cornerX = (x // 3) * 3
        cornerY = (y // 3) * 3
        for i in range(2):
            for j in range(2):
                if self.agent.currentEnvironment[cornerX + i][cornerY + j] == testInput:
                    return false

        return true