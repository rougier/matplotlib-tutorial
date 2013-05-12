from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2,2)
plt.xticks([]), plt.yticks([]), 
ax.set_zticks([])

ax.text2D(0.05, .95, " 3D plots \n\n",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='x-large',
          bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
          transform = gca().transAxes)

ax.text2D(0.05, .89, " Plot 2D or 3D data",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='medium',
          transform = gca().transAxes)

plt.savefig('../figures/plot3d.png', dpi=64)
plt.show()
