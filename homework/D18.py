import matplotlib.pyplot as plt
import numpy as np

plt.figure()
a = np.arange(0, 360)
b = np.cos(a * np.pi/90.0)

plt.plot(a,b)
plt.xlim(-30, 390)
plt.ylim(-1.5, 1.5)

plt.xlabel('axis-X')
plt.ylabel('axis-Y')
plt.title('Cos')

plt.savefig("filename.png",dpi=300,format="png")

plt.figure()
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
plt.rcParams['axes.facecolor'] = 'lightcyan'
plt.scatter(X, Y, c='mediumpurple')
plt.title("Scatter plot")

plt.show()