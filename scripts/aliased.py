from pylab import *

size = 128,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,0,1,1], frameon=False)

rcParams['text.antialiased'] = False
text(0.5,0.5,"Aliased",ha='center',va='center')

plt.xlim(0,1),plt.ylim(0,1),
plt.xticks([]),plt.yticks([])

savefig('../figures/aliased.png', dpi=dpi)
