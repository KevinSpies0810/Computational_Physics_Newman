from matplotlib import pylab as py
import numpy as np

data = np.loadtxt("cpresources/sunspots.txt",dtype=float)
xvalues = data[:1001,0]/12+1749
yvalues = data[:1001,1]

x_average_values = xvalues[5:-5]

def running_average(data):
    y_data = data[:1001,1]
    averages = []
    for i in range(5,len(y_data)-5):
        average = 1/11*np.sum(y_data[i-5:i+6])
        averages.append(average)
    return averages
        

py.plot(xvalues,yvalues,"-")
py.plot(x_average_values,running_average(data),"r")
py.show()
