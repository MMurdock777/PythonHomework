def flatten_list(list_in: list):
    list_out = []
    for i in list_in:
        if isinstance(i, list):
            list_out.extend(flatten_list(i))
        else:
            list_out.append(i)
    return list_out


print(flatten_list([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
