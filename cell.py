class Cell:
    def __init__(self):
        self.adjCount = 0
        self.isMined = false
        self.isMarked = false
        self.isCovered = true

    def get_count(self):
        return self.adjCount
    def set_count(self, adjCount):
        self.adjCount = adjCount

    def get_mine(self):
        return self.isMined
    def set_mine(self, isMined):
        self.isMined = true

    def get_mark(self):
        return self.isMarked
    def toggle_mark(self):
        if not self.isCovered:
            return false
        self.isMarked = not self.isMarked
        return true

    def get_cover(self):
        return self.isCovered

    def uncover(self):
        if self.isMarked or not self.isCovered:
            return false
        self.isCovered = false
        return true

