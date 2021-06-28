n = int(input())
parts = list(map(int, input().split()))

m = int(input())
needs = list(map(int, input().split()))

for i in needs :
    if i in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')