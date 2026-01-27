# 첫째 줄부터 열번째 줄까지 숫자가 한 줄에 하나씩 주어지고 42로 나눈 나머지를 구하고
# 서로 다른 나머지의 갯수를 출력하는 문제

remainders = set()
for _ in range(10):
    number = int(input())
    remainders.add(number % 42)
print(len(remainders))