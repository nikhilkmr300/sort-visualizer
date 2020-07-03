import numpy as np
import matplotlib.pyplot as plt

def bar(array, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    x = np.array(range(len(array)))

    # Plotting
    fig, ax = plt.subplots(1, 1)
    ax.bar(x, array, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    return fig, ax
