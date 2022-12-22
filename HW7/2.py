i = 1
sum_of_nums = 0
while i:
    try:
        num_input = input("Введите следующее число: ")
        if num_input == "":
            i = 0
            pass
        else:
            sum_of_nums += float(num_input)
            print(round(sum_of_nums, 4))
    except ValueError:
        print("Введенное значение не является числом")
        pass
