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