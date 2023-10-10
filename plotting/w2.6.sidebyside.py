import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 100000)
plt.subplot(2, 1, 2) #the code in this row denotes the (row column, index) of the plot
plt.hist(x, bins=80)

x = np.random.uniform(-4.0, 1.0, 1000)
plt.subplot(2, 1, 1)
plt.hist(x)

plt.show()