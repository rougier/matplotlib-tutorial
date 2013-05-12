from pylab import *

figure(figsize=(8,5), dpi=80)
subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X, S, color="red", linewidth=2.5, linestyle="-")

xlim(X.min()*1.1, X.max()*1.1)
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

ylim(C.min()*1.1,C.max()*1.1)
yticks([-1, 0, +1])

# savefig("../figures/exercice_5.png",dpi=72)
show()
