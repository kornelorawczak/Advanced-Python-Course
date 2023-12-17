import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1,2)


X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100
axs[0].scatter(X_data, Y_data, marker="*")

years = [2006 + x for x in range(16)]
weights = np.random.random(16) * 100
axs[1].plot(years, weights, lw=3, linestyle="--")

# ax = plt.axes(projection="3d")
#
# X = np.arange(0,50,0.1)
# Y = np.random.random(500) * 100
# Z = np.arange(0,50,0.1)
#
# ax.scatter(X,Y,Z)

plt.show()
