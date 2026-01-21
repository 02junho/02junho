# 영어 대소문자와 공백으로 이루어진 문자열이 주어졌을때, 단어의 개수 출력하는 문제

def count_words(s):
    words = s.split()
    return len(words)
input_string = input()
print(count_words(input_string))