# 행렬 덧셈 문제 (N*M이 주어질 때, 두 행렬 A와 B의 합을 구하는 프로그램 작성)

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

result = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

for row in result:
    print(' '.join(map(str, row)))