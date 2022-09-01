#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        edge_case = [0, None]
        edge_case = tuple(edge_case)
        return edge_case
    tuple_a = [len(sentence), sentence[0]]
    tuple_a = tuple(tuple_a)
    return tuple_a
