import cell

class Level:
    def __init__(self, width, height, mineCount):
        # create board of size width * height
        self.__board = [ [Cell] * height ] * width
        self.__width = width
        self.__height = height

        # populate board with mines
        # doesn't account for selecting a mined spot
        while mineCount > 0:
            x = random.randrange(__width)
            y = random.randrange(__height)
            self.__board[x][y].setMine()

        for mine in range(0, mineCount):
            x = random.randrange(width)
            y = random.randrange(height)
            if self.__board[x][y].isMined() is False:
                self.__board[x][y].setMine()
                mineCount -= 1

        # calculate mine counts
        for x in range(0, width):
            for y in range(0, height):
                if self.__board[x][y].getMine():
                    self.__board[x][y].setCount(self.__getAdjMineCount(x, y))
                else:
                    self.__board[x][y].setCount(-1)

    def mark(self, x, y):
        if boundsCheck(x, y):
            __board[x][y].togglemark()

    def reveal(self, x, y):
        if boundsCheck(x, y):
            __board[x][y].uncover()

    def __autoReveal(self, x, y):
        # out of bounds base case
        if boundsCheck(x, y) is False:
            return
        wasRevealed = __board[x][y].uncover()
        count = __board[x][y].adjCount()

        # numbered or marked cell base case
        if count != 0 and wasRevealed is False:
            return
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                __autoReveal(x + i, y + j)


    def uncoverAll(self):
        for cell in __board:
            cell.uncover()

    def allMinesMarked(self):
        for cell in __board:
            if cell.isMined() and cell.isMarked() is False:
                return False
        return True

    def allUnminedRevealed(self):
        for cell in __board:
            if cell.isMined() is False and cell.isCovered() is False:
                return False
        return True

    def boundsCheck(self, x, y):
        return x >= 0 and y >= 0 and x < __width and y < __height

    def getBoard(self):
        return __board, __length, __width

    def __getAdjMineCount(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                adj = self.__getAdjCell(x, y, i, j)
                if adj is not None and adj.getMine():
                    count += 1
        return count

    def __getAdjCell(self, x, y, i, j):
        x += i
        y += j
        if x < 0 or x >= self.__width or y < 0 or y >= self.height:
            return None
        return self.__board[x][y]
