import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):

    x_axis = np.linspace(frame, frame + 0.3, 40)
    xdata.append(x_axis)
    ydata.append(0.5 * x_axis)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 80),
                    init_func=init, blit=False)
plt.show()