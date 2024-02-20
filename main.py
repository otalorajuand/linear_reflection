from line import Line
from plot import Plot
from parabole import Parabole


# Plotting

if __name__ == "__main__":

    intercept = 8
    slope = -0.18

    parabole = Parabole(0.1)
    line = Line(m = slope, b = intercept)
    plot = Plot(line, parabole)
    #plot.show()
    #plot.show()