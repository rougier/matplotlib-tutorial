import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,5),dpi=72)
fig.patch.set_alpha(0.0)
axes = plt.subplot(111)

n = 5
Z = np.zeros((n,4))
X = np.linspace(0,2,n,endpoint=True)
Y = np.random.random((n,4))
plt.boxplot(Y)

#plt.xlim(-0.2,4.2)
#plt.ylim(-1.2,1.2)
plt.xticks([]), plt.yticks([])

plt.text(-0.05, 1.05, " Box Plot \n\n",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='x-large',
          bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
          transform = axes.transAxes)

plt.text(-0.05, .95, " Make a box and whisker plot ",
          horizontalalignment='left',
          verticalalignment='top',
          family='Lint McCree Intl BB',
          size='medium',
          transform = axes.transAxes)

plt.savefig('../figures/boxplot.png', dpi=64)
plt.show()
