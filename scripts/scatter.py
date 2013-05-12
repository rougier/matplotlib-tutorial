from pylab import *

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

T = np.arctan2(Y,X)
scatter(X,Y,s=75,c=T,alpha=.5)
xlim(-1.5,1.5), xticks([])
ylim(-1.5,1.5), yticks([])

text(-0.05, 1.05, " Scatter Plot \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)

text(-0.05, .975, " Make a scatter plot of x versus y ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)

plt.savefig('../figures/scatter.png', dpi=64)

