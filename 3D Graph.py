# Importing Libraries
from mpl_toolkits import mplot3d
import numpy as  np
import matplotlib.pyplot as plt


# defining surface and axes
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)
fig = plt.figure()

#syntax for 3d plotting
ax = plt.axes(projection = '3d')


#syntax for plotting
ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'green')
ax.set_title('3D Image')
plt.show