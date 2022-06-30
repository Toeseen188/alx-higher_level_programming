#!/usr/bin/python3
if __name__ == "__main__":
    from calculation_1 import add, mul, div, sub
    a = 10
    b = 5
    print(f"{a:d} + {b:d} = {add(a, b):d}")
    print(f"{a:d} - {b:d} = {sub(a, b):d}")
    print(f"{a:d} * {b:d} = {mul(a, b):d}")
    print(f"{a:d} / {b:d} = {div(a,b):d}")
