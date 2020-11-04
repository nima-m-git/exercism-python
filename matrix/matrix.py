class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [_.split(' ') for _ in matrix_string.splitlines()]
        self.row_l = len(self.matrix[0])
        self.col_l = len(self.matrix)

    def row(self, index):
        return [int(self.matrix[index-1][_]) for _ in range(self.row_l)]

    def column(self, index):
        return [int(self.matrix[_][index-1]) for _ in range(self.col_l)]



