team_name = input("Введите название команды: ")
print(f"{team_name} - чемпион!")
print("-" * len(team_name))
print(f"{team_name.lower()} - чемпион!")
print("Длина названия: ", len(team_name))
p_in_team = "п" in team_name
print("Буква п в названии: ", "п" in team_name.lower())
print("Число букв а: {} ".format(team_name.lower().count("а")))