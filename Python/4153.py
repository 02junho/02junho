# 직각삼각형 구하는 문제
# 세 변의 길이가 주어지고 직각삼각형을 이루는지 판단, 세 변의 길이가 모두 0이면 종료
# 맞으면 'right' 틀리면 'wrong' 출력

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('right')
    else:
        print('wrong')