
# Basic Calculator Program

print("Welcome to the Basic Calculator!")

# Get first number
num1 = input("Enter the first number: ")
num1 = float(num1)

# Get second number
num2 = input("Enter the second number: ")
num2 = float(num2)

# Get operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")
