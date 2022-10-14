print("Input v - speed:")
v = float(input())
print("Input t - time:")
t = float(input())
distance = v*t

while distance > 123:
    distance -= 123

if distance == 123:
    distance = 0

print("Stopped on kilometer #:", round(distance))


# TODO здесь надо было с помощью остатков от деления находить остаток круга