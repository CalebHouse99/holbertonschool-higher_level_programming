#!/usr/bin/python3
import sys

def main():
    pass

if __name__ == "__main__":
    main()

n = len(sys.argv)

if len(sys.argv) - 1 == 0:
    print("{}.".format(len(sys.argv)))
elif len(sys.argv) - 1 == 1:
    print("{} argument:{}1: {}".format(len(sys.argv) - 1, '\n', sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1), end="\n")
    for i in range(1, n):
        if i < n:
            print("{}:{}".format(len(sys.argv) - 1, n - 1, sys.argv[i]))
