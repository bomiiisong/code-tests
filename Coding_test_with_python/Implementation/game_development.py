N, M = map(int, input().split())
X, Y, d = map(int, input().split())
# direction = [0, 3, 2, 1]
game_map = []
visit_time = 0
count = 1

for _ in range(M) :
    game_map.append(list(map(int, input().split())))

game_map[X][Y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if visit_time == 4:
        nx = X - dx[d]
        ny = Y - dy[d]
        if game_map[nx][ny] == 1:
            break
        else:
            X = nx
            Y = ny
            visit_time = 0
    else:
        if d == 0:
            d = 3
            visit_time += 1
        else:
            d -= 1
            visit_time += 1
            
        nx = X + dx[d]
        ny = Y + dy[d]

        if game_map[nx][ny] == 0:
            X = nx
            Y = ny
            visit_time = 0
            count += 1
            game_map[nx][ny] = 2
            
        else:
            continue

print(count)
    
