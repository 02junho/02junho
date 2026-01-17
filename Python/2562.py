# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어지고
# 출력되는 첫 줄에 최댓값과 둘째 줄에 몇 번째에 있는지 출력하는 문제

numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1  # 1-based index

print(max_value)
print(max_index)