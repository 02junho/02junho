# 별 찍기 문제 (오른쪽 정렬)

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)