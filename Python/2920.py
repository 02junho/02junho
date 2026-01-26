# 다장조는 8개의 음으로 이뤄져 있고, 각각 1번~8번까지 번호를 붙인다
# c d e f g a b C 총 8개 음이며 각각 1 2 3 4 5 6 7 8번이다
# 1부터 8까지 차례대로 연주하면 ascending(오름차순)
# 8부터 1까지 차례대로 연주하면 descending(내림차순
# 섞이면 mixed

notes = list(map(int, input().split()))
if notes == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif notes == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")