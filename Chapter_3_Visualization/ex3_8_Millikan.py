import numpy as np, pylab as pl

data = np.loadtxt("cpresources/millikan.txt")
x = data[:,0]
y = data[:,1]
N = len(x)

E_x = 1/N * (sum(x))
E_y = 1/N * (sum(y))
E_xx = 1/N * (sum(x**2))
E_xy = 1/N * (sum(x*y)) 

m = (E_xy-E_x*E_y)/(E_xx-E_x**2)
c = (E_xx*E_y-E_x*E_xy)/(E_xx-E_x**2)

best_fit = []
for element in data:
    best_fit.append(m*element[0]+c)

pl.plot(x,y, "ko")
pl.plot(x,best_fit)
pl.xlabel("f [Hz]")
pl.ylabel("Voltage [V]")
# pl.show()

print(f"m = {m:.2f}, c = {c:.2f}")

e = 1.602e-19

h_calculated = m*e
h_literature = 6.62607015e-34
print(f"h berechnet = {h_calculated}, h Literatur = {h_literature}")
print(f"{100-(h_calculated/h_literature)*100:.5f}% Abweichung")

