from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize = (8, 8))


class Plot():

    global x
    x = symbols('x', real=True)

    def __init__(self, original_line):
        self.original_line = original_line

    def show(self):

        reflection_line = self.original_line.reflection_line()
        m3 = reflection_line.m
        b3 = reflection_line.b

        b2 = self.original_line.b
        m2 = self.original_line.m

        # Parabole
        x1 = np.linspace(-20, 20, 100)
        y1 = 0.1 * x1 ** 2

        expr = m3*x + b3 - 0.1 * x**2
        sol = solve(expr, x)

        y_min = m3*float(sol[0]) + b3
        y_max = m3*float(sol[1]) + b3

        # Reflection line
        x3 = np.linspace(float(sol[0]), float(sol[1]), 100)
        y3 = m3*x3 + b3

        if m2 == None:
            plt.vlines(x = b2, 
                       ymin = y_min if b2 <=0 else y_max, 
                       ymax = 40, 
                       color='green')

        else:

            x2 = np.linspace(float(sol[0]), float(sol[1]), 100)
            y2 = m2*x2 + b2

            plt.plot(x2, y2, color='green')
            

        plt.vlines(x = 0, ymin = 0, ymax = 40, color='black')
        plt.hlines(y = 0, xmin = -20, xmax = 20, color='black')
        
        plt.plot(x1, y1)
        plt.plot(x3, y3, color='green')
        plt.scatter(0, 1 / (4*0.1))
        plt.show()

    def animation(self):

        reflection_line = self.original_line.reflection_line()
        m3 = reflection_line.m
        b3 = reflection_line.b

        b2 = self.original_line.b
        m2 = self.original_line.m
        
        fig, ax = plt.subplots()
        xdata, ydata = [], []
        ln, = ax.plot([], [], 'green')

        def init():
            ax.set_xlim(-20, 20)
            ax.set_ylim(0, 40)
            return ln,

        def update(frame):

            x_axis = np.linspace(frame, frame + 5, 160)
            xdata.append(x_axis)
            ydata.append(m3 * x_axis + b3)
            ln.set_data(xdata, ydata)
            return ln,
    
        x1 = np.linspace(-20, 20, 100)
        y1 = 0.1 * x1 ** 2
        plt.plot(x1, y1)

        ani = FuncAnimation(fig, update, frames=np.linspace(-20, 20, 20),
                            init_func=init, blit=False)
        plt.show()
