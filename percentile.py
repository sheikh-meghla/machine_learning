import numpy
number = [12, 15, 14, 10, 8, 11, 13, 12, 16, 14, 9, 11, 15, 14, 10, 12, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
x = numpy.percentile(number, 50)
print(x)