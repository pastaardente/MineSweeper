import level

class Game:
    def __init(self):
        self.start()

    def start(self):
        size = m = 0

        while size <= 0:
            size = int(input("Board Size: "))
            if size <= 0: print("Please enter a number greater than 0")

        while m <= 0:
            m = int(input("Number of Mines: "))
            if m <= 0: print("Please enter a number greater than 0")

        self.__level = level.Level(size, m)
        self.show()
        self.instructions()

    def loop(self):
        command = input("> ")
        if (command == "show"):
            self.show()

        elif (command == "m"):
            x, y = self.getCoords()
            wasMarked = self.__level.mark(x, y)
            if (wasMarked):
                print("cell has been marked!")
            else:
                print("cell has been unmarked!")

        elif (command == "u"):
            x, y = self.getCoords()
            wasMined = self.__level.reveal(x, y)
            if (wasMined):
                self.gameOver()
                return False
            self.show()

        elif (command == "q"):
            return False

        else:
            self.invalidInput()


        if (self.__level.allMinesMarked() or self.__level.allUnminedRevealed()):
            self.gameWon()
            return False

        return True

    def getCoords(self):
        x = int(input("X: "))
        y = int(input("Y: "))

        while (self.__level.boundsCheck(x, y) is False):
            print("Coordinate is out of bounds")
            x = int(input("X: "))
            y = int(input("Y: "))
        return x, y


    def gameOver(self):
        self.__level.uncoverAll()
        self.show()
        print("Game Over!")

    def gameWon(self):
        self.__level.uncoverAll()
        self.show()
        print("You did it!")

    def prompt(self):
        print("> ")

    def instructions(self):
        print("show: show board")
        print("m x y: mark cell at (x, y)")
        print("u x y: uncover cell at (x, y)")
        print("q: quit")

    def invalidInput(self):
        print("Invalid Input")

    def show(self):
        print(str(self.__level))

