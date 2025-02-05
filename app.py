def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):  
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y
    
def exponent(x , y):
    return x ** y

# Test the functions
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
print(multiply(5, 3))  # Output: 15
print(divide(5, 3))  # Output: 1.666666666666
print(exponent(5, 3))  # Output: 125

def greet(name):
    return "Hello, " + name + "!"
print(greet("John"))  # Output: Hello, John!

