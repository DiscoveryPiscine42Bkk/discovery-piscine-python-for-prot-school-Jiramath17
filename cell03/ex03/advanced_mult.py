import sys

def print_multiplication_table():
    row = 0
    while row <= 10:
        line = [str(row * col) for col in range(11)]
        print(f"Table de {row}: " + " ".join(line))
        row += 1

def main():
    if len(sys.argv) > 1:
        print("none")
    else:
        print_multiplication_table()

if __name__ == "__main__":
    main()