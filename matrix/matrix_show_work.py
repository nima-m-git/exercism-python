class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [_.split(' ') for _ in matrix_string.splitlines()]
        self.row_l = len(self.matrix[0])
        self.col_l = len(self.matrix)

    def row(self, index):
        #return [1, 2]
        return [int(self.matrix[index-1][_]) for _ in range(self.row_l)]

    def column(self, index):
        return [int(self.matrix[_][index-1]) for _ in range(self.col_l)]








'''matrix string passed like :
matrix = Matrix("1 2\n3 4")

- str.splitlines() =
    ['1 2', '3 4']

-newlist = [i.replace(' ', ', ') for i in list] =
    ['1, 2', '3, 4']

want: [[1, 2],
       [3, 4]]

  
row 1 = 1,2      = st1_e1, st1_e2  row[i] = same string[i], dif element
row 2 = 3,4     = str2_e1, st2_e2
column 1 = 1,3   = st1_e1, st2_e1  column[i] = diff str, same element[i]
column 2 = 2, 4  = st1_e2, st1_e2


matrix = [_.split(' ') for _ in matrix_string.splitlines()] =
        ['1', '2']
        ['3', '4'] -matrix achieved!
        index - matrix[row][column]
        range 0 - len/-1
'''




