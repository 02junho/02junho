# 입력 받은 그대로 출력하는 문제

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break
