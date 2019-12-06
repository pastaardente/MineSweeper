class Cell:
    def __init__(self):
        self.adjCount = 0
        self.isMined = False
        self.isMarked = False
        self.isCovered = True

    def get_count(self):
        return self.adjCount
    def set_count(self, adjCount):
        self.adjCount = adjCount

    def get_mine(self):
        return self.isMined
    def set_mine(self, isMined):
        self.isMined = True

    def get_mark(self):
        return self.isMarked
    def toggle_mark(self):
        if not self.isCovered:
            return False
        self.isMarked = not self.isMarked
        return True

    def get_cover(self):
        return self.isCovered

    def uncover(self):
        if self.isMarked or not self.isCovered:
            return False
        self.isCovered = false
        return True

