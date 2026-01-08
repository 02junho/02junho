## 테스트 케이스 개수 입력 후 각 테스트 케이스마다 두 정수의 합 출력 문제

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)