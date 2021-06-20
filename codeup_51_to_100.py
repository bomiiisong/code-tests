## 51. 입력값 비교하기
a, b = map(int, input().split())
if a != b:
    print(True)
else: 
    print(False)

## 52. 입력값 True/False 로 반환하기
value = int(input())
print(bool(value))

## 53. 입력값의 bool 값을 반대로 출력하기
value = bool(int(input()))
print(not value)

## 54. 2개 정수의 bool 값이 모두 True 일 때에만 True 반환
v1, v2 = map(int, input().split())
print(bool(v1) and bool(v2))  # And 연산은 두 값이 True일 때만 True 반환

## 55. 2개 정수의 bool 값 중 하나만 True여도 True 반환
v1, v2 = map(int, input().split())
print(bool(v1) or bool(v2))

## 56. bool 값이 다를 때에만 True 출력
v1, v2 = map(int, input().split())
v1 = bool(v1)
v2 = bool(v2)
print((v1 and (not v2)) or ((not v1) and v2))

## 57. bool 값이 같을 때에만 True 출력
v1, v2 = map(int, input().split())
v1 = bool(v1)
v2 = bool(v2)
print(((not v1) and (not v2)) or (v1 and v2))

## 58. bool 값이 모두 False 일 때에만 True 출력
v1, v2 = map(int, input().split())
v1 = bool(v1)
v2 = bool(v2)
print(not(v1 or v2))

## 59. 비트단위로 NOT 연산 출력하기
value = int(input())
print(~value)  # ~ : tilde

## 60. 비트단위 AND 연산 출력하기
v1, v2 = map(int, input().split())
result = v1 & v2
print(result)

## 61. 비트단위 OR 연산 출력하기
v1, v2 = map(int, input().split())
result = v1 | v2
print(result)

## 62. 비트단위 XOR 연산 출력하기
v1, v2 = map(int, input().split())
result = v1^v2
print(result)

## 63. 입력값 중 큰 값 출력
v1, v2 = map(int, input().split())

if v1 >= v2 :
    print(v1)
else:
    print(v2)

## 64. 세 입력값 중 가장 작은 값 출력
v1, v2, v3 = map(int, input().split())
result = (v1 if v1 < v2 else v2) if ((v1 if v1 < v2 else v2) < v3) else v3
print(result)

## 65. 정수 3개 입력받아 짝수만 출력
v1, v2, v3 = map(int, input().split())

if v1 % 2 == 0:
    print(v1)
if v2 % 2 == 0:
    print(v2)
if v3 % 2 == 0:
    print(v3)

## 66. 정수 3개 입력받아 짝/홀 출력
v1, v2, v3 = map(int, input().split())

if v1 % 2 == 0:
    print('even')
else :
    print('odd')
    
if v2 % 2 == 0:
    print('even')
else :
    print('odd')
    
if v3 % 2 == 0:
    print('even')
else :
    print('odd')

## 67. 정수 1개 입력받아 음/양, 짝/홀 분류
value = int(input())

if value < 0:
    if value % 2 == 0:
        print("A")
    else:
        print("B")
else :
    if value % 2 == 0:
        print("C")
    else:
        print("D")

## 68. 점수별 등급 출력
score = int(input())

if score >= 90 :
    print("A")
else:
    if score >= 70 :
        print("B")
    else:
        if score >= 40 :
            print("C")
        else:
            print("D")

## 69. 입력값 조건별 출력
score = input()
if score == 'A' :
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run')
elif score == 'D':
    print('slowly~')
else:
    print('what?')

## 70. 입력값에 따른 계절 출력
month = int(input())

if month // 3 == 1:
    print('spring')
elif month // 3 == 2:
    print('summer')
elif month // 3 == 3:
    print('fall')
else:
    print('winter')

## 71. while 조건문 
value = 1

while value != 0:
    value = int(input())
    if value != 0 :
        print(value)
    else:
        break

## 72. 카운트다운 구현
value = int(input())

while value != 0 :
    print(value)
    value -= 1

## 73. 카운트다운 구현 2
value = int(input())

while value != 0 :
    value -= 1
    print(value)
    
## 74. 입력한 알파벳까지 출력
word = ord(input())
base_word = ord('a')

while base_word <= word :
    print(chr(base_word), end=' ')
    base_word += 1

## 75. 0부터 입력값까지 출력 (for문)
value = int(input())

for i in range(value+1):
    print(i)

## 76. 0부터 입력값까지 출력 (while 문)
value = int(input())
base = 0
while base <= value :
    print(base)
    base += 1

## 77. 짝수 합 구하기
number = int(input())
total = 0
for i in range(1, number+1):
    if i % 2 == 0:
        total += i 
print(total)        

