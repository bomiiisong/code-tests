n = int(input())
x = list(map(int, input().split()))

x.sort()  ## 인원이 많은 그룹부터 생성 시 최댓값 불가
group = 0
member = 0

for i in x:
    member += 1
    if member >= i:
        group += 1
        member = 0

print(group)