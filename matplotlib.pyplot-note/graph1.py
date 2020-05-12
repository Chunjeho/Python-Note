import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, num = 10000)
x1 = np.linspace(-20, 20, num = 10000)

y = np.zeros((10000), dtype = 'float64')
y = x/((x**2)+1)

y1 = np.zeros((10000), dtype = 'float64')
y1 = x*0.0

dx = np.diff(x)
dy = np.diff(y)
fp = np.divide(dy, dx)

plt.plot(x[0:9999],y[0:9999],'g',x1,y1,'k',x[0:9999],fp,'r')
plt.show()
