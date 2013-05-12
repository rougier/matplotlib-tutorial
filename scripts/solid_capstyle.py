from pylab import *

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,0,1,1], frameon=False)

plot(np.arange(4), np.ones(4), color="blue", linewidth=8, solid_capstyle = 'butt')

plot(5+np.arange(4), np.ones(4), color="blue", linewidth=8, solid_capstyle = 'round')

plot(10+np.arange(4), np.ones(4), color="blue", linewidth=8, solid_capstyle = 'projecting')

xlim(0,14)
xticks([]),yticks([])

savefig('../figures/solid_capstyle.png', dpi=dpi)
#show()
