import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

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

def simulate_function_values(a, b, n, num_simulations):
    x = np.linspace(a, b, n)
    y = func(x)

    results = np.random.choice(y, size=num_simulations)

    return results

def main():
    n = 3  # порядковий номер в журналі
    a = 1
    b = n + 3
    num_simulations = 1000

    results = simulate_function_values(a, b, 100, num_simulations)

    # Analyze the results.
    max_result = func(b)
    frequencies = [results.count(value) for value in np.arange(0, max_result, 0.01)]

    # Visualize the results.
    x_values = np.arange(0, max_result, 0.01)
    data = [go.Bar(x=x_values, y=frequencies, name='Function')]

    x_axis_config = {'title': 'Result', 'dtick': 0.1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = go.Layout(title=f'Results of simulating function f(x) = sinc(2x - 1), sinc(x) = sin(x)/x, ∀N ∈ N, N = {n}',
                          xaxis=x_axis_config, yaxis=y_axis_config)

    fig = go.Figure(data=data, layout=my_layout)
    plot(fig, filename='function_simulation.html')

if __name__ == '__main__':
    main()