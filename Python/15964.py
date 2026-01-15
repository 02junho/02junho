# 이상한 기호 함수 풀이 문제 (A@B = (A + B) * (A - B)) 조건: A, B ≤ 1,000

A, B = map(int, input().split())
A,B = int(A), int(B)
int(A), int(B) <= 1000
result = (A + B) * (A - B)
print(result)