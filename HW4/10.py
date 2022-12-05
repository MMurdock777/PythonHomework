def check_magic_date(date: str):
    day = int(date.split(".")[0])
    month = int(date.split(".")[1])
    year = int(date.split(".")[2][2:])
    if day * month == year:
        print(f"{date} - магическая дата")
    # else:
    # print(f"{date} - не магическая дата")


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for y in range(1901, 2001):
    leap_check = 0
    if y % 4 == 0:
        leap_check = 1
    for m in range(1, 13):
        days = days_in_month[m - 1]
        if days == 28:
            days += leap_check
        for d in range(1, days + 1):
            check_magic_date(f"{d}.{m}.{y}")

# Для индивидуального ввода
# date_check = input("Введите дату в формате ДД.ММ.ГГ: ")
# check_magic_date(date_check)
