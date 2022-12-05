guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

flag = 0
while flag == 0:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    status = input("Гость пришёл или ушёл? ")
    if status == "пришел":
        guest_name = input("Имя гостя: ")
        if len(guests) == 6:
            print(f"Прости, {guest_name}, но мест нет")
        else:
            print(f"Привет, {guest_name}!")
            guests.append(guest_name)
    if status == "ушел":
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!")
    if status == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        flag = 1
