
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(f"{param}ism")
