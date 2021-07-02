s = input()
number = int(s[0])

for i in range(1, len(s)):
    if number < 2 :
        number += int(s[i])
    else:
        number *= int(s[i])

print(number)