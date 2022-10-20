print("Input v - speed:")
v = float(input())
print("Input t - time:")
t = float(input())
distance = v * t

laps = distance // 123
kilometer = distance % 123

print(f"Ran {laps} laps and stopped on kilometer {kilometer}")


# TODO здесь надо было с помощью остатков от деления находить остаток круга