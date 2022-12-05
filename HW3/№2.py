a = list(range(160, 177, 2))
b = list(range(162, 181, 3))

c = a + b
for i in range(0, len(c) - 1):
    for j in range(0, len(c) - 1 - i):
        if c[j] > c[j + 1]:
            swap = c[j]
            c[j] = c[j + 1]
            c[j + 1] = swap

print("Отсортированный список учеников:", c)
