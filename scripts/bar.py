from pylab import *

n = 16
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
xlim(-.5,n), xticks([])
ylim(-1,+1), yticks([])

text(-0.05, 1.05, " Bar Plot \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)

text(-0.05, .975, " Make a bar plot with rectangles ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)

savefig('../figures/bar.png', dpi=64)

