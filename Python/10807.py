# N개의 정수가 있을때, 정수 v가 몇 개인지 구하는 프로그램

N = int(input())
numbers = list(map(int, input().split()))

v = int(input())
count = numbers.count(v)
print(count)