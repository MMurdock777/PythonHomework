list_a = []
list_b = []


for i in range(1, 4):
    list_a.append(input(f"Введите {i}-е число для первого списка: "))
for i in range(1, 8):
    list_b.append(input(f"Введите {i}-е число для второго списка: "))

print(f"Первый список: {list_a}")
print(f"Второй список: {list_b}")

list_a.extend(list_b)
list_a = list(set(list_a))
print(f"Новый первый список с уникальными элементами: {list_a}")
