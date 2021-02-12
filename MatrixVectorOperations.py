import numpy as np

def addition(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def substraction(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

# element wise, NOT matrix multiplication, use matrix_product() for that
def product(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def division(matrix1, matrix2):
    return np.divide(matrix1, matrix2)

def module(vector):
    return np.linalg.norm(vector)

def inverse(matrix):
    return np.linalg.inv(matrix)

def determinant(matrix):
    return np.linalg.det(matrix)

def matrix_product(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def matrix_dot(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# dimensions must be 2 or 3
def cross_product(vector1, vector2):
    return np.cross(vector1, vector2)


def check_if_point_inside(barycentric_coords):
    inside = True
    for number in barycentric_coords:
        if number < 0 or number > 1:
            inside = False
    return inside
