from statistics import mean
import numpy
matrix = numpy.arange(1, 51 , 1).reshape(5, 10)
elements = sum(len(row) for row in matrix)
print(elements)
rows = len(matrix)
print(rows)
columns = len(matrix[0])
print(columns)
avr_rows = numpy.mean(matrix, axis = 1)
print(avr_rows)
avr_columns = numpy.mean(matrix, axis = 0)
print(avr_columns)
third_column = matrix[:, 2]
print(third_column)
fourth_row = matrix[3]
print(fourth_row)