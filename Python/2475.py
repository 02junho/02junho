# 검증수 문제 (5자리 숫자에서 각 숫자를 제곱한 후 더한 다음 10으로 나눈 나머지 출력)
# 각 숫자 사이에 빈칸이 있음

numbers = list(map(int, input().split()))
result = sum([num ** 2 for num in numbers]) % 10
print(result)