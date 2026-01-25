import numpy
number = [12, 15, 14, 10, 8, 11, 13, 12, 16, 14, 9, 11, 15, 14, 10, 12]
x = numpy.std(number)

if 0 < x <= 5:
    x = "Low standard deviation"
elif 5 < x <= 15:
    x = "Medium standard deviation"
else:
    x = "High standard deviation"
print(x)