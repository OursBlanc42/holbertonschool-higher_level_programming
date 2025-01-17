#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

"""

"""

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = ["+", "-", "*", "/"]
    funcall = [add, sub, mul, div]

    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op_index = operator.index(sys.argv[2])
        result = funcall[op_index](a, b)
        print(f"{a} {sys.argv[2]} {b} = {result}")
