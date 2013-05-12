from pylab import *

figure(figsize=(8,5), dpi=80)
subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X, S, color="red", linewidth=2.5, linestyle="-")

xlim(-4.0,4.0)
xticks(np.linspace(-4,4,9,endpoint=True))

ylim(-1.0,1.0)
yticks(np.linspace(-1,1,5,endpoint=True))

#savefig("../figures/exercice_3.png",dpi=72)
show()
