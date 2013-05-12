from pylab import *

n = 20
Z = np.ones(n)
Z[-1] *= 2

axes([0.025,0.025,0.95,0.95])

pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
gca().set_aspect('equal')
xticks([]), plt.yticks([])

# savefig('../figures/pie_ex.png',dpi=48)
show()
