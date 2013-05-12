from pylab import *

n = 20
X = np.ones(n)
X[-1] *= 2
pie(X, explode=X*.05, colors = ['%f' % (i/float(n)) for i in range(n)])

fig = gcf()
w,h = fig.get_figwidth(), fig.get_figheight()
r = h/float(w)

xlim(-1.5,1.5)
ylim(-1.5*r,1.5*r)
xticks([]), plt.yticks([])

plt.text(-0.05, 1.05, " Pie Chart \n\n",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='x-large',
          bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
          transform = gca().transAxes)

plt.text(-0.05, .975, " Make a pie chart of an array ",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='medium',
          transform = gca().transAxes)

plt.savefig('../figures/pie.png', dpi=64)
