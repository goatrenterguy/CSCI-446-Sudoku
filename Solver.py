import Agent


class Solver:

    def __init__(self, agent:Agent, sensor: Agent.Sensor, actuator: Agent.Actuator ):
        self.sensor = sensor
        self.actuator = actuator
        self.agent = agent

    def solve(self):
        pass
