import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, num = 500)
x1 = np.linspace(-20, 20, num = 500)

y = np.zeros((500), dtype = 'float64')
y = x/(x**2+1)

y1 = np.zeros((500), dtype = 'float64')
y1 = x*0.0

plt.plot(x,y,'g',x1,y1,'r')
plt.show()
