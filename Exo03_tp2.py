#!/bin/python3
import numpy as np
from math import gcd, cos, sin, tan, radians
from functools import reduce


def ppcm(numbers):
    '''

    '''
    return(reduce(lambda x, y: x * y // gcd(x, y), numbers))



def pgcd(numbers):
    return reduce(gcd, numbers) 


def calculate_trigonometric(angles):
    trig_values = {
        "cos": [cos(radians(angle)) for angle in angles],
        "sin": [sin(radians(angle)) for angle in angles],
        "tan": [tan(radians(angle)) for angle in angles],
    }
    return trig_values


def list_operations(list1, list2):
    operations = {
        "sum": [x + y for x, y in zip(list1, list2)],
        "difference": [x - y for x, y in zip(list1, list2)],
        "multiplication": [x * y for x, y in zip(list1, list2)],
        "division": [x / y for x, y in zip(list1, list2)],
    }
    return operations


def calculate_power_and_modulo(list1, list2):
    power_mod = {
        "power": [x ** y for x, y in zip(list1, list2)],
        "modulo": [x % y for x, y in zip(list1, list2)],
    }
    return power_mod


def matrix_operations(matrix):
    matrix = np.array(matrix)
    determinant = np.linalg.det(matrix)
    trace = np.trace(matrix)
    transpose = matrix.T
    rank = np.linalg.matrix_rank(matrix)
    inverse = None
    if determinant and determinant != 0:
        inverse = np.linalg.inv(matrix)

    results = {
        "determinant": determinant,
        "trace": trace,
        "rank": rank,
        "transpose": transpose,
        "inverse": inverse,
    }
    return results

def element_wise_operations(matrix, operation):
    np_matrix = np.array(matrix)
    if operation == "square":
        return np_matrix ** 2
    elif operation == "sqrt":
        return np.sqrt(np_matrix)
    else:
        print("Unsupported operation!")

def eigen_proper(matrix):
    np_matrix = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(np_matrix)
    return {
        "eigenvalus": eigenvalues,
        "eigenvectors": eigenvectors,
    }

