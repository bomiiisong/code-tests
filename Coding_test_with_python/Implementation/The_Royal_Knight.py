knight = input()
X = knight[0]
Y = int(knight[1])

X_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

garden = [[0 for _ in range(8)] for _ in range(8)]
count = 0

X_idx = X_list.index(X) + 1

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

for i in range(8):
    nx = X_idx + dx[i]
    ny = Y + dy[i]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1
    else:
        continue

print(count)
