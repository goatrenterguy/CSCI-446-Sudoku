class Environment:

    def __init__(self, difficulty: str, boardNumber: int):
        self.__board = self.loadBoard(difficulty, boardNumber)  # Initialize board

    #   :param difficulty: String of difficulty of the board to load
    #   :param boardNumber: Int of the number of the board to load
    #   Reads in and loads the board
    @staticmethod
    def loadBoard(difficulty: str, boardNumber: int):
        board = []
        try:
            file = open("Puzzles/" + str(difficulty) + "-P" + str(boardNumber) + '.csv', "r")
        except FileNotFoundError:
            print("File failed to load, check input. Loading default board...")
            file = open("Puzzles/Easy-P1.csv", "r")
        #   Read file in line by line
        for line in file:
            board.append([int(numbers) for numbers in line.strip("\n").strip("\ufeff0").replace("?", "0").split(",")])
        file.close()
        return board

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
