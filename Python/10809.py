# 알파벳 소문자로 이루어진 단어 S
# 각 알파벳이 단어에 처음 등장하는 위치를 공백으로 구분해서 출력
# 단어에 포함되지 않은 알파벳은 -1

word = input().strip()
positions = [-1] * 26  # 알파벳 개수만큼 초기화
for index, char in enumerate(word):
    if positions[ord(char) - ord('a')] == -1:  # 처음 등장하는 경우
        positions[ord(char) - ord('a')] = index
print(' '.join(map(str, positions)))
