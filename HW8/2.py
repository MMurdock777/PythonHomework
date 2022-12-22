try:
    file_in = input("Введите путь файла для чтения: ")
    with open(file_in, "r", encoding="utf-8") as fr:
        lines = fr.readlines()
        lines_for_new_file = []
        for line in lines:
            if line[0] == "#":
                continue
            else:
                lines_for_new_file.append(line)
    fr.close()
    file_out = input("Введите путь файла для записи: ")
    with open(file_out, "w") as fw:
        fw.writelines(lines_for_new_file)
except IOError:
    print("Введенный путь не существует")
