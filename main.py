from line import Line
from plot import Plot


# Plotting

if __name__ == "__main__":

    b2 = 30
    m2 = 2

    m1 = -2
    b1 = -10

    original_line = Line(m2, b2)
    wall = Line(m1, b1)

    plot = Plot(original_line, wall)
    plot.show()