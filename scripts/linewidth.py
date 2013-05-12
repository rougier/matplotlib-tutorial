from pylab import *

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,.1,1,.8], frameon=False)

for i in range(1,11):
    plot( [i,i], [0,1], color='b', lw=i/2. )

xlim(0,11),ylim(0,1)
xticks([]),yticks([])
savefig('../figures/linewidth.png', dpi=dpi)

