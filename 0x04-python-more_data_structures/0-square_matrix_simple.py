#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda y: y * y), elm)) for elm in matrix]
