s = list(input())
s.sort()
num = 0

for _ in range(len(s)):
    if s[0].isdigit():  ## isdigit() / isalpha() 기억하기
        num += int(s.pop(0))
    else:
        continue
s.append(str(num))
print(''.join(s))  ## join함수 기억하기