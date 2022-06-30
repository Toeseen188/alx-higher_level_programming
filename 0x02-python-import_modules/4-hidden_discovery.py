#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    data = dir(hidden_4)
    length = len(data)
    for i in range(1, length):
        if data[i][0] != '_':
            print("{:s}".format(data[i]))
