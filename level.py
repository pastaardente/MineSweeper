import random
import cell

class Level:
    def __init__(self, width, height, mineCount):
        # create board of size width * height
        self.__board = [ [cell.Cell()] * height ] * width
        self.__width = width
        self.__height = height
        self.__mineCount = mineCount

        for c in self.__board:
            c = cell.Cell()

        # populate board with mines
        while mineCount > 0:
            x = random.randrange(self.__width)
            y = random.randrange(self.__height)
            self.__board[x][y].setMine()
            mineCount -= 1

        # calculate mine counts
        for x in range(0, width):
            for y in range(0, height):
                if self.__board[x][y].isMined():
                    self.__board[x][y].setCount(self.__getAdjMineCount(x, y))
                else:
                    self.__board[x][y].setCount(-1)

    def mark(self, x, y):
        if self.boundsCheck(x, y):
            self.__board[x][y].togglemark()
            return self.__board[x][y].isMarked()

    def reveal(self, x, y):
        if self.boundsCheck(x, y):
            if self.__board[x][y].uncover():
                return self.__board[x][y].isMined()
        return False

    def __autoReveal(self, x, y):
        # out of bounds base case
        if self.boundsCheck(x, y) is False:
            return
        wasRevealed = self.__board[x][y].uncover()
        count = self.__board[x][y].adjCount()

        # numbered or marked cell base case
        if count != 0 and wasRevealed is False:
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
                output += str(self.__board[x][y]) + " "
            output += "| " + str(x) + '\n'

        output += "\t   "
        for x in range(0, self.__width):
            output += str(x) + ' '

        markCount = 0
        for line in self.__board:
            for cell in line:
                if cell.isMarked(): markCount += 1

        output += "\n\tStatus: " + str(markCount) + '/' + str(self.__mineCount)
        return output


    def uncoverAll(self):
        for line in self.__board:
            for cell in line:
                cell.uncover()

    def allMinesMarked(self):
        for line in self.__board:
            for cell in line:
                if (cell.isMined() and (cell.isMarked() is False)):
                    return False
        return True

    def allUnminedRevealed(self):
        for line in self.__board:
            for cell in line:
                if ((cell.isMined() is False) and (cell.isCovered() is False)):
                    return False
        return True

    def boundsCheck(self, x, y):
        return x >= 0 and y >= 0 and x < self.__width and y < self.__height

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
        return self.__board[x][y]
