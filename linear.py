import matplotlib.pyplot as plt
from scipy import stats

x = [7, 0, 14, 5, 20, 6, 9, 11, 3, 12, 15, 8, 4]
y = [1,3,2,3,6,7,5,9,4,8,9,10,6]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()