class OperationError(Exception):
    def __init__(self):
        super().__init__()


def calculator(num1, operator: str, num2):
    try:
        if operator == "+":
            return num1+num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            return num1 / num2
        if operator == "//":
            return num1 // num2
        if operator == "%":
            return num1 % num2
        if operator == "^":
            return num1 ** num2
    except ZeroDivisionError:
        return None


operations_list = ["+", "-", "*", "/", "//", "%", "^"]

calc_inputs = []
sum_of_equations = 0
try:
    with open("calc_input.txt ", "r", encoding="utf-8") as fr:
        lines = fr.readlines()
        for line in lines:
            try:
                if line == "":
                    continue
                calc_inputs = line.rstrip().split()
                if calc_inputs[1] in operations_list:
                    answer = calculator(float(calc_inputs[0]), calc_inputs[1], float(calc_inputs[2]))
                    if answer is None:
                        print(f"Выражение введено неверно. Исправьте выражение {line.rstrip()}")
                    else:
                        sum_of_equations += answer
                else:
                    raise OperationError
            except OperationError and TypeError and IndexError:
                print(f"Выражение введено неверно. Исправьте выражение {line.rstrip()}")
                continue

    print(sum_of_equations)

except IOError and FileNotFoundError:
    print("Путь файла не найден.")
