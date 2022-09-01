#!/usr/bin/python3
import sys

def main():
    pass

if __name__ == "__main__":
    main()

if len(sys.argv) - 1 == 0:
    print("{}.".format(len(sys.argv)))
elif len(sys.argv) - 1 == 1:
    print("{} argument:{}1: {}".format(len(sys.argv) - 1, '\n', sys.argv[1]))
else:
    print("{} arguments:{}{}:{}".format(len(sys.argv) - 1, '\n', len(sys.argv) - 1, sys.argv[1:]))
