#Designing simple calculator with basic arithmetic operations, with two number inputs
# Arithmetic operators (Addition(+), substraction(-), Multiplication(*), Division(/), Modulus(%), Exponentiation(**), Floor(//))

#defining functions for performing arithmetic functions
def addition(x, y):
    return x +y;
def substraction(x, y):
    return x -y 
def multiplication(x, y):
    return x *y
def division(x, y):
    if (x != 0):
        return x / y 
    else:
        return "please give valid number!"
def modulus(x , y):
    return x % y
def exponentiation(x, y):
    return x ** y 
def floor (x,y):
    if (x != 0):
        return x // y 
    else:
        return "please give valid number!"


#taking inputs from the user 
num1 = int(input("Enter number for first Input: "))
num2 = int(input("Enter number for second Input: "))
operation = input("Please give arithmetic operator(+, -, *, /, **, %, //): ")
#Execution of arithmetic operations
if( operation == "+"):
    result = addition(num1, num2)
elif( operation == "-"):
    result = substraction(num1, num2)

elif( operation == "*"):
    result = multiplication(num1, num2)
elif( operation == "/"):
    result = division(num1, num2)
elif( operation == "%"):
    result = modulus(num1, num2)
elif( operation == "**"):
    result = exponentiation(num1, num2)
elif( operation == "//"):
    result = floor(num1, num2)
else:
    result = "please give  valid operator"
print(result)