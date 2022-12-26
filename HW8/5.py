import zipfile


def get_zip(path: str):
    zip_read = zipfile.ZipFile(path)
    return zip_read


def letter_count_from_zip(zip_path: str, file_path: str):
    symbol_dict = {}
    with get_zip(zip_path).open(file_path, 'r') as zr:
        for i in zr:
            line = i.decode("utf-8")
            for j in line:
                if j.isalpha():
                    if j in symbol_dict:
                        symbol_dict[j] += 1
                    else:
                        symbol_dict[j] = 1
    return symbol_dict


def output_sorted_results(letter_stats: dict):
    letter_stats = sorted(letter_stats.items(), key=lambda x: x[1], reverse=True)
    print("Буква | Частота")
    for i in letter_stats:
        print(f"    {i[0]} | {i[1]}")


letter_frequency = letter_count_from_zip('voyna-i-mir.zip', 'voyna-i-mir.txt')
output_sorted_results(letter_frequency)

