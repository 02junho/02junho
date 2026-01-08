## 무한으로 정수의 합을 출력하지만 종료할 수 있는 문제

import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

    except EOFError:
        break
    except ValueError:
        break