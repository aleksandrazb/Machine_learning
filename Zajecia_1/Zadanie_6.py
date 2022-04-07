import numpy
X = numpy.array([[1, 2, 3], [1, 3, 6]])
y = numpy.array([[5, 6]]).T
print(X)
print(y)
array_result = (numpy.linalg.inv((X.T).dot(X))).dot(X.T).dot(y)
print(array_result)
X = numpy.matrix([[1, 2, 3], [1, 3, 6]])
y = numpy.matrix([[5], [6]])
print(X)
print(y)
matrix_result = (X.T * X)**-1 * X.T * y
print(matrix_result)