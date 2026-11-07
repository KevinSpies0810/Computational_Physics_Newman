import pylab as plt, numpy as np

def deltoid_curve():
    theta = np.linspace(0,2*np.pi,100)

    x = 2*np.cos(theta)+np.cos(2*theta)
    y = 2*np.sin(theta)-np.sin(2*theta)

    plt.plot(x,y)
    plt.title("Deltoid Curve")
    plt.grid()
    plt.xlabel(r"$2\cdot\cos(\theta)+\cos(2\theta)$")
    plt.ylabel(r"$2\cdot\sin(\theta)-\sin(2\cdot\theta)$")
    plt.show()

def polar_plot():
    theta = np.linspace(0,2*np.pi,100)

    r = theta**2

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    plt.plot(x,y)
    plt.grid()
    plt.axis("equal")
    plt.title("Galilean Sprial")
    plt.show()

def feys_function():
    theta = np.linspace(0,24*np.pi,10000)
    r = np.exp(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5

    x = r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x,y)
    plt.show()

feys_function()