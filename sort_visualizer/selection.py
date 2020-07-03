import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from helper import is_sorted, plot

# Data for marker below selection sort plot
MARKER = '^'    # Marker text
MARKER_Y = -5   # y-coordinate of marker in data coordinates
MARKER_SIZE = 15    # Font size of marker text
MARKER_WEIGHT = 'bold'  # Font weight of marker text
MARKER_COLOR = 'r'  # Color of marker text

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    sort_time = 0   # Time for sorting (excluding plotting)
    i = 0   # Iteration index
    while(not is_sorted.is_sorted(array_copy, desc=desc)):
        # Part 1: Finding min_index/max_index in array_copy[i:]
        min_index = i
        max_index = i
        for j in range(i + 1, len(array_copy)):
            start_time = time.time()
            # Sorting in ascending order
            if(desc == False):
                if(array_copy[j] < array_copy[min_index]):
                    min_index = j
            # Sorting in descending order
            elif(desc == True):
                if(array_copy[j] > array_copy[max_index]):
                    max_index = j
            stop_time = time.time()
            # Adding time taken for finding min_index/max_index to sort_time
            sort_time += (stop_time - start_time)

            # Plotting
            if(visualize == True):
                fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
                ax.annotate(s=MARKER, xy=(j, 0), xytext=(j, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
                plt.show(block=False)
                plt.pause(sleep_time)
                plt.close()

        # Part 2: Swapping array_copy[i] with array_copy[min_index]/
        # array_copy[max_index]
        start_time = time.time()
        # Sorting in ascending order
        if(desc == False):
            tmp = array_copy[min_index]
            array_copy[min_index] = array_copy[i]
            array_copy[i] = tmp
            i += 1
        # Sorting in descending order
        elif(desc == True):
            tmp = array_copy[max_index]
            array_copy[max_index] = array_copy[i]
            array_copy[i] = tmp
            i += 1
        stop_time = time.time()
        # Adding time taken for finding min_index/max_index to sort_time
        sort_time += (stop_time - start_time)

    # Plotting after last swap
    if(visualize == True):
        fig, ax = plot.bar(array_copy, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
        ax.annotate(s=MARKER, xy=(j, 0), xytext=(j, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    return (array_copy, sort_time)
