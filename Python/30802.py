# 웰컴 키트 만들기
# 티셔츠 사이즈 S, M, L, XL, XXL, XXXL이고 T장씩 뮦음
# 펜은 한 종류, P자루씩 묶음
# 첫 줄에 참가자의 수 N, 둘째 줄에 T장씩 사이즈별 신청자 수, 셋째 줄에 정수 티셔츠와 펜의 묶음 수를 의미하는 T와 P가 주어짐
# 출력 첫 줄에 티셔츠를 T장씩 최소 몇 묶음 사야 하는지, 둘째 줄에 펜을 P자루씩 최소 몇 묶음 사야 하는지 출력

import sys

# 입력 받기
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 1. 티셔츠 묶음 수 계산
tshirt_bundles = 0
for s in sizes:
    if s > 0:
        # 각 사이즈별로 필요한 묶음 수 계산
        # (s + T - 1) // T 는 올림 계산과 동일한 로직입니다.
        tshirt_bundles += (s + T - 1) // T

# 2. 펜 묶음 및 낱개 계산
pen_bundles = N // P
pen_individuals = N % P

# 결과 출력
print(tshirt_bundles)
print(f"{pen_bundles} {pen_individuals}")