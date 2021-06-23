n = int(input())
numbers = [int(input()) for _ in range(n)]

up_down = sorted(numbers, reverse=True)

for i in up_down:
    print(i, end=' ')