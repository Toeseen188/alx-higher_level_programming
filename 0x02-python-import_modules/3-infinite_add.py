#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    data = 0
    length = len(argv)
    for i in range(1, length):
        data = int(argv[i]) + data
    print(f"{data}")
