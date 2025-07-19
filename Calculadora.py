# Calculator Exercise with Conditional Statements

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
opr = input('Choose the operation to perform: Addition, Subtraction, Multiplication or Division: ').lower()
result = 0

if opr == 'addition':
    result = num1 + num2
    print("The addition of", num1, "+", num2, "is", result)
elif opr == 'subtraction':
    result = num1 - num2
    print("The subtraction of", num1, "-", num2, "is", result)
elif opr == 'multiplication':
    result = num1 * num2
    print("The multiplication of", num1, "*", num2, "is", result)
elif opr == 'division':
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The division of", num1, "/", num2, "is", result)
else:
    print("Invalid operation. Please choose Addition, Subtraction, Multiplication, or Division.")
