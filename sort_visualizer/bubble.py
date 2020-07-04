import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from helper import is_sorted, plot

# Data for marker below bubble sort plot
MARKER = '^'    # Marker text
MARKER_Y = -5   # y-coordinate of marker in data coordinates
MARKER_SIZE = 15    # Font size of marker text
MARKER_WEIGHT = 'bold'  # Font weight of marker text
MARKER_COLOR = 'r'  # Color of marker text

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    """
    Function to visualize bubble sort.

    Parameters:
    array (arraylike): Array to be sorted.
    desc (bool): Sort in ascending order if True, else sort in descending order.
    visualize (bool): Generates visualization if True.
    sleep_time (float): Time in ms between frames.
    Other parameters are for the matplotlib plot.

    Returns:
    tuple: Tuple containing the sorted array and the time taken for sorting.
    """

    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    # Plotting initial state
    if(visualize == True):
        fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, xticks=[], yticks=[], color=color)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    sort_time = 0   # Time for sorting (excluding plotting)
    sorted_upto = -1    # Index upto which array_copy is sorted
    while(not is_sorted.is_sorted(array_copy, desc=desc)):
        for i in range(len(array_copy) - 2, sorted_upto, -1):
            start_time = time.time()
            # Sorting in ascending order
            if(desc == False):
                if(array_copy[i] > array_copy[i + 1]):
                    # Swapping array_copy[i] with array_copy[i + 1]
                    tmp = array_copy[i + 1]
                    array_copy[i + 1] = array_copy[i]
                    array_copy[i] = tmp
            # Sorting in descending order
            elif(desc == True):
                if(array_copy[i] < array_copy[i + 1]):
                    # Swapping array_copy[i] with array_copy[i + 1]
                    tmp = array_copy[i + 1]
                    array_copy[i + 1] = array_copy[i]
                    array_copy[i] = tmp
            stop_time = time.time()

            # Adding time taken for iteration to sort_time
            sort_time += (stop_time - start_time)

            # Plotting
            if(visualize == True):
                fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, xticks=[], yticks=[], color=color)
                ax.annotate(s=MARKER, xy=(i, 0), xytext=(i, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
                plt.show(block=False)
                plt.pause(sleep_time)
                plt.close()

        sorted_upto += 1

    return array_copy, sort_time
