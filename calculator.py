print("WELCOME TO TWO NUMBER CALCULATOR")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("Choose between: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
n=input("Enter your choice: ")
if n=="1":
    print("The addition of number",a,"and",b,"is",a+b)
elif n=="2":
    print("The subtraction of number",a,"and",b,"is",a-b)
elif n=="3":
    print("The multiplication of number",a,"and",b,"is",a*b)
elif n=="4":
    if b==0:
        print("Error: Division by zero")
    else:
        print("The division of number",a,"and",b,"is",a/b)