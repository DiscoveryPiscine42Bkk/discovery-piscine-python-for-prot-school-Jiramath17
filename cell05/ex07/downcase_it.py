
import sys

sys.argv = ['downcase_it.py', 'HELLO WORLD'] 

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].lower())
