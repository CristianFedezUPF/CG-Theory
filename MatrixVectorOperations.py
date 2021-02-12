import numpy as np


def inverse(matrix):
    return np.linalg.inv(matrix)


def determinant(matrix):
    return np.linalg.det(matrix)


def matrix_product(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)


def matrix_dot(matrix1, matrix2):
    return np.dot(matrix1, matrix2)


def check_if_point_inside(barycentricCoords):
    inside = True
    for number in barycentricCoords:
        if number < 0 or number > 1:
            inside = False
    return inside


# dimensions must be 2 or 3
def cross_product(vector1, vector2):
    return np.cross(vector1, vector2)


