import matplotlib.pyplot as plt
from scipy import stats

x = [80,70, 60,50,40,30,20,10,0,90,100,110,120,130,140,150,160,170,180,190]
y = [2,5,7,8,1,20,4,9,6,15,11,10,3,4,25,30,8,4,2,7]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()