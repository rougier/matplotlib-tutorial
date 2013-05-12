from pylab import *

n = 8
X,Y = np.mgrid[0:n,0:n]
T = np.arctan2(Y-n/2.0, X-n/2.0)
R = 10+np.sqrt((Y-n/2.0)**2+(X-n/2.0)**2)
U,V = R*np.cos(T), R*np.sin(T)

axes([0.025,0.025,0.95,0.95])
quiver(X,Y,U,V,R, alpha=.5)
quiver(X,Y,U,V, edgecolor='k', facecolor='None', linewidth=.5)

xlim(-1,n), xticks([])
ylim(-1,n), yticks([])

# savefig('../figures/quiver_ex.png',dpi=48)
show()
