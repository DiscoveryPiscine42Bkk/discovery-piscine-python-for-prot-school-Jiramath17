number = input("Enter a number: ").strip()

if number.lstrip('-').isdigit():
    number = int(number)  
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
else:
    print("Invalid input! Please enter a valid number.")
