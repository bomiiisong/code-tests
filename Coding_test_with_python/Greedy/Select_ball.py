n, m = map(int, input().split())
k = list(map(int, input().split()))

cases = 0

for i in range(n):
    for j in range(i+1, n):
        if k[i] == k[j]:
            continue
        else:
            cases += 1

print(cases)