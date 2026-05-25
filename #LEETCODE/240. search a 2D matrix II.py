#240
#search a 2D matrix II
def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols=len(matrix[0])
    i=0
    j=cols-1
    while i<rows and j>=0:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]<target:
            i+=1
        else:
            j-=1
    return False    
