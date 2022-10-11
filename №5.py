print("ax + b = 0")
print("Input a")
a = float(input())
print("Input b")
b = float(input())
print("Segment [m;n]")
print("Input m")
m = float(input())
print("Input n")
n = float(input())
solution = -(b)/a
answer = m<=solution<=n
print("Solution:", solution)
print (f"m<={solution}<=n = {answer}")

