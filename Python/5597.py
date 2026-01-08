# 과제를 냈는지 확인하는 문제(28명이 제출하고 2명이 미제출)

students = set(range(1, 31))
for _ in range(28):
    submitted = int(input())
    students.discard(submitted)

for student in sorted(students):
    print(student)