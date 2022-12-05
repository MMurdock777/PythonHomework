def nok(nums: list) -> int:
    i = 0
    nok_found = max(num_list)
    while i < 1:
        for j in range(0, len(nums)):
            b = nok_found % nums[j]
            if b != 0:
                nok_found += 1
                break
            if j == len(nums) - 1:
                i = 1
    return nok_found


def nod(nums: list) -> int:
    i = 0
    nod_found = 2
    while i < 1:
        if nod_found > min(nums) / 2:
            nod_found = 1
            break
        for j in range(0, len(nums)):
            b = nums[j] % nod_found
            if b != 0:
                nod_found += 1
                break
            if j == len(nums) - 1:
                i = 1
    return nod_found


num_list = [4, 8, 6, 8, 12]

print("НОК:", nok(num_list))
print("НОД:", nod(num_list))