## 78. 특정 종료 조건
while True :
    word = input()
    if word != 'q' :
        print(word)
    else:
        print(word)
        break

## 79. 1부터 값을 더해 입력한 수보다 합이 작으면 종료
value = int(input())
total = 0
n = 0

while True :
    n += 1
    total += n
    if total >= value :
        print(n)
        break

## 80. 입력받은 두 수의 모든 조합 출력
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

## 81. 16진수 구구단 출력
word = int(input(), 16)
for i in range(1, 16):
    print('%X*%X=%X' %(word, i, word*i))

## 82. 369 게임
number = int(input())

for i in range(1, number+1):
    if i % 10 == 3:
        print("X", end=' ')
    elif i % 10 == 6 :
        print("X", end=' ')
    elif i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')

## 83. 조합 수 구하기
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k, end=' ')
            print()
            count += 1
print(count)

## 84. 사운드파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
byte = (h * b * c * s) / 8
mb = (byte/1024)/1024
print(f'{mb:.1f} MB')

## 85. 이미지파일 저장용량 계산하기
w, h, b = map(int, input().split())
byte = (w * h * b) / 8
mb = (byte/1024) / 1024
print(f'{mb:.2f} MB')

## 86. 입력값보다 커질 때까지 더하기
subject = int(input())
number = 0
total = 0

while True : 
    total += number
    number += 1
    if total >= subject:
        break
    
print(total)

## 87. 3의 배수 출력하기
number = int(input())

for i in range(1, number+1):
    if i % 3 == 0 :
        continue
    else:
        print(i, end=' ')

## 88. 등차수열
a, d, n = map(int, input().split())
total = a

for i in range(0, n-1):
    total += d
print(total)

## 89. 등비수열
a, r, n = map(int, input().split())
total = a

for i in range(0, n-1):
    total += r
print(total)

## 90. 수열
a, m, d, n = map(int, input().split())
total = a

for _ in range(0, n-1):
    total = (total * m) + d
print(total)

## 91. 다시 만나는 날 계산
d1, d2, d3 = map(int, input().split())

start = 1

while start % d1 != 0 or start % d2 != 0 or start % d3 != 0 :
    start += 1

print(start)

## 92. 리스트 활용 (1)
total = int(input())
num = [int(i) for i in input().split()]

count = [0 for _ in range(24)]

for i in range(total):
    count[num[i]] += 1
    
for j in range(1, 24):
    print(count[j], end=' ')

## 93. 리스트 활용 (2)
count = int(input())
rand_num = [int(i) for i in input().split()]

for i in range(count-1, -1, -1):
    print(rand_num[i], end=' ')

## 94. 리스트에서 최솟값 찾기
count = int(input())
rand_num = [int(i) for i in input().split()]

print(min(rand_num))

## 95. 2중 리스트 활용
num = int(input())
game = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(num):
    x, y = map(int, input().split())
    game[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(game[i][j], end=' ')
    print()

## 96. 십자 뒤집기 게임
game = [[]*19 for _ in range(19)]
for i in range(19):
    game[i] = list(map(int, input().split()))
    
num = int(input())

for _ in range(num):
    x, y = map(int, input().split())
    
    for i in range(19):
        if game[x-1][i] == 1:
            game[x-1][i] = 0
        else:
            game[x-1][i] = 1
    
    for j in range(19):
        if game[j][y-1] == 1:
            game[j][y-1] = 0
        else:
            game[j][y-1] = 1 
            
for i in range(19):
    for j in range(19):
        print(game[i][j], end=' ')
    print()

## 97. 설탕과자 뽑기 게임
w, h = map(int, input().split())
num = int(input())

game = [[0 for _ in range(h)] for _ in range(w)]

for i in range(num):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            game[x-1][y-1] = 1
            y += 1
    else :
        for j in range(l):
            game[x-1][y-1] = 1
            x += 1
            
for i in range(w):
    for j in range(h):
        print(game[i][j], end=' ')
    print()

## 98. 성실한 개미
game = [[]*10 for _ in range(10)]
for i in range(10):
    game[i] = list(map(int, input().split()))
    
x, y = 1, 1
game[x][y] = 9

while True:
    if game[x][y] == 2:  # 가장 먼저 확인해야함 => 먹이 지날칠 수 있으므로
        game[x][y] = 9
        break
    
    elif game[x][y+1] != 1: # 다음 좌표 == 0 으로 하면 먹이(2)를 지나치므로 !=1로 조건 제시
        game[x][y] = 9
        y += 1
    
    else:
        if game[x+1][y] != 1:
            game[x][y] = 9
            x += 1
        else:
            game[x][y] = 9
            break

for i in range(10):
    for j in range(10):
        print(game[i][j], end=' ')
    print()