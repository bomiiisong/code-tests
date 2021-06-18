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