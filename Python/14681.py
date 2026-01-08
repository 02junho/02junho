## 사분면 고르기 문제

x = map(int, input().split())
y = map(int, input().split())
x, y = list(x)[0], list(y)[0]

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

## 다르게 푸는 방법

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)