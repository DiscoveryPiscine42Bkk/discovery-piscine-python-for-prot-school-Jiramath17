
number = input("Give me a number: ")

try:
    float_number = float(number)

    if '.' in number and float_number == int(float_number):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valid number.")
