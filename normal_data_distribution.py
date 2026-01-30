import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(9.0, 2.0, 90000)

plt.hist(x, 100)
plt.show()