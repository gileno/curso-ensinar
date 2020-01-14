import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'r')
plt.show()
