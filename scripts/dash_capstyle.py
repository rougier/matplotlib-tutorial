from pylab import *

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,0,1,1], frameon=False)

plot(np.arange(4), np.ones(4), color="blue", dashes=[15,15], linewidth=8, dash_capstyle = 'butt')

plot(5+np.arange(4), np.ones(4), color="blue", dashes=[15,15], linewidth=8, dash_capstyle = 'round')

plot(10+np.arange(4), np.ones(4), color="blue", dashes=[15,15], linewidth=8, dash_capstyle = 'projecting')

xlim(0,14)
xticks([]),yticks([])

savefig('../figures/dash_capstyle.png', dpi=dpi)
#show()
