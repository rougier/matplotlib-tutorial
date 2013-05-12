from pylab import *

figure(figsize=(8,5), dpi=80)
subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X+.1, C, color="blue", linewidth=2.5, linestyle="-",alpha=.15)
plot(X, S, color="red", linewidth=2.5, linestyle="-")

xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1,C.max()*1.1)

# savefig("../figures/exercice_4.png",dpi=72)
show()
