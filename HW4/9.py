def decimal_to_base(num_1: int, base: int) -> str:
    num_in_base = ""
    num_to_letter = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while num_1 >= base:
        digit = num_1 % base
        if digit >= 10:
            digit = num_to_letter[digit]
        num_in_base = str(digit) + num_in_base
        num_1 = num_1 // base

    if num_1 >= 10:
        num_1 = num_to_letter[num_1]
    num_in_base = str(num_1) + num_in_base

    return num_in_base


def base_to_decimal(num_2: str, base: int):
    i = 0
    num_in_dec = 0
    letter_to_num = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, }
    while i < len(num_2):
        digit = num_2[i]
        if digit.isalpha():
            digit = letter_to_num[digit]
        num_in_dec += base ** (len(num_2) - 1 - i) * int(digit)
        i += 1

    return num_in_dec


num = input("Введите число: ")
base_from = int(input("Введите исходную систему исчисления: "))
base_to = int(input("Введите целевую систему исчисления: "))

print(decimal_to_base(base_to_decimal(num, base_from), base_to))
