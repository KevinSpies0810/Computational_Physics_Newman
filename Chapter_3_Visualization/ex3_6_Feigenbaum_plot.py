import numpy as np, pylab as pl

def feigenbaum(x,r):
    return r*x*(1-x)

result = []
j = 1.01
r_values = []

while j <= 4:
    start = 0.5
    for i in range(1000):
        step = feigenbaum(start,j)
        if i >= 900:
            result.append(start)
            r_values.append(j)
        start = step
    j += 0.01

pl.plot(r_values,result,"k.", markersize=0.2)
pl.xlabel("r")
pl.ylabel("$x_n$",rotation=0)
pl.show()