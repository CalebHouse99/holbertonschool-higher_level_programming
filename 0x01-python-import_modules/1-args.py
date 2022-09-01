#!/usr/bin/python3
import sys

def main():
    pass

if __name__ == "__main__":
    main()

if sys.argv == None:
    print("{}.".format(len(sys.argv)))
else:
    print("{}: {}".format(len(sys.argv), sys.argv))
