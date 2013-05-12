from pylab import *

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,0.1,1,.8], frameon=False)

for i in range(1,11):
    plot( [i,i], [0,1], lw=1.5 )
xlim(0,11)
xticks([]),yticks([])
savefig('../figures/color.png', dpi=dpi)
