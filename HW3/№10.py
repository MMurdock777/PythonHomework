num_amount = int(input("Кол-во чисел: "))
num_list = []
for i in range(0, num_amount):
    num_list.append(int(input("Число: ")))
print(f"Последовательность: {num_list}")

i = 0
insert_spot = len(num_list)
insert_num = 0

while i < len(num_list) - 1:
    if num_list[i] != num_list[len(num_list) - 1 - i]:
        num_list.insert(insert_spot, num_list[insert_num])
        i = 0
        insert_num += 1
    else:
        i += 1

print(f"Нужно приписать чисел: {len(num_list) - insert_spot}")
list_added= []
for i in range(insert_spot, len(num_list)):
    list_added.append(num_list[i])

print(f"Сами числа: {list_added}")



