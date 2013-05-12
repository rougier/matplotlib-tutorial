from pylab import *

plt.subplot(211)
gca().set_xticklabels([])
gca().set_yticklabels([])
#xticks([]), yticks([])

text(-0.05, 1.1, " Multiplot \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)
text(-0.05, .925, " Plot several plots at once ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)

plt.subplot(223)
gca().set_xticklabels([])
gca().set_yticklabels([])
#xticks([]), yticks([])

plt.subplot(224)
gca().set_xticklabels([])
gca().set_yticklabels([])
#xticks([]), yticks([])

plt.savefig('../figures/multiplot.png', dpi=64)
