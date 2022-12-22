sum_of_numbers = 0

with open("input_numbers.txt", "r") as fr:
    lines = fr.readlines()
    for line in lines:
        line_stripped = line.rstrip()
        nums = line_stripped.split()
        for num in nums:
            sum_of_numbers += int(num)
fr.close()
with open("output_sum.txt", "w") as fw:
    fw.write(str(sum_of_numbers))
