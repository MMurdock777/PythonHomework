def exact_power_two(num: int):
    if num == 1:
        print("YES")
        return
    i = num % 2
    if i != 0 or num < 1:
        print("NO")
        return
    else:
        if num >= 2:
            exact_power_two(num // 2)


exact_power_two(int(input("Введите число:  ")))
