# Создать 2 пустых списка
a = []
b = []

# Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
a.append(4.5)
a.append(3.4)
# Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
a.extend([8.7, 1.3])


# Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
b.append(14.5)
b.append(3.4)

# Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
b.extend([8.7, 11.3])

# Вставить целое число 100 на 2-е и 4-е место списка 'a'
a.insert(1, 100)
a.insert(3, 100)

# Вставить целое число 200 на 1-е и 3-е место списка 'b'
b.insert(0, 200)
b.insert(2, 200)

# Вывести списки на экран
print("Исходные списки:")
print(a)
print(b)

# Удалить первые элементы из списков 'a' и 'b'
del a[0]
del b[0]

# Удалить элемент 100 из списка 'a'
a.remove(100)
# Удалить элемент 200 из списка 'b'
b.remove(200)

# Вывести списки на экран
print("\nПосле удалений:")
print(a)
print(b)

# Создать множества из списков 'a' и 'b', а также их пересечение
sa = set(a)
sb = set(b)
sa_and_sb = sa & sb
# Вывести экран уникальные элементы каждого списка и общие
print("\nУникальные элементы:\n 1-й: {}\n 2-й: {}".format(sa, sb))
print("общие:", sa_and_sb)

# Соединить списки 'a' и 'b'
c = a + b

# Отсортировать список 'c' по возрастанию и убыванию
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

# Среднее арифметическое элементов списка 'c', расположенных на четных местах
sr_ar = sum(c[1::2])/len(c[0::2])
# Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
product = 1
for i in c[0::2]:
    product *= i
sr_geom = round(product ** (1 / len(c[1::2])), 2)

# Максимальный и минимальный элементы
c_max = max(c)
c_min = min(c)

# Вывести результаты на экран
print("\nИтоговые:")
print("3-й:", c)
print("Сортировка (возр.):", c_asc)
print("Сортировка (убыв.):", c_desc)
print(f"Ср. арифм. = {sr_ar}, ср. геометр. = {sr_geom}")
print(f"Макс. и мин.: {c_max} {c_min}")




