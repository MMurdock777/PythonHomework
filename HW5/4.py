letters = ["a", "b", "c", "d", "e", "f"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pairs = list(map(lambda x, y: (x, y), letters, numbers))

print(pairs)
