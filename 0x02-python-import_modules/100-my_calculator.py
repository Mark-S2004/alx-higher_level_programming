#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operation = {'+': add, '-': sub, '*': mul, '/': div}
    result = operation.get(argv[2], None)
    if not result:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {argv[2]} {b} = {result(a, b)}")
