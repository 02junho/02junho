# OX 횟수 계산 문제
# O의 연속된 개수에 따라 점수를 계산한다
# OOOXOOXXOOO -> 1+2+3 + 1 + 1+2+3 = 13
# 첫째 줄은 테스트 갯수

n = int(input())
for _ in range(n):
    line = input().strip()
    score = 0
    consecutive = 0
    for char in line:
        if char == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    print(score)