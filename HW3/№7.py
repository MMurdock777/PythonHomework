pair_num = int(input("Кол-во коньков: "))
pair_list = []
for i in range(1, pair_num+1):
    pair_list.append(int(input(f"Размер {i}-й пары: ")))

sorted(pair_list)

person_size_num = int(input("Кол-во людей: "))
person_size_list = []
for i in range(1, person_size_num + 1):
    person_size_list.append(int(input(f"Размер ноги {i}-го человека: ")))

sorted(person_size_list)

people_with_skates = 0
for j in person_size_list:
    for k in pair_list:
        if j <= k:
            people_with_skates += 1
            pair_list.remove(k)
            break
print(f"Наибольшее кол-во людей, которые могут взять ролики: {people_with_skates}")
