# 테스트 갯수 입력 후
# 빠른 A+B 출력하는 문제 (input 대신 sys.stdin.readline 사용)

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)