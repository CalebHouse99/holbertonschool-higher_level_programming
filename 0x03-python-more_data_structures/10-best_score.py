#!/usr/bin/python3
def best_score(a_dictionary):
    highest = -1
    winner = ""
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > highest:
                highest = a_dictionary[key]
                winner = key
    else:
        return None
    return winner
