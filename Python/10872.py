## 팩토리얼 출력하는 문제

n = int(input())

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(n))