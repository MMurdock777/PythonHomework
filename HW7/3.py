class NumOutOFScope(Exception):
    def __init__(self):
        super().__init__()


def grade_converter(grade_input):
    try:
        grade_input = int(grade_input)
        if 91 <= grade_input <= 100:
            return "A"
        elif 84 <= grade_input <= 90:
            return "B"
        elif 74 <= grade_input <= 83:
            return "C"
        elif 68 <= grade_input <= 73:
            return "D"
        elif 61 <= grade_input <= 67:
            return "E"
        elif 0 <= grade_input <= 60:
            return "F"
        else:
            raise ValueError
    except ValueError:
        try:
            if grade_input == "A":
                return 5
            elif grade_input == "B":
                return 4
            elif grade_input == "C":
                return 4
            elif grade_input == "D":
                return 3
            elif grade_input == "E":
                return 3
            elif grade_input == "F":
                return 2
            else:
                raise NumOutOFScope
        except NumOutOFScope:
            return "Введенное значение неверно или не попадает в интервалы оценок"


i = 1
input_grades = []
while i:
    grade = input("Введите оценку: ")
    if grade == "":
        i = 0
        continue
    else:
        input_grades.append(grade)

for j in input_grades:
    print(grade_converter(j))
