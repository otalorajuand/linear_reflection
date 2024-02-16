from line import Line
from plot import Plot


# Plotting

if __name__ == "__main__":

    b = 30
    m = 2

    original_line = Line(m, b)

    plot = Plot(original_line)
    plot.show()