import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.axes([0.1, 0.1, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.1,0.1,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.2, 0.2, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.2,0.2,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.3, 0.3, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.3,0.3,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.4, 0.4, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.4,0.4,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.figure()
n = 12
X = np.arange(12)

Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
for x, y in zip(X,Y1):
    plt.text(x, y+0.05, '%.2f' %y, ha='center', va='bottom')

plt.bar(X, -Y2, facecolor='pink', edgecolor='white')
for x, y in zip(X, Y2):
    plt.text(x, -y-0.15,'%.2f' %-y, ha='center', va='bottom')




plt.ylim(-1.25, 1.25)


# print(Y1, Y2)



plt.show()