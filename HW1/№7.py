print("Input number with 2 digits:")
num1 = int(input())
print("Input number with 3 digits:")
num2 = int(input())
num1first = num1 // 10
num1second = num1 % 10
num2first = num2 // 100
num2second = num2 % 100 // 10
num2third = num2 % 100 % 10
print(f"Sum of digits of first number: {num1first + num1second}\n"
      f"Product of digits of first number: {num1first * num1second}\n"
      f"Sum of digits of second number: {num2first + num2second + num2third}\n"
      f"Product of digits of second number: {num2first * num2second * num2third}\n")
