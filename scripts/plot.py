from pylab import *

n = 256
X = np.linspace(0,2,n)
Y = np.sin(2*np.pi*X)

plt.plot (X, Y, lw=2, color='violet')
xlim(-0.2,2.2), xticks([])
ylim(-1.2,1.2), yticks([])

plt.text(-0.05, 1.05, " Regular Plot \n\n",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='x-large',
          bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
          transform = gca().transAxes)

plt.text(-0.05, .975, " Plot lines and/or markers ",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='medium',
          transform = gca().transAxes)

plt.savefig('../figures/plot.png', dpi=64)

