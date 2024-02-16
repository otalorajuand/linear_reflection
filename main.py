from line import Line
from plot import Plot


# Plotting

if __name__ == "__main__":

    intercept = 8
    slope = -0.18

    line = Line(m = slope, b = intercept)
    plot = Plot(line)
    plot.show()