import numpy as np, pylab as pl

data = np.loadtxt("cpresources/stm.txt",float)

pl.imshow(data,origin="lower")
pl.gray()
pl.colorbar()
pl.title("STM meaurement of the (111)-Surface of Si")
pl.show()