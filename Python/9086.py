# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자 출력

T = int(input())
for _ in range(T):
    s = input()
    print(s[0] + s[-1])