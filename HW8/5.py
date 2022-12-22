import zipfile

symbol_dict = {}
zip = zipfile.ZipFile('voyna-i-mir.zip')
with zip.open('voyna-i-mir.txt', 'r') as zr:
    for i in zr:
        line = i
        for j in line:
            if j in symbol_dict:
                symbol_dict[i] += 1
            else:
                symbol_dict[i] = 1
print(symbol_dict)