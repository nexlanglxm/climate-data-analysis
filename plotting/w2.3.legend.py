import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 *x
noise = np.random.normal(0.0, 1.0, (len(x)))

plt.plot(x, y + noise,'b.', label = 'Actual data')
plt.plot(x, y,'g-', label = 'Fitted model')


plt.title("Avg speed vs DoT")
plt.xlabel('Avg speed')
plt.ylabel('Distance covered')
plt.legend()

plt.show()