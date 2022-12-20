def reverse_number(num: int, rev_num=0):
    if num < 10:
        return rev_num * 10 + num

    remainder = num % 10
    rev_num = rev_num * 10 + remainder
    return reverse_number(num // 10, rev_num)


print(reverse_number(547889321))
