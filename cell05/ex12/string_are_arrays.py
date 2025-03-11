
import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    found_z = False
    for char in string:
        if char == 'z':
            print('z', end='')
            found_z = True
    
    if not found_z:
        print("none")
    else:
        print()  
