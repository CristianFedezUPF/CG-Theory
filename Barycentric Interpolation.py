import MatrixVectorOperations
import numpy as np

# input data
matrix = np.matrix(input("Input data using ; to separate rows and spaces to separate columns: \n"))
print("Matrix is:")
print(matrix)

# determinant
print("\nIts determinant is: ")
print(MatrixVectorOperations.determinant(matrix))

# the inverse matrix is the matrix that changes from usual coordinates into barycentric coordinates.
matrixToBarycentric = MatrixVectorOperations.inverse(matrix)
print("\nIts inverse matrix is: ")
print(matrixToBarycentric)
print('\n')

# input point
point = np.matrix(input("Input point as a column for which to find its barycentric coordinates\n (x\n y\n 1): \n"))

# barycentric coordinates are the result of multiplying the inverse matrix
# we've computed before and the point coordinates.
barycentricCoordinates = MatrixVectorOperations.matrix_product(matrixToBarycentric, point)
print("\nThe barycentric coordinates for this point are: ")
print(barycentricCoordinates)

is_inside = MatrixVectorOperations.check_if_point_inside(barycentricCoordinates)
if not is_inside:
    print("Point is outside triangle")

mode = -1
while mode < 0 or mode > 1:
    mode = int(input("Choose a mode, 0 for interpolating grayscale or 1 for RGB:\n"))

repeat = 1
while repeat != 0:
    # if interpolating grayscale value
    if mode == 0:
        grayscale_values = np.matrix(input("Introduce grayscale values for every vertex of the triangle as a row "
                                           "(Ga, Gb, Gc): \n"))
        grayscale_res = MatrixVectorOperations.matrix_dot(grayscale_values, barycentricCoordinates)
        print("The grayscale interpolated value corresponding to point ")
        print(point)
        print("is: ")
        print(grayscale_res)
    # if interpolating RGB
    if mode == 1:
        vertex_A = input("Introduce RGB color values for each vertex as a row. \n" + "Vertex A: ")
        vertex_B = input("\nVertex B: ")
        vertex_C = input("\nVertex C: ")
        vertex_colours = np.matrix(vertex_A + ' ; ' + vertex_B + ' ; ' + vertex_C)
        red_channel = vertex_colours[:, 0]
        green_channel = vertex_colours[:, 1]
        blue_channel = vertex_colours[:, 2]
        # transposing to get the right dimensions for the dot product for every channel.
        red_channel = np.ndarray.transpose(red_channel)
        green_channel = np.ndarray.transpose(green_channel)
        blue_channel = np.ndarray.transpose(blue_channel)
        # dot product and convert matrix of 1x1 to scalar using np.ndarray.item()
        red_interpolated = np.ndarray.item(MatrixVectorOperations.matrix_dot(red_channel, barycentricCoordinates))
        green_interpolated = np.ndarray.item(MatrixVectorOperations.matrix_dot(green_channel, barycentricCoordinates))
        blue_interpolated = np.ndarray.item(MatrixVectorOperations.matrix_dot(blue_channel, barycentricCoordinates))
        print("The final interpolated RGB value for the triangle is: ")
        print("(" + str(round(red_interpolated, 2)) + ", " + str(round(green_interpolated, 2)) + ", "
                  + str(round(blue_interpolated, 2)) + ")")




