import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    x = np.linspace(-20, 20, num = 10000)
    x1 = np.linspace(-20, 20, num = 10000)

    y = np.zeros((10000), dtype = 'float64')
    y = x/((x**2)+1)

    y1 = np.zeros((10000), dtype = 'float64')
    y1 = x*0.0

    dx = np.diff(x)
    dy = np.diff(y)
    fp = np.divide(dy, dx)

    plt.plot(x1,y1,'k', label='f(x) = 0')
    plt.plot(x[0:10000],y[0:10000],'g', label="f(x)")
    plt.plot(x[0:9999],fp,'r', label="f'(x)")

    plt.title('$\mathit{f(x)=}$' + r'$\frac{x}{x^{2}+1}$')
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.legend()
    plt.tight_layout()
    plt.savefig('Graph1.png')
    plt.show()
