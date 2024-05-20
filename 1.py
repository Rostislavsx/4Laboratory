import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    """
    Calculate sinc function values for passed array of arguments
    """
    return np.where(x == 0, 1, np.sin(x) / x)

def func(x):
    """
    Calculate function values for passed array of arguments
    """
    return sinc(2 * x - 1)

def tabulate(a, b, n):
    x = np.linspace(a, b, n)
    y = func(x)
    return {'x': x, 'y': y}

def main():
    res = tabulate(0, 1, 1000)

    plt.plot(res['x'], res['y'])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()