import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, num = 1000)
y = np.sin(x)

plt.plot(x, y, 'g-')
plt.title("My first graph", fontdict={'fontsize' : 20})
plt.xlabel('x [rad]')
plt.ylabel('sin(x)')

plt.show()
