# 숫자의 합 출력 (공백 없이 숫자의 갯수 입력 후 숫자의 합 출력)

n = int(input())
numbers = input()
result = sum(int(numbers[i]) for i in range(n))
print(result)