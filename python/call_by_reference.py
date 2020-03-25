num1 = 0
num2 = 0
while True:
    num1 += 1
    num2 += 1
    if id(num1) != id(num2):
        break

print("num1: " + str(num1))
print("num2: " + str(num2))