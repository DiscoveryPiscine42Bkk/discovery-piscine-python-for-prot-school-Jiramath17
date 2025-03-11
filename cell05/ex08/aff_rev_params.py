
import sys

sys.argv = ['aff_rev_params.py', 'EiEi', 'Phum', 'D kub']  

if len(sys.argv) < 2:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)
