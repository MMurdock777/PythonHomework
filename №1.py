print("Input positive number")
number = int(input())

while (number <= 0):
    print("Input positive number")
    number = int(input())

sum = (number*(number+1))/2
print("Sum of natural numbers:", sum)