from collections import deque

n, m = map(int, input().split())
maze = [[int(i) for i in input()] for _ in range(n)]
print(maze)

X, Y = 0, 0

# 상, 하, 좌, 우 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((X,Y)) 

while queue:
    X, Y = queue.popleft()

    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == 0:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[X][Y] + 1
            queue.append((nx, ny))

print(maze[n-1][m-1])



