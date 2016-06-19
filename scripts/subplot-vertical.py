from pylab import *

subplot(1,2,1)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,1)',ha='center',va='center',size=24,alpha=.5)

subplot(1,2,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,2)',ha='center',va='center',size=24,alpha=.5)

# plt.savefig('../figures/subplot-vertical.png', dpi=64)
show()
