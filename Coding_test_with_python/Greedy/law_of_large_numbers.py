N, M, K = map(int, input().split())
number = [int(v) for v in input().split()]
result = 0

number.sort()
first = number[N-1] # 가장 큰 수
second = number[N-2] # 두 번째로 큰 수

count = int(M / (K+1)) * K
count += M % (K+1)

result += (count) * first
result += (M - count) * second

print(result)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           