import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.subplot(1,2,1)
plt.plot(x, x**2)
plt.subplot(1,2,2)
plt.plot(x, np.sqrt(x))
plt.show()