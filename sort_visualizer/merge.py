import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from helper import is_sorted, plot

# Data for marker below mergef sort plot
MARKER = '^'    # Marker text
MARKER_Y = -5   # y-coordinate of marker in data coordinates
MARKER_SIZE = 15    # Font size of marker text
MARKER_WEIGHT = 'bold'  # Font weight of marker text
MARKER_COLOR = 'r'  # Color of marker text

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    def plot_figure(array, mid, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        # Plotting
        fig, ax = plot.bar(array, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
        ax.annotate(s=MARKER, xy=(mid, 0), xytext=(mid, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    def merge(array, l, mid, r, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        # Populating left_array, contains elements from index l to mid
        left_array = array[l:(mid + 1)].copy()  # Using copy to avoid aliasing
        # Populating right_array, contains elements from index mid to r
        right_array = array[(mid + 1):(r + 1)].copy()   # Using copy to avoid aliasing

        # Merging left_array and right_array into array
        i = 0; j = 0
        k = l
        while(i < left_array.shape[0] and j < right_array.shape[0]):
            if(desc == False):
                if(left_array[i] <= right_array[j]):
                    array[k] = left_array[i].copy() # Using copy to avoid aliasing
                    i += 1
                    k += 1
                elif(left_array[i] > right_array[j]):
                    array[k] = right_array[j].copy()    # Using copy to avoid aliasing
                    j += 1
                    k += 1
            elif(desc == True):
                if(left_array[i] > right_array[j]):
                    array[k] = left_array[i].copy() # Using copy to avoid aliasing
                    i += 1
                    k += 1
                elif(left_array[i] <= right_array[j]):
                    array[k] = right_array[j].copy()    # Using copy to avoid aliasing
                    j += 1
                    k += 1
        # Adding leftover elements from left_array into array
        while(i < left_array.shape[0]):
            array[k] = left_array[i].copy() # Using copy to avoid aliasing
            i += 1
            k += 1
        # Adding leftover elements from right_array into array
        while(i < right_array.shape[0]):
            array[k] = right_array[i].copy() # Using copy to avoid aliasing
            i += 1
            k += 1

        if(visualize == True):
            plot_figure(array, mid, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    def merge_sort(array, l, r, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        if(l >= r):
            return

        mid = (l + r) // 2

        merge_sort(array, l, mid, desc=desc, visualize=visualize, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)   # Sorting left half
        merge_sort(array, mid + 1, r, desc=desc, visualize=visualize, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)   # Sorting right half
        merge(array, l, mid, r, desc=desc, visualize=visualize, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)  # Merging left and right halves

    if(visualize == True):
        merge_sort(array_copy, 0, len(array_copy) - 1, desc=desc, visualize=visualize, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    start_time = time.time()
    # Time for sorting must not include time for plotting, so visualize=False
    merge_sort(array_copy, 0, len(array_copy) - 1, desc=desc, visualize=False)
    stop_time = time.time()
    sort_time = stop_time - start_time

    return array_copy, sort_time
