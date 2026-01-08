## 두 정수의 합을 출력하고 마지막엔 0 0 입력받으면 종료하는 문제

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)