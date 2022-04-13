n = 5
ma = [[None] * n for j in range(n)]
dx, dy = 0, 1
x, y = 0, 0
for i in range(1, n**2+1):
    ma[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and ma[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = dy, -dx
        x, y = x + dx, y + dy
for i in ma:
    print(*i)


rows, columns = 8, 1
matrix = [[None for _ in range(columns)] for _ in range(rows)]


def print_matrix(rows, columns, matrix):
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).rjust(3), end=" ")
        print()


number, row, column = 1, 0, 0
direction = "hs"
while number != columns * rows + 1:
    if matrix[row][column] is None:
        matrix[row][column] = number
        number += 1
    if len(matrix[row]) == 1:
        row += 1
        continue
    if (column == columns - 1 or matrix[row][column + 1] is not None) and matrix[row][column - 1] == number - 2 and column:
        direction = "vs"
    elif (row == rows - 1 or matrix[row + 1][column] is not None) and matrix[row - 1][column] == number - 2:
        direction = "hr"
    elif (column == 0 or matrix[row][column - 1] is not None) and matrix[row][column + 1] == number - 2:
        direction = "vr"
    elif row != rows - 1 and matrix[row - 1][column] is not None and matrix[row + 1][column] == number - 2:
        direction = "hs"
    if direction == "hs":
        column += 1
        continue
    elif direction == "vs":
        row += 1
        continue
    elif direction == "hr":
        column -= 1
        continue
    elif direction == "vr":
        row -= 1


print_matrix(rows, columns, matrix)