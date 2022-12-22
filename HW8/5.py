import zipfile

symbol_dict = {}
zipread = zipfile.ZipFile('voyna-i-mir.zip')
with zipread.open('voyna-i-mir.txt', 'r') as zr:
    for i in zr:
        line = i.decode("utf-8")
        for j in line:
            if j in symbol_dict:
                symbol_dict[j] += 1
            else:
                symbol_dict[j] = 1

symbol_dict = sorted(symbol_dict.items(), key=lambda x: x[1])
print(symbol_dict)
