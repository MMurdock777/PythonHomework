import math
print("Input first number:")
num1 = int(input())
while (num1 <= 0):
    print("Input positive number")
    num1 = int(input())
print("Input second number:")
num2 = int(input())
while (num2 <= 0):
    print("Input positive number")
    num2 = int(input())
sum = num1+num2
diff = num1-num2
prod = num1*num2
quotient = round(num1/num2, 2)
floorquot = num1//num2
modulo = num1%num2
power = num1**num2
log1 = round(math.log10(num1),2)
log2 = round(math.log10(num2),2)
less = num1<num2
lessequ = num1<=num2
great = num1>num2
greatequ = num1>=num2
notequ = num1!=num2
equal = num1 == num2
print(f"{num1} + {num2} = {sum}\n{num1} - {num2} = {diff}\n"
      f"{num1} * {num2} = {prod}\n{num1} / {num2} = {quotient}\n"
      f"{num1} // {num2} = {floorquot}\n{num1} % {num2} = {modulo}\n"
      f"{num1} ** {num2} = {power}\nlog10({num1})  = {log1}\n"
      f"log10({num2})= {log2}\n{num1} < {num2} = {less}\n"
      f"{num1} <= {num2} = {lessequ}\n{num1} > {num2} = {great}\n"
      f"{num1} >= {num2} = {greatequ}\n{num1} != {num2} = {notequ}\n"
      f"{num1} == {num2} = {equal}")

