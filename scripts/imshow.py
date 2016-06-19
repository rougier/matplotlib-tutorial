from pylab import *

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,8*n)
y = np.linspace(-3,3,6*n)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
imshow(Z,interpolation='nearest',cmap='bone', origin='lower')
xticks([]), yticks([])

plt.text(-0.05, 1.05, " Imshow \n\n",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='x-large',
          bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
          transform = gca().transAxes)

plt.text(-0.05, .975, " Display an image to current axes ",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='medium',
          transform = gca().transAxes)

#plt.savefig('../figures/imshow.png', dpi=64)
plt.show()
