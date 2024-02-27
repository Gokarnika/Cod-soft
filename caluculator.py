def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("select operation:")
print("1-Add")
print("2-Subract")
print("3-Multiply")
print("4-Divide")
while True:
    choice=input("Enter choice(1/2/3/4):")
    if choice in('1','2','3','4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except valueError:
            print("Invalid input")
            continue
        if choice=="1":
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=="2":
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=="3":
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=="4":
            print(num1,"/",num2,"=",divide(num1,num2))
        next_calculation=input("to go for next calculation?(yes/no):")
        if next_calculation=="no":
           break
    else:
        print("invalid input")

