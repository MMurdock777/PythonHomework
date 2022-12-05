def cipher(line: str, shift: int):
    line = line.lower()
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    pos_list = []
    for i in line:
        pos_list.append(alphabet.index(i))
    for j in range(shift):
        alphabet = alphabet[1:] + alphabet[0]
    print(alphabet)
    encoded_line = ""
    for k in pos_list:
        encoded_line += alphabet[k]

    print(encoded_line)


def decipher(line: str, shift: int):
    line = line.lower()
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_shifted = alphabet
    for j in range(shift):
        alphabet_shifted = alphabet_shifted[1:] + alphabet_shifted[0]
    pos_list = []
    for i in line:
        pos_list.append(alphabet_shifted.index(i))
    print(alphabet)
    decoded_line = ""
    for k in pos_list:
        decoded_line += alphabet[k]

    print(decoded_line)


cipher("введенного", 5)
decipher("жжйийттузу", 5)
