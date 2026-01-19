# 첫째 줄에 정수의 개수
# 둘째 줄에 정수들을 공백으로 구분하여 입력

N = int(input())
arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(min, max)