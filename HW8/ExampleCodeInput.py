#Счетчик суммы чисел в файле
sum_of_numbers = 0

#Открытие файла для чтения
with open("input_numbers.txt", "r") as fr:
    lines = fr.readlines()
#Построчная обработка файла
    for line in lines:
        line_stripped = line.rstrip()
        nums = line_stripped.split()
        for num in nums:
            sum_of_numbers += int(num)
#Закрытие файла
fr.close()
#Открытие файла для записи
with open("output_sum.txt", "w") as fw:
    fw.write(str(sum_of_numbers))
