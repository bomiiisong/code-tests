n = int(input())
map = [[0 for _ in range(n)] for _ in range(n)]
direction = list(input().split())

X, Y = 1, 1

for i in direction:
    if i == 'R' and Y < n :
        Y += 1
        # print(X, Y)
    
    elif i == 'L' and Y > 1 :
        Y -= 1

    elif i == 'U' and X > 1 :
        X -= 1

    elif i == 'D' and X < n :
        X += 1

print(X, Y)
