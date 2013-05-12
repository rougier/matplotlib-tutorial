from pylab import *

def linestyle(ls,name):
    size = 256,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0,0,1,1],frameon=False)
    X = np.arange(11)
    Y = np.ones(11)
    plot(X,Y,ls,color=(.0,.0,1,1), lw=3, ms=10, mfc=(.75,.75,1,1), mec=(0,0,1,1))
    xlim(0,10)
    xticks([]), yticks([])
    print'../figures/linestyle-%s.png' % name
    savefig('../figures/linestyle-%s.png' % name, dpi=dpi)

for ls in ['-','--',':',',','o','^','v','<','>','s',
           '+','x','d','1','2','3','4','h','p','|','_']:
    linestyle(ls,ls)
linestyle('D', 'dd')
linestyle('H', 'hh')
linestyle('.', 'dot')
linestyle('-.', '-dot')
