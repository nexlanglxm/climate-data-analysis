import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 *x
noise = np.random.normal(0.0, 1.0, (len(x)))

plt.plot(x, y)
plt.plot(x, y + noise, 'g-')
plt.ylabel('random numbers')
plt.show()