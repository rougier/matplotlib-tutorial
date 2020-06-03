import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5), dpi=80)
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X+.1, C, color="blue", linewidth=2.5, linestyle="-",alpha=.15)
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1,C.max()*1.1)

# savefig("../figures/exercice_4.png",dpi=72)
plt.show()()
