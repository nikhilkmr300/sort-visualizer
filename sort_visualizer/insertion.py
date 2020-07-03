import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from helper import is_sorted, plot

# Data for marker below insertion sort plot
MARKER = '^'    # Marker text
MARKER_Y = -5   # y-coordinate of marker in data coordinates
MARKER_SIZE = 15    # Font size of marker text
MARKER_WEIGHT = 'bold'  # Font weight of marker text
MARKER_COLOR = 'r'  # Color of marker text

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    # Plotting initial state
    if(visualize == True):
        fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, xticks=[], yticks=[], color=color)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    sort_time = 0   # Time for sorting (excluding plotting)
    for i in range(1, len(array_copy)):
        start_time = time.time()
        j = i - 1
        element = array_copy[i]
        stop_time = time.time()
        # Adding time taken for initialization to sort_time
        sort_time += (stop_time - start_time)
        while(j >= 0):
            # Plotting
            if(visualize == True):
                fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, xticks=[], yticks=[], color=color)
                ax.annotate(s=MARKER, xy=(j, 0), xytext=(j, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
                plt.show(block=False)
                plt.pause(sleep_time)
                plt.close()

            start_time = time.time()
            # Sorting in ascending order
            if(desc == False):
                if(array_copy[j] > element):
                    array_copy[j + 1] = array_copy[j]
                    j -= 1
                else:
                    break
            # Sorting in descending order
            elif(desc == True):
                if(array_copy[j] < element):
                    array_copy[j + 1] = array_copy[j]
                    j -= 1
                else:
                    break
            stop_time = time.time()

            # Adding time taken for iteration to sort_time
            sort_time += (stop_time - start_time)

        array_copy[j + 1] = element

    return array_copy, sort_time
