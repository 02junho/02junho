# 문자열 S를 입력 받고, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 문제
# 첫 줄엔 테스트 케이스 T

T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for char in S:
        P += char * R
    print(P)