import numpy
A = numpy.matrix([[0, 4, -2], [-4, -3, 0]])
print(A)
B = numpy.matrix([[0, 1], [1, -1], [2, 3]])
print(B)
x = numpy.array([[2], [1], [0]])
print(x)
Ax = A * x
print(Ax)
AB = A * B
print(AB)
detAB = numpy.linalg.det(AB)
print(detAB)
ABt_min_BtAt = AB.T - (B.T * A.T)
print(ABt_min_BtAt)