from pylab import *

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=cm.hot)
C = contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
clabel(C, inline=1, fontsize=10)
xticks([]), yticks([])

text(-0.05, 1.05, " Contour Plot \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)

text(-0.05, .975, " Draw contour lines and filled contours ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)

savefig('../figures/contour.png', dpi=64)

