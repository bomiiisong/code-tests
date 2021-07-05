s = input()
number = int(s[0])

for i in range(1, len(s)):
    temp = int(s[i])
    if number < 2 or temp < 2:
        number += temp
    else:
        number *= temp

print(number)