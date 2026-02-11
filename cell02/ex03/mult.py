x=int(input("Enter the first number:\n"))
y=int(input("Enter the second number:\n"))
z=x*y
print(f"{x} x {y} = {z}")
if z<0:
    print("This number is negative.")
elif z>0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")