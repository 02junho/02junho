# X보다 작은 수 출력하는 문제 (첫 줄에 수의 개수 N과 기준 X가 주어짐)

n, x = map(int, input().split())
numbers = list(map(int, input().split()))

for num in numbers:
    if num < x:
        print(num, end=' ')