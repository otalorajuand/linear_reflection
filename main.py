from line import Line
from plot import Plot


# Plotting

if __name__ == "__main__":

    b2 = 15
    m2 = None

    m1 = 0.2 * b2
    b1 = 0.1*(b2**2) - m1*b2
    original_line = Line(m2, b2)
    wall = Line(m1, b1)

    plot = Plot(original_line, wall)
    plot.show()