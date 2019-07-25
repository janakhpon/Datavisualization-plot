import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019]
pops = [0.00, 1.92, 2.14, 2.22, 2.37, 2.34, 2.26, 2.10,  1.71, 1.21, 1.25, 0.94, 0.67, 0.81, 0.69, 0.64, 0.61, 0.63]
deaths = [0.00, 0.77, 0.68, 0.54, 0.38, 0.23, 0.11, 0.02, 0.05, 0.12, 0.18, 0.25, 0.31, 0.35, 0.37, 0.38]
plt.plot(years, pops, '--', color = (255/255, 100/255, 100/255))
plt.plot(years, deaths, color = (255/255, 50/255, 80/255))

plt.ylabel("Population percentage rate")
plt.xlabel("Population Growth")
plt.title("Myanmar Population Survey")
plt.show()


















