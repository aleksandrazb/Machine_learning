import numpy
matrix = numpy.matrix([[0, 4, -2], [-4, -3, 0], [9, 6, -3]])
print(matrix)
array = numpy.array([[0, 4, -2], [-4, -3, 0], [9, 6, -3]])
print(array)
print(matrix**-1)
print(numpy.linalg.inv(array))
print(array**-1)