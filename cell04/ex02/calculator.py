
def calculate_operations(a, b):
    
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "undefined (cannot divide by zero)"
    
    return addition, subtraction, division, multiplication

num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

print("Thank you!")

add, sub, div, mul = calculate_operations(num1, num2)

print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} * {num2} = {mul}")
