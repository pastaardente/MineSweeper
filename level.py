import random
import cell

class Level:
    # board is inverted
    def __init__(self, size, mineCount):
        self.__board = dict()
        self.__width = size
        self.__height = size
        self.__mineCount = mineCount

        for x in range(0, self.__width):
            for y in range(0, self.__height):
                self.__board.update({ (x, y) : cell.Cell() })

        # populate board with mines
        while mineCount > 0:
            x = random.randrange(self.__width)
            y = random.randrange(self.__height)
            self.__board[(x, y)].setMine()
            if (self.__board[(x, y)].isMined()):
                mineCount -= 1

        # calculate mine counts
        for x in range(0, self.__width):
            for y in range(0, self.__height):
                if not self.__board[(x, y)].isMined():
                    self.__board[(x, y)].setCount(self.__getAdjMineCount(x, y))
                else:
                    self.__board[(x, y)].setCount(-1)

    def mark(self, y, x):
        if self.boundsCheck(x, y):
            self.__board[(x, y)].togglemark()
            return self.__board[(x, y)].isMarked()

    def reveal(self, y, x):
        if self.boundsCheck(x, y):
            if not self.__board[(x, y)].isMarked():
                result = self.__board[(x, y)].isMined()
                self.__autoReveal(x, y)
                return result
        return False

    def __autoReveal(self, x, y):
        # out of bounds base case
        if self.boundsCheck(x, y) is False:
            return

        wasRevealed = self.__board[(x, y)].uncover()
        count = self.__board[(x, y)].adjCount()

        # numbered or marked cell base case
        if count != 0 or wasRevealed is False:
            return
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.__autoReveal(x + i, y + j)

    def __str__(self):
        output = "\t   "
        for x in range(0, self.__width):
            output += str(x) + ' '
        output += '\n'

        for x in range(0, self.__width):
            output += '\t' + str(x) + "| "
            for y in range(0, self.__height):
                output += str(self.__board[(x, y)]) + " "
            output += "| " + str(x) + '\n'

        output += "\t   "
        for x in range(0, self.__width):
            output += str(x) + ' '

        markCount = 0
        for _, cell in self.__board.items():
            if cell.isMarked(): markCount += 1

        output += "\n\tStatus: " + str(markCount) + '/' + str(self.__mineCount)
        return output


    def uncoverAll(self):
        for _, cell in self.__board.items():
            cell.uncover()

    def allMinesMarked(self):
        for _, cell in self.__board.items():
            if (cell.isMined() is not cell.isMarked()):
                return False
        return True

    def allUnminedRevealed(self):
        for _, cell in self.__board.items():
            if ((cell.isMined() is False) and (cell.isCovered())):
                return False
        return True

    def boundsCheck(self, x, y):
        return (x >= 0 and y >= 0 and x < self.__width and y < self.__height)

    def getBoard(self):
        return self.__board, self.__length, self.__width

    def __getAdjMineCount(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                adj = self.__getAdjCell(x, y, i, j)
                if adj is not None and adj.isMined():
                    count += 1
        return count

    def __getAdjCell(self, x, y, i, j):
        x += i
        y += j
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            return None
        return self.__board[(x, y)]
