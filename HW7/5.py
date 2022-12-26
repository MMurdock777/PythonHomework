class OperationError(Exception):
    def __init__(self):
        super().__init__()


def calculator(num1, operator: str, num2):
    try:
        if operator == "+":
            return num1+num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        elif operator == "//":
            return num1 // num2
        elif operator == "%":
            return num1 % num2
        elif operator == "^":
            return num1 ** num2
    except ZeroDivisionError:
        print("Деление на 0 не возможно. Введите исправленное выржение")
        return None


i = 1
operations_list = ["+", "-", "*", "/", "//", "%", "^"]
while i:
    calc_inputs = []
    try:
        equation = input("Введите выражение:")
        if equation == "":
            i = 0
            continue
        calc_inputs = equation.split()
        if calc_inputs[1] in operations_list:
            answer = calculator(float(calc_inputs[0]), calc_inputs[1], float(calc_inputs[2]))
            if answer is None:
                raise ZeroDivisionError
            else:
                print(answer)
        else:
            raise OperationError
    except OperationError and ValueError and ZeroDivisionError and IndexError:
        print("Выражение введено неверно. Введите исправленное выражение.")
        continue
