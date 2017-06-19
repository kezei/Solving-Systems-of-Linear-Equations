import sys

def numberOfElements(n):
    list = []
    for i in range(0, n-1):
        list.append(0)
    return list

class Matrix():
    // m rows
    // n columns
    def __init__(self, m, n):
        self.rows = m
        self.columns = n
        self.matrix = [self.rows * numberOfElements(self.columns)]

    def editRow(self.matrix, row, newRow):
        if len(newRow) != self.columns:
            return("Your new row's length is not the same as the length of the other rows")
        self.matrix[row-1] = newRow
        return ()

def reducedRowEchelonForm(variableMatrix, resultMatrix):
    if resultMatrix.columns!=1:
        return("The number of rows the matrix representing the results of the original expressions has is bigger than 1")
    if variableMatrix.rows!=resultMatrix.rows:
        return("The number of rows of the matrices is not the same")
    mutatedVariableMatrix=variableMatrix
    mutatedResultVariable=resultMatrix
