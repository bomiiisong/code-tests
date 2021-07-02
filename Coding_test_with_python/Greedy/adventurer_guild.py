n = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)
group = 0
total = len(x)

for i in x:
    if total < i:
        break
    else:
        total -= i
    group += 1

print(group)