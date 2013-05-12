from pylab import *

fig =figure()
fig.subplots_adjust(bottom=0.025, left=0.025, top = 0.975, right=0.975)

subplot(2,1,1)
xticks([]), yticks([])

subplot(2,3,4)
xticks([]), yticks([])

subplot(2,3,5)
xticks([]), yticks([])

subplot(2,3,6)
xticks([]), yticks([])

savefig('../figures/multiplot_ex.png',dpi=48)
show()
