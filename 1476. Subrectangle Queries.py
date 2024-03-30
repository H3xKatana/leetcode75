#1476. Subrectangle Queries
class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle= rectangle
        pass
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rectangle[i][j]=newValue
        pass

    def getValue(self, row: int, col: int) -> int:
        return  self.rectangle[row][col]
        pass
    
