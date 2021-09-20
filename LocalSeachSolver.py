import copy
import math
import random
import numpy
from random import choice


class SimulatedAnnealing:
    def __init__(self):
        self.initialBoard = None

    def solve(self, board, temp, beta):
        self.initialBoard = copy.deepcopy(board)
        board = self.generateRandomNumInBlocks(board)
        updates = 1
        T = self.annealingSchedule(temp, beta, updates)
        while T > .01:
            nextBoard = self.nextState(copy.deepcopy(board))
            costDelta = self.costFunction(board) - self.costFunction(nextBoard)
            if costDelta > 0:
                board = nextBoard
                if self.costFunction(board) == 0:
                    return board, self.costFunction(board), updates
            elif random.random() < math.exp(costDelta / T):
                board = nextBoard
            print("Cost Delta: " + str(costDelta) + " Probability: " + str(math.exp(costDelta / T)) + " Temp: " + str(
                "Temp: " + str(T)))
            updates += 1
            T = self.annealingSchedule(temp, beta, updates)
        return board, self.costFunction(board), updates

    #   Swap two of the cells in each box
    def nextState(self, board):
        one = choice(range(9))
        two = choice(range(9))
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                initialBlock = self.getNumbersInBlock(row, col, self.initialBoard)
                while one == two or self.initialBoard[initialBlock[one][0]][initialBlock[one][1]] != 0 or \
                        self.initialBoard[initialBlock[two][0]][initialBlock[two][1]] != 0:
                    one = choice(range(9))
                    two = choice(range(9))
                # Swap swap
                board[initialBlock[one][0]][initialBlock[one][1]], board[initialBlock[two][0]][initialBlock[two][1]] = \
                board[initialBlock[two][0]][initialBlock[two][1]], board[initialBlock[one][0]][initialBlock[one][1]]
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

    def printBoard(self, board):
        for y in board:
            print(y)


class GeneticAlgorithm:
    def __init__(self):
        self.initialBoard = None

    def solve(self, puzzle, popSize):
        # Set up population
        self.initialBoard = copy.deepcopy(puzzle)
        population = self.initPopulation(popSize)
        popRank = numpy.array(self.rankPopulation(population))

        while True:
            # Tournament selection with two tournaments each using half the population
            #group1 = population[:len(population) // 2]
            #group2 = population[len(population) // 2:]
            #parent1 = group1[0]
            #p1fitness = self.fitness(parent1)
            #parent2 = group2[0]
            #p2fitness = self.fitness(parent2)
            #for individual in group1:
            #    if p1fitness > self.fitness(individual):
            #        parent1 = individual
            #        p1fitness = self.fitness(parent1)
            #for individual in group2:
            #    if p2fitness > self.fitness(individual):
            #        parent2 = individual
            #        p2fitness = self.fitness(parent2)

            # Rank Order Selection
            weights = [0.5, 0.25, 0.13, 0.06, 0.03, 0.015, 0.008, 0.004, 0.002, 0.001]
            firstChoice = popRank[numpy.random.choice(range(10), 1, p=weights)]
            p1fitness = firstChoice[0][0]
            parent1 = firstChoice[0][1]
            secondChoice = popRank[numpy.random.choice(range(10), 1, p=weights)]
            p2fitness = secondChoice[0][0]
            parent2 = secondChoice[0][1]
            print("P1 fitness: " + str(p1fitness))

            # Return if either parent is the correct solution
            if self.fitness(parent1) == 0:
                return parent1
            if self.fitness(parent2) == 0:
                return parent2

            # Convert parents into chromosomes and create the new population with crossovers
            chrom1 = self.toChromosome(parent1)
            chrom2 = self.toChromosome(parent2)
            #for i in range(popSize // 2):
            # Combine the two parents
            chrom1v2, chrom2v2 = self.crossover(chrom1, chrom2)
            # Mutate probabilistically based on the fitness of the parent
            if 1 / choice(range(1, p1fitness)) < 1 / 10:
                chrom1v2 = self.mutate(chrom1v2)
            if 1 / choice(range(1, p2fitness)) < 1 / 10:
                chrom2v2 = self.mutate(chrom2v2)
            print(popRank[9][1])
            population.remove(popRank[9][1])
            population.remove(popRank[8][1])
            population.append(self.toSolution(chrom1v2))
            population.append(self.toSolution(chrom2v2))
            popRank = numpy.array(self.rankPopulation(population))


    def initPopulation(self, popSize):
        population = []
        for i in range(popSize):
            individual = copy.deepcopy(self.initialBoard)
            population.append(self.generateRandomNumInBlocks(individual))
        return population

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

    def getNumbersInBlock(self, row, col, board):
        blocks = [[] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                blocks[((y // 3) * 3) + (x // 3)].append((y, x))
        block = blocks[((row // 3) * 3) + (col // 3)]
        return block

    def fitness(self, board):
        cost = 0
        for y in range(9):
            for x in range(9):
                # remove value so it doesn't get counted as a conflict
                n = board[y][x]
                board[y][x] = 0
                # check row
                for k in range(9):
                    if board[y][k] == n:
                        cost += 1
                # check column
                for k in range(9):
                    if board[k][x] == n:
                        cost += 1
                # check cell
                cornerX = (x // 3) * 3
                cornerY = (y // 3) * 3
                for i in range(3):
                    for j in range(3):
                        if board[cornerY + i][cornerX + j] == n:
                            cost += 1
                # replace value
                board[y][x] = n
        return cost

    def toChromosome(self, solution):
        chromosome = []
        for y in range(9):
            for x in range(9):
                if self.initialBoard[y][x] == 0:
                    chromosome.append(solution[y][x])
        return chromosome

    def toSolution(self, chromosome):
        solution = copy.deepcopy(self.initialBoard)
        pointer = 0
        for y in range(9):
            for x in range(9):
                if solution[y][x] == 0:
                    solution[y][x] = chromosome[pointer]
                    pointer += 1
        return solution

    def crossover(self, chro1, chro2):
        crossoverPoint = choice(range(len(chro1)))
        chro1v2 = [None] * len(chro1)
        chro2v2 = [None] * len(chro2)
        for i in range(crossoverPoint):
            chro1v2[i] = chro1[i]
            chro2v2[i] = chro2[i]
        for i in range(crossoverPoint, len(chro1)):
            chro1v2[i] = chro2[i]
            chro2v2[i] = chro1[i]
        return chro1v2, chro2v2

    def mutate(self, chrom):
        for i in range(len(chrom)):
            if choice(range(100)) == 0:
                chrom[i] = choice(range(1, 10))
                print("MUTATE")
        return chrom

    def rankPopulation(self, pop):
        popRank = []
        for individual in pop:
            popRank.append([self.fitness(individual),individual])
        popRank.sort(key=lambda y: y[0])
        return popRank