from pylab import *

plt.subplot(111,polar=True)

N = 20
theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
bars = bar(theta, radii, width=width, bottom=0.0)
for r,bar in zip(radii, bars):
    bar.set_facecolor( cm.jet(r/10.))
    bar.set_alpha(0.5)
gca().set_xticklabels([])
gca().set_yticklabels([])

text(-0.2, 1.05, " Polar Axis \n\n",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='x-large',
      bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
      transform = gca().transAxes)
text(-0.2, .975, " Plot anything using polar axis ",
      horizontalalignment='left',
      verticalalignment='top',
      family='Lint McCree Intl BB',
      size='medium',
      transform = gca().transAxes)
savefig('../figures/polar.png', dpi=64)

