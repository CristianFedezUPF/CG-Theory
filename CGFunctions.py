import MatrixVectorOperations as MVO
import numpy as np


def orientation(point1, point2, point3):
    matrix = 0
    row1 = np.append(point1, 1)
    row2 = np.append(point2, 1)
    row3 = np.append(point3, 1)
    if row1.size == 3:
        matrix = np.array([row1, row2, row3])
    elif row1.size == 4:
        row4 = [1,1,1,1]
        matrix = np.array([row1, row2, row3, row4])
    determinant = MVO.determinant(matrix)
    if determinant > 0:
        print("This orientation is anti-clockwise")
    elif determinant < 0:
        print("This orientation is clockwise")
    else:
        print("This three points form a line")

def normal(point1, point2, point3):
    point1_point2 = MVO.substraction(point2, point1)
    point2_point3 = MVO.substraction(point3, point2)
    res = MVO.cross_product(point1_point2, point2_point3)
    res = MVO.division(res, MVO.module(res))
    print(res)


A = np.array([1, 2, 1])
B = np.array([-1, 1, 0])
C = np.array([0, -2, -1])
orientation(A, B, C)
normal(A, B, C)