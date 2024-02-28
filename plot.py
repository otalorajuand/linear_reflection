from pyexpat.errors import XML_ERROR_INCOMPLETE_PE
from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(8, 8))


class Plot():

    global x
    x = symbols('x', real=True)

    def __init__(self, original_line, reflection_line, parabole):
        self.original_line = original_line
        self.parabole = parabole
        self.reflection_line = reflection_line

    def plot_reflected_line(self):

        a = self.parabole.a

        m3 = self.reflection_line.m
        b3 = self.reflection_line.b

        expr = m3 * x + b3 - a * x**2
        sol = solve(expr, x)

        # Reflection line
        x3 = np.linspace(float(sol[0]), float(sol[1]), 100)
        y3 = m3 * x3 + b3

        plt.plot(x3, y3, color='green')

    def plot_original_line(self):

        a = self.parabole.a

        m3 = self.reflection_line.m
        b3 = self.reflection_line.b

        m2 = self.original_line.m
        b2 = self.original_line.b

        expr = m3 * x + b3 - a * x**2
        sol = solve(expr, x)

        y_min = m3 * float(sol[0]) + b3
        y_max = m3 * float(sol[1]) + b3

        # Reflection line
        x3 = np.linspace(float(sol[0]), float(sol[1]), 100)
        y3 = m3 * x3 + b3

        if m2 is None:
            plt.vlines(x=b2,
                       ymin=y_min if b2 <= 0 else y_max,
                       ymax=40,
                       color='green')

        else:

            x2 = np.linspace(float(sol[0]), float(sol[1]), 100)
            y2 = m2 * x2 + b2
            plt.plot(x2, y2, color='green')

    def plot_parabole(self):

        x1 = np.linspace(-20, 20, 100)
        y1 = self.parabole.a * x1 ** 2

        plt.plot(x1, y1)
        plt.scatter(0, 1 / (4 * self.parabole.a))

    def show(self):

        self.plot_parabole()
        self.plot_original_line()
        self.plot_reflected_line()

        plt.vlines(x=0, ymin=0, ymax=40, color='black')
        plt.hlines(y=0, xmin=-20, xmax=20, color='black')
        plt.show()

    def animation(self):

        a = self.parabole.a

        m3 = self.reflection_line.m
        b3 = self.reflection_line.b

        b2 = self.original_line.b

        expr = m3 * x + b3 - a * x**2
        sol = solve(expr, x)

        x_min = float(sol[0])
        x_max = float(sol[1])

        y_min = float(m3 * x_min + b3)
        y_max = float(m3 * x_max + b3)

        fig, ax = plt.subplots()
        xdata, ydata = [], []
        ln, = ax.plot([], [], 'green')

        self.plot_parabole()

        def init():
            ax.set_xlim(-20, 20)
            ax.set_ylim(0, 40)
            return ln,

        

        if m3 > 0:

            def update_1(frame):

                if frame > b2:

                    y_axis = np.linspace(frame, frame)
                    xdata.append(np.linspace(b2, b2))
                    ydata.append(y_axis)
                    ln.set_data(xdata, ydata)

                elif frame <= b2:
                    x_axis = np.linspace(frame, frame)
                    xdata.append(x_axis)
                    ydata.append(m3 * x_axis + b3)
                    ln.set_data(xdata, ydata)
                else:
                    pass
                return ln,
        
            frames = np.concatenate(
                [np.linspace(40, float(y_max), 680), np.linspace(b2 - 0.1, x_min, 120)])
        else:

            def update_1(frame):

                if frame < b2:

                    y_axis = np.linspace(frame, frame)
                    xdata.append(np.linspace(b2, b2))
                    ydata.append(-y_axis)
                    ln.set_data(xdata, ydata)

                elif frame >= b2:
                    x_axis = np.linspace(frame, frame)
                    xdata.append(x_axis)
                    ydata.append(m3 * x_axis + b3)
                    ln.set_data(xdata, ydata)
                else:
                    pass
                return ln,
        
            print(f"y_min: {y_min}, y_max: {y_max}, x_min: {x_min}, x_max: {x_max}")

            frames = np.concatenate(
                [np.linspace(-40, float(y_min), 680), np.linspace(x_max, b2 - 0.1, 120)])

        ani = FuncAnimation(fig, update_1,
                            frames=frames,
                            init_func=init,
                            blit=True,
                            repeat=False,
                            interval=3)

        plt.show()
