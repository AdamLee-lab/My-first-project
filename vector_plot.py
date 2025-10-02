import numpy as np
import matplotlib.pyplot as plt
import math as m

# x=[0.1*i for i in range(0, 51)]
# y=[m.sin(i) for i in x]
# z=[m.cos(i) for i in x]

# plt.plot(x, y)
# # plt.show()
# plt.plot(x, z)
# plt.show()

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

# fig1, ax1 = plt.subplots()
# print(dir(ax1))

plt.quiver(X, Y, U, V, width=0.001, scale=20)
plt.streamplot(X, Y, U, V, broken_streamlines=False, linewidth=0.5, color='r')
plt.show()
