import matplotlib
#matplotlib.use('Agg')
from pylab import *


def tickline():

    size = 512,32
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    ax = axes([0.05, 0, 0.9, 1], frameon=False)
    xlim(0,10), ylim(-1,1), yticks([])
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.plot(np.arange(11), np.zeros(11), color='none')
    return ax

ax = tickline()
ax.xaxis.set_major_locator(NullLocator())
savefig('../figures/ticks-NullLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(MultipleLocator(1.0))
savefig('../figures/ticks-MultipleLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(FixedLocator([0,2,8,9,10]))
savefig('../figures/ticks-FixedLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(IndexLocator(3,1))
savefig('../figures/ticks-IndexLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(LinearLocator(5))
savefig('../figures/ticks-LinearLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(LogLocator(2,[1.0]))
savefig('../figures/ticks-LogLocator.png', dpi=72)

ax = tickline()
ax.xaxis.set_major_locator(AutoLocator())
savefig('../figures/ticks-AutoLocator.png', dpi=72)
