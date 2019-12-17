class Cell:
    def __init__(self):
        self.__adjCount = 0
        self.__isMined = False
        self.__isMarked = False
        self.__isCovered = True

    def adjCount(self):
        return self.__adjCount
    
    def setCount(self, adjCount):
        self.__adjCount = adjCount

    def isMined(self):
        return self.__isMined
    
    def setMine(self):
        self.__isMined = True
        
   
    def isMarked(self):
        return self.__isMarked
    
    def togglemark(self):
        if self.__isCovered:
            self.__isMarked = not self.__isMarked
            return True
        else:
            return False
    
   
    def isCovered(self):
        return self.__isCovered

    def uncover(self):
        if self.__isMarked or not self.__isCovered:
            return False
        self.__isCovered = False
        return True
    
    # toString override 
    def __str__(self):
        if self.__isMarked:
            return "X"
        elif self.__isCovered:
            return "?"
        elif self.__isMined:
            return "*"
        elif self.__adjCount == 0:
            return "_"
        else:
            return str(self.__adjCount)
