class Environment:

    def __init__(self):
        self.__board = []  # Initialize board
    #   :param difficulty: String of difficulty of the board to load
    #   :param boardNumber: Int of the number of the board to load
    #   Reads in and loads the board
    def loadBoard(self, difficulty: str, boardNumber: int):
        try:
            file = open("Puzzles/" + str(difficulty) + "-P" + str(boardNumber) + '.csv', "r")
        except FileNotFoundError:
            print("File failed to load, check input. Loading default board...")
            file = open("Puzzles/Easy-P1.csv", "r")
        #   Read file in line by line
        for line in file:
            self.__board.append(
                [int(numbers) for numbers in line.strip("\n").strip("\ufeff0").replace("?", "0").split(",")])
        file.close()

    #   Getter for the board
    def getBoard(self):
        return self.__board

    #   :param cords: A tuple where the values are y coordinate, x coordinate, and value to set respectively
    #   Set a single cell
    def setCell(self, coords: tuple):
        try:
            if self.__board[coords[0]][coords[1]] == 0:
                self.__board[coords[0]][coords[1]] = int(coords[2])
                return True
            else:
                print("Cannot set row: " + str(coords[0]) + "col: " + str(coords[1]) + "to: " + str(coords[2]))
                return False
        except TypeError:
            print("Check @coords types\nCoords: " + str(coords))
            return False
