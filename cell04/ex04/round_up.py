x = input("Give me a number: ")
num = float(x)
if num == int(num):
    print(int(num))
elif num > 0:
    print(int(num) + 1)
else:
    print(int(num))