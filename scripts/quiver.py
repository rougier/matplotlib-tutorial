from pylab import *

n = 8
X,Y = np.mgrid[0:n,0:n]
T = np.arctan2(Y-n/2.0, X-n/2.0)
R = 10+np.sqrt((Y-n/2.0)**2+(X-n/2.0)**2)
U,V = R*np.cos(T), R*np.sin(T)

quiver(X,Y,U,V,R, alpha=.5)
quiver(X,Y,U,V, edgecolor='k', facecolor='None', linewidth=.5)

xlim(-1,n), xticks([])
ylim(-1,n), yticks([])

text(-0.05, 1.05, " Quiver Plot \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)

text(-0.05, .975, " Plot a 2-D field of arrows ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)

savefig('../figures/quiver.png', dpi=64)

