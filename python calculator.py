#Simple Calculator

# This adds two numbers
def add (x, y):
    return x + y

#This subtracts two numbers
def subtract(x, y):
    return x - y

#This multiplies two numbers
def multliply(x, y):
    return x * y

#This divides two numbers
def divide(x, y):
    return x / y


print("Select Operation")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

while True:
    #User Input
    choice = input ("Enter Choice(1,2,3,4): ")

    #Check to make sure the input was valid
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multliply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")