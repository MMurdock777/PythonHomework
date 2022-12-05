def sort_neg_pos(*nums):
    list_pos = []
    list_neg = []
    for i in nums:
        if i >= 0:
            list_pos.append(i)
        else:
            list_neg.append(i)
    for i in range(0, len(list_pos) - 1):
        for j in range(0, len(list_pos)-1-i):
            if list_pos[j] > list_pos[j+1]:
                swap = list_pos[j]
                list_pos[j] = list_pos[j+1]
                list_pos[j+1] = swap
    for i in range(0, len(list_neg) - 1):
        for j in range(0, len(list_neg) - 1 - i):
            if list_neg[j] < list_neg[j+1]:
                swap = list_neg[j]
                list_neg[j] = list_neg[j+1]
                list_neg[j+1] = swap

    tuple_lists = (list_neg, list_pos)
    return tuple_lists


print(sort_neg_pos(-1, 7, 5, 1000, -11, -6, 500, -27))
