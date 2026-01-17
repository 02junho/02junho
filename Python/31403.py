# A,B,C를 각각 수와 문자열로 생각했을 때 A+B-C의 두 결과를 출력하는 문제
# 한 줄에 하나씩 입력

A = input()
B = input()
C = input()

# 1. 수로 계산 (정수로 변환 후 계산)
print(int(A) + int(B) - int(C))

# 2. 문자열로 계산 (A와 B를 이어 붙인 후 정수로 변환하여 C를 뺌)
combined_AB = A + B
print(int(combined_AB) - int(C))