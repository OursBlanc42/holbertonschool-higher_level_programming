#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for subitem in item:
            print("{:d}".format(subitem), end=" ")

        print()
