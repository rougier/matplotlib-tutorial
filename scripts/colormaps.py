from pylab import *

def colormap(cmap,filename):
    n = 512
    Z = np.linspace(0,1,n,endpoint=True).reshape((1,n))
    size = 512,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.,0.,1.,1.], frameon=False)
    xticks([]), yticks([])
    imshow(Z,aspect='auto',cmap=cmap,origin="lower")
    savefig( "../figures/cmap-%s.png" % filename, dpi=dpi )



cmaps = [m for m in cm.datad if not m.endswith("_r")]
cmaps.sort()

#print """
#.. list-table::
#   :widths: 10 30 50
#   :header-rows: 1
#
#   * - Name
#     - Description
#     - Appearance
#
#"""

for i in range(len(cmaps)):
    name = cmaps[i]
    filename = name
    if name == 'Spectral':
        filename = 'spectral-2'
    colormap(name,filename)
    #print "   * - %s" % name
    #print "     - " 
    #print "     - .. image:: figures/cmap-%s.png" % filename
    #print

