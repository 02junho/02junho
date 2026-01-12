# 성적이 주어졌을때 학점을 출력하는 문제 ex) A+ 입력시 4.3 출력

# grade = input()
# if grade == "A+":
#     print(4.3)
# elif grade == "A0":
#     print(4.0)
# elif grade == "A-":
#     print(3.7)
# elif grade == "B+":
#     print(3.3)
# elif grade == "B0":
#     print(3.0)
# elif grade == "B-":
#     print(2.7)
# elif grade == "C+":
#     print(2.3)
# elif grade == "C0":
#     print(2.0)
# elif grade == "C-":
#     print(1.7)
# elif grade == "D+":
#     print(1.3)
# elif grade == "D0":
#     print(1.0)
# elif grade == "D-":
#     print(0.7)
# else:
#     print(0.0)


# 다른 방법
grade = input()
grades = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}
print(grades[grade])