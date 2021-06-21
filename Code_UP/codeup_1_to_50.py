## 23. 시:분:초 를 입력받을 때, '분'만 출력하기
time = input().split(':')
print(time[1])

##24. 2개의 단어를 입력받아 공백덦이 출력하기
word1, word2 = input().split()
print(word1 + word2)

## 25. 2개의 정소를 입력받아 합 출력하기
# (1)
num1, num2 = input().split()  ## 왜 return type이 int??
print(int(num1) + int(num2))

#(2)
num1, num2 = [int(v) for v in input().split()]
print(num1 + num2)

## 26. 2개의 실수를 입력받아 합 출력하기
f1, f2 = [float(v) for v in input().split()]
print(f1 + f2)

## 27. 10진수를 16진수로 출력하기
num = int(input())
print('%x' % num)

## 28. 10진수를 16진수 대문자로 출력하기
num = int(input())
print('%X' % num)

## 29. 8진수로 출력하기
num = int(input(), 16)
print('%o' % num)

## 30. 10진수 유니코드 출력
code = ord(input())
print(code)

## 31. 10진수 정수를 유니코드로 변환하기
code = int(input())
print(chr(code))

## 32. 부호 바꿔 출력하기
num = int(input())
print(-num)

## 33. 문자 입력받아 다음 문자 출력하기
word = ord(input())  # 문자를 아스키코드 숫자로 변환
print(chr(word+1))   # 다음 문자의 유니코드로 바꾼 후 문자로 변환

## 34. 2개의 정수값 입력받아 뺄셈
n1, n2 = input().split()
print(int(n1) - int(n2))

## 35. 입력받은 실수 곱 출력하기
f1, f2 = input().split()
print(float(f1) * float(f2))

## 36. 단어, 반복횟수 입력받아 반복횟수만큼 단어 반복 출력
w, n = input().split()
print(w * int(n))

## 37. 36번과 동일

## 38. 정수, 횟수 입력받아 정수에 횟수만큼 거듭제곱 
a, b = input().split()
print(int(a)**int(b))

## 39. 실수 거듭제곱
f1, f2 = input().split()
print(float(f1) ** float(f2))

## 40. 몫 구하기
a, b = input().split()
print(int(a)//int(b))

## 41. 나머지 구하기
a, b = input().split()
print(int(a) % int(b))

## 42. 실숫값 반올림하기
f = float(input())
print(format(f, '.2f'))  # format 함수 사용

## 43. 실수를 나눈 결과를 셋째자리까지 출력
f1, f2 = input().split()
result = float(f1) / float(f2)
print(format(result, '.3f'))

## 44. 합, 차, 곱, 몫, 나머지, 나누기 출력
a, b = input().split()

total = int(a) + int(b)
minus = int(a) - int(b)
multiple = int(a) * int(b)
quotient = int(a) // int(b)
remainder = int(a) % int(b)
divide = int(a) / int(b)

print(total)
print(minus)
print(multiple)
print(quotient)
print(remainder)
print(format(divide, '.2f'))  # 소숫점 둘쨋자리까지 출력

## 45. 합과 평균 출력
n1, n2, n3 = input().split()
total = (int(n1) + int(n2) + int(n3))  # sum 허용인됨
avg = total / 3
print(total, format(avg, '.2f'))

# 시도해보고싶은 방법
nums = [int(v) for v in input().split()]
total = sum(nums[0], nums[1], nums[2]) 
avg = total / len(nums)
print(total, avg)

## 46. 비트단위 시프트 연산자 사용
num = int(input())
print(num<<1)

## 47. 비트단위연산자
# a<<b => a * 2**b 값으로 연산됨
a, b = map(int, input().split())
print(a<<b)

## 48. 정수값 비교하기
a, b = map(int, input().split())

if a < b :
    print(True)
    
else:
    print(False)

## 49. 비교/관계 연산자 사용하기
a, b = map(int, input().split())

if a == b :
    print(True)
else : 
    print(False)

## 50. 값 비교하기
a, b = map(int, input().split())

if b >= a :
    print(True)
elif b != a :
    print(False)