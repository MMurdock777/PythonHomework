friend_num = int(input("Кол-во друзей: "))
debt_num = int(input("Долговых расписок: "))

debt_list = []
for i in range(1, debt_num+1):
    print(f"{i}-я расписка:")
    took = int(input("Кому: "))
    gave = int(input("От кого: "))
    amount = int(input("Сколько: "))
    single_debt = [took, gave, amount]
    debt_list.extend(single_debt)

print("Баланс друзей:")
balance_list = []
friend_balance = 0
for i in range(0, friend_num):
    for j in range(0, debt_num*3, 3):
        if debt_list[j] - 1 == i:
            friend_balance -= debt_list[j+2]
        if debt_list[j+1] - 1 == i:
            friend_balance += debt_list[j+2]
    print(f"{i + 1}: {friend_balance}")
    friend_balance = 0
