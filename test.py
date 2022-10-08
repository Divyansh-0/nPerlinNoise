import numpy as np
from matplotlib import pyplot
from src import Noise

mul, res = 1, 8
x, y = 128 * mul, 128 * mul
m = 8
n = Noise(frequency=(8*m), waveLength=(128*m), octaves=8)
mesh = np.meshgrid(np.linspace(0, x, x * res), np.linspace(0, y, y * res))


def getH():
    return n(*mesh, checkFormat=True)


h = getH()
try:
    fig, ax = pyplot.subplots()
    ax.imshow(h, cmap='gray')
    pyplot.show()
except NameError:
    pass
