class Matrix:
    # def __init__(self, matrix_string):
    #     self._rows = matrix_string.split("\n")

    # def row(self, index):
    #     row[0] = self._rows[index -1].replace(' ',", ")
    #     return row

    # def column(self, index):
    #     column =""
    #     # print (self._rows[1])
    #     for row in self._rows:
            
    #         column += str(row[index]) + ", "
    #         # print(row[1] + " ")
    #         # print (column)
    #     return column[:-2]

    def __init__(self, m_string):
        self.matrix = [[int(i) for i in e.split()] for e in m_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [r[index - 1] for r in self.matrix]



if __name__ == "__main__":

    matrix = Matrix("1 2 3\n2 5 6\n7 8 9\n8 7 6")
    # 
    print(matrix.row(2))
    # print(matrix.column(1))
    # print(matrix.column(4))
    # print(matrix.column(3))
    