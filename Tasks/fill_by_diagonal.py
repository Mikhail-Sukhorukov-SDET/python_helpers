rows, columns = 8, 1
matrix = [[None for _ in range(columns)] for _ in range(rows)]


def print_matrix(rows, columns, matrix):
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).rjust(5), end=" ")
        print()


number, row, column = 1, 0, 0
while matrix[rows - 1][columns - 1] is None:
    if matrix[row][column] is None:
        matrix[row][column] = number
        number += 1
    if column != 0 and row != rows - 1:
        row += 1
        column -= 1
        continue
    if None in matrix[row] or len(matrix[row]) == 1:
        not_empty_index = 0
        for m_row in matrix:
            if None in m_row:
                not_empty_index = matrix.index(m_row)
                break
        if None in matrix[not_empty_index]:
            column = matrix[not_empty_index].index(None)
        row = not_empty_index
        continue

print_matrix(rows, columns, matrix)