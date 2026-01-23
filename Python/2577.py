# 숫자의 개수 출력 문제
# 세 자연수를 곱하여 나온 결과에서 각 숫자가 몇 번 나오는지 출력하는 프로그램
# 첫째 줄엔 0의 개수, 둘째 줄부터 열 번째 줄까지 1부터 9의 개수 출력

a = int(input())
b = int(input())
c = int(input())
result = a * b * c
result_str = str(result)
for i in range(10):
    print(result_str.count(str(i)))