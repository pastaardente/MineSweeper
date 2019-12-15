class Cell:
    def __init__(self):
        self.__adjCount = 0
        self.__isMined = False
        self.__isMarked = False
        self.__isCovered = True

    @property
    def adjCount(self):
        return self.__adjCount
    
    @__adjCount.setter
    def adjCount(self, adjCount):
        self.__adjCount = adjCount

    @property
    def isMined(self):
        return self.__isMined
    
    @__isMined.setter
    def isMined(self, isMined):
        self.__isMined = True
        
   @property 
    def isMarked(self):
        return self.__isMarked
    
    def togglemark(self):
        if not self.__isCovered:
            return False
        self.__isMarked = not self.__isMarked
        return True
    
   @property
    def isCovered(self):
        return self.__isCovered

    def uncover(self):
        if self.__isMarked or not self.__isCovered:
            return False
        self.__isCovered = false
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
            return self.__adjCount
