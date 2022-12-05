def count_letters(line: str):
    line = line.lower()
    letters = {}
    for i in line:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    for j in letters:
        print(f"{j} = {letters[j]}")


count_letters("Это пробное предложение.")
