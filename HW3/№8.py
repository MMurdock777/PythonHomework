person_num = int(input("Кол-во человек: "))
count_num = int(input("Какое число в считалке? "))

person_list = list(range(1, person_num+1))
print(person_list)

startnum = 0
while len(person_list) > 1:
    print(f"Текущий круг людей: {person_list}")
    print(f"Начало счёта с номера {person_list[startnum]}")
    leave = abs(count_num + startnum - 1)
    while leave > len(person_list) - 1:
        leave -= len(person_list)
    print(f"Выбывает человек под номером {person_list[leave]}")
    if leave == len(person_list) - 1:
        startnum = 0
    else:
        startnum = leave
    person_list.pop(leave)

print(f"Остался человек под номером: {person_list[0]}")

