
import sys

sys.argv = ['count_it.py', 'Game', 'of', 'Thrones']  

if len(sys.argv) < 2:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
