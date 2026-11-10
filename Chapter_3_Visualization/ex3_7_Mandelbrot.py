import numpy as np, pylab as pl

def mandelbrot(z,c):
    return z**2+c

x = np.linspace(-1.5, 1, 400)
y = np.linspace(1.5, -1.5, 400)

X,Y = np.meshgrid(x,y)

z = X + 1j*Y
z_values = np.zeros((len(z),len(z)), dtype=complex)

for i in range(len(z)):
    for j in range(len(z)):
        z0 = 0
        for k in range(100):
            z_prime = mandelbrot(z0,z[i,j])
            z0 = z_prime
            if np.sqrt(z0.real**2+z0.imag**2) >= 2:
                break
            z_values[i,j] = z0


pl.imshow(z_values.real, extent=[-2,2,-2,2])
pl.gray()
pl.show()
print(z_values)