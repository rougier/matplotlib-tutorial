# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = 16
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
plt.xlim(-.5,n), plt.xticks([])
plt.ylim(-1,+1), plt.yticks([])

plt.text(-0.05, 1.05, " Bar Plot \n\n",
         horizontalalignment='left',
         verticalalignment='top',
         family='Lint McCree Intl BB',
         size='x-large',
         bbox=dict(facecolor='white', alpha=1.0, width=375, height=65),
         transform = plt.gca().transAxes)

plt.text(-0.05, .975, " Make a bar plot with rectangles ",
         horizontalalignment='left',
         verticalalignment='top',
         family='Lint McCree Intl BB',
         size='medium',
         transform = plt.gca().transAxes)

# plt.savefig('../figures/bar.png', dpi=64)
plt.show()

