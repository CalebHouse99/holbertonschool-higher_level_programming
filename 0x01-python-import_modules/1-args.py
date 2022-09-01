#!/usr/bin/python3
import sys

def main():
    pass

if __name__ == "__main__":
    main()

if sys.argv == None:
    print("{}.".format(len(sys.argv)))
else:
    print("{} arguments:{} {}".format(len(sys.argv), '\n', sys.argv[]))
