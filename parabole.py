import matplotlib.pyplot as plt
import numpy as np

class Parabole():

    def __init__(self, a):
        self.a = a

    def plot(self):
         
        x1 = np.linspace(-20, 20, 100)
        y1 = self.a * x1 ** 2

        plt.plot(x1, y1)
        plt.scatter(0, 1 / (4 * self.a))

