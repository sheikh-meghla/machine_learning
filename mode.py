from scipy import stats
number = [1,5, 10, 15, 20, 25, 30, 35, 5, 5, 6, 40, 45, 50, 55, 60, 65, 70, 75]
x = stats.mode(number)
print(x)