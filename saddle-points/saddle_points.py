def saddle_points(matrix):
    if not matrix:
        return set()
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError('That is not a matrix!')
    row_len = len(matrix[0])
    col_len = len(matrix)

    return [{'row': k+1, 'column': i+1} for k in range(col_len) for i in range(row_len)
            if max(matrix[k]) <= matrix[k][i] <= min([row[i] for row in matrix])]

