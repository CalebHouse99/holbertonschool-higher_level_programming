#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(a_dictionary.items()))
    for key in a_dictionary:
        print("{}: {}".format(key, a_dictionary[key]))
