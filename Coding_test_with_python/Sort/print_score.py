n = int(input())
student = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    student.append([name, score])

sort_stu = sorted(student, key=lambda student:student[1])

for s in sort_stu:
    print(s[0], end=' ')