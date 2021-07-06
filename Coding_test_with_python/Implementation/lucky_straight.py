n = input()
mid = (len(n) // 2) - 1
left = 0
right = 0

for i in range(mid+1):
    left += int(n[i])
for j in range(mid+1, len(n)):
    right += int(n[j])

if left == right:
    print('LUCKY')
else:
    print('READY')