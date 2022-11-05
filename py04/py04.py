#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(0, 10, 0.1)
y = np.sin(x)
ax.plot(x, y, marker=".")
plt.show()
