import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
    _x = [c for c in range(1,100)]
    xs = np.array(_x)
    ys = (((-1)**(xs-1))*(2**xs))/(xs*np.log(2))

    plt.title("Heart-Bit")
    plt.plot(xs,ys, color="blue")
    plt.savefig('HeartBit.png')
    plt.show()
