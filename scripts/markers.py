from pylab import *

def marker(m,name):
    size = 256,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0,0,1,1],frameon=False)
    X = np.arange(11)
    Y = np.ones(11)
    plot(X,Y,color='w', lw=1, marker=m, ms=10, mfc=(.75,.75,1,1), mec=(0,0,1,1))
    xlim(0,10)
    xticks([]), yticks([])
    print '../figures/marker-%s.png' % name
    savefig('../figures/marker-%s.png' % name, dpi=dpi)

#print"""
#.. list-table::
#   :widths: 15 30 50
#   :header-rows: 1
#
#   * - Symbol
#     - Description
#     - Appearance
#"""
for m in [0,1,2,3,4,5,6,7,'o','h','_','1','2','3','4','8','p',
           '^','v','<','>','|','d',',','+','s','*','|','x']:
    if type(m) is int:
        marker(m, 'i%d' % m)
        #print "   * - %d" % m
        #print "     - "
        #print "     - .. image:: figures/marker-i%d.png" % m
    else:
        marker(m,m)
        #print "   * - ``%s``" %  m
        #print "     - "
        #print "     - .. image:: figures/marker-%s.png" % m

marker('D', 'dd')
marker('H', 'hh')
marker('.', 'dot')
marker(r"$\sqrt{2}$", "latex")
#print "   * - ``r'$\sqrt{2}$'``"
#print "     - "
#print "     - .. image:: figures/marker-latex.png"
#print
