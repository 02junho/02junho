# ACM 호텔 문제
# 첫 줄엔 입력의 개수 T
# 다음 줄부터 각 테스트 케이스마다 정수 H, W, N
# H는 호텔의 층 수, W는 각 층의 방 수, N은 몇 번째 손님인지 나타낸다.
# 각 손님은 엘리베이터 옆에 있는 101호부터 차례대로 배정
# 엘리베이터에서 가까운 방이 우선
# 즉, 1층부터 H층까지 차례대로 배정
# 각 층의 방은 왼쪽부터 W호까지 차례대로 배정
# N번째 손님에게 배정되는 방 번호를 출력하는 문제

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room_number = N // H + 1
    if floor == 0:
        floor = H
        room_number -= 1
    print(f"{floor}{room_number:02d}")