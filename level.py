import cell

class Level:
    def __init__(self, width, height, mineCount):
        # create board of size width * height
        self.__board = [ [Cell] * height ] * width
        self.__width = width
        self.__height = height

        # populate board with mines
        # doesn't account for selecting a mined spot
        for mine in range(0, mineCount):
            x = random.randrange(width)
            y = random.randrange(height)
            self.__board[x][y].setMine()

        # calculate mine counts
        for x in range(0, width):
            for y in range(0, height):
                if self.__board[x][y].getMine():
                    self.__board[x][y].setCount(self.__getAdjMineCount(x, y))
                else:
                    self.__board[x][y].setCount(-1)

    def mark(self, x, y):
        return

    def reveal(self, x, y):
        return

    def __autoReveal(self, x, y):
        return

    def uncoverAll(self):
        return

    def allMinesMarked(self):
        return False

    def allUnminedRevealed(self):
        return False

    def boundsCheck(self, x, y):
        return True

    def getBoard(self):
        return __board, __length, __width

    def __getAdjMineCount(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                adj = self.__getAdjCell(x, y, i, j)
                if adj is not None and adj.getMine():
                    count++
        return count

    def __getAdjCell(self, x, y, i, j):
        x += i
        y += j
        if x < 0 or x >= self.__width or y < 0 or y >= self.height:
            return None
        return self.__board[x][y]
