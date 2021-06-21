import time

n, m = map(int, input().split())
card = []
for _ in range(n):
    card.append(list(map(int, input().split())))

min_num = [min(raw) for raw in card]
max_value = max(min_num)
print(max_value)