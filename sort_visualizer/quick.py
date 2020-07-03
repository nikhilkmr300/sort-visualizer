import numpy as np
import matplotlib.pyplot as plt
import random
import time
import sys

from helper import is_sorted, plot

# Data for marker below quick sort plot
MARKER = '^'    # Marker text
MARKER_Y = -5   # y-coordinate of marker in data coordinates
MARKER_SIZE = 15    # Font size of marker text
MARKER_WEIGHT = 'bold'  # Font weight of marker text
MARKER_COLOR = 'r'  # Color of marker text

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, partition_strategy='random', random_seed=1, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    def plot_figure(array, sleep_time=SLEEP_TIME, marker_x=None, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        # Plotting
        fig, ax = plot.bar(array, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
        if(marker_x is not None):
            ax.annotate(s=MARKER, xy=(marker_x, 0), xytext=(marker_x, MARKER_Y), xycoords='data', textcoords='data', fontsize=MARKER_SIZE, ha='center', fontweight=MARKER_WEIGHT, color=MARKER_COLOR)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    def partition(array, l, r, desc=False, visualize=True, partition_strategy='random', sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b', random_seed=1):
        if(visualize == True):
            plot_figure(array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

        random.seed(random_seed)
        pivot_index = l
        if(partition_strategy == 'first'):
            # Pivot is the element with index l
            pivot_index = l
        elif(partition_strategy == 'last'):
            # Pivot is the element with index r
            pivot_index = r
        elif(partition_strategy == 'random'):
            # Pivot is a random element with index in range[l, r]
            pivot_index = random.randint(l, r)
        elif(partition_strategy == 'median_of_3'):
            # Pivot is the median of the elements with indices l, (l + r) // 2 and r
            first = array[l]
            mid = array[(l + r) // 2]
            last = array[r]
            if(mid < first < last or last < first < mid):
                # Pivot is the element with index l
                pivot_index = l
            elif(mid < last < first or first < last < mid):
                # Pivot is the element with index r
                pivot_index = r
            else:
                # Pivot is the element with index (l + r) // 2
                pivot_index = (l + r) // 2
        else:
            print('partition_strategy must be \'first\', \'random\' or \'median_of_3\'.')
            sys.exit()

        # Moving pivot to index r
        array[pivot_index], array[r] = array[r], array[pivot_index]

        # The array is divided into 4 regions:
        # If desc == False: | [l] ----- <= pivot ----- [i] | ----- > pivot ----- | [j] ----- unseen ----- | [r] pivot |
        # If desc == True:  | [l] ----- >= pivot ----- [i] | ----- < pivot ----- | [j] ----- unseen ----- | [r] pivot |
        i = l - 1
        for j in range(l, r):
            if(desc == False):
                if(array[j] <= array[r]):
                    i += 1
                    # Swapping array[i] and array[j]
                    array[i], array[j] = array[j], array[i]
            elif(desc == True):
                if(array[j] >= array[r]):
                    i += 1
                    # Swapping array[i] and array[j]
                    array[i], array[j] = array[j], array[i]
        # Swapping array[i + 1] and pivot (array[r])
        array[i + 1], array[r] = array[r], array[i + 1]

        if(visualize == True):
            plot_figure(array, sleep_time=sleep_time, marker_x=i + 1, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

        return i + 1

    def quick_sort(array, l, r, desc=False, visualize=True, partition_strategy='random', sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks='', yticks='', color='b', random_seed=1):
        if(l >= r):
            return

        if(visualize == True):
            plot_figure(array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

        partition_index = partition(array, l, r, desc=desc, visualize=visualize, partition_strategy=partition_strategy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color, random_seed=random_seed)
        quick_sort(array, l, partition_index - 1, desc=desc, visualize=visualize, partition_strategy=partition_strategy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color, random_seed=random_seed)
        quick_sort(array, partition_index + 1, r, desc=desc, visualize=visualize, partition_strategy=partition_strategy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color, random_seed=random_seed)

        if(visualize == True):
            plot_figure(array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    if(visualize == True):
        quick_sort(array, 0, len(array) - 1, desc=desc, visualize=visualize, partition_strategy=partition_strategy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color, random_seed=random_seed)

    start_time = time.time()
    # Time for sorting must not include time for plotting, so visualize=False
    quick_sort(array_copy, 0, len(array) - 1, desc=desc, visualize=False, partition_strategy=partition_strategy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color, random_seed=random_seed)
    stop_time = time.time()
    sort_time = stop_time - start_time

    return array_copy, sort_time
