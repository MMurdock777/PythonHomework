i = 0
start_num = 0
nums = 100
mid_num = nums // 2
check_step = mid_num
while i < 1:
    check_step = check_step // 2
    if check_step < 1:
        check_step = 1
    ans = input(f"Твое число равно, меньше или больше, чем число {mid_num}? ")
    if ans == "1":
        print("Твое число: ", mid_num)
        break
    elif ans == "2":
        mid_num = mid_num + check_step
    else:
        mid_num = mid_num - check_step
