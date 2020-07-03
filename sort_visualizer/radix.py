import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from helper import is_sorted, plot

SLEEP_TIME = 0.0001     # Time in milliseconds between plotting figures (frames)

def sort_visualize(array, desc=False, visualize=True, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
    # Sorting a copy of array so that the original array is unchanged
    array_copy = np.array(array.copy())

    def plot_figure(array, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        # Plotting
        fig, ax = plot.bar(array, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
        plt.show(block=False)
        plt.pause(sleep_time)
        plt.close()

    if(visualize == True):
        plot_figure(array_copy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    num_iters = get_num_digits(np.max(array_copy))

    sort_time = 0
    for i in range(num_iters):
        start_time = time.time()
        array_copy = counting_sort(array_copy, k=9, digit=i)
        stop_time = time.time()
        sort_time += (stop_time - start_time)

        if(visualize == True):
            plot_figure(array_copy, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    if(desc == False):
        return (array_copy, sort_time)
    elif(desc == True):
        return (np.flip(array_copy), sort_time)

def counting_sort(array, k=9, digit=None):
    return_array = np.zeros(len(array), dtype=int)
    if(digit is None):
        # Cumulative frequency of array elements
        count = np.zeros(k + 1, dtype=int) # count[i] tracks the number of occurrences of number i in array
        # Populating count
        for i in range(len(array)):
            count[array[i]] += 1
        for i in range(1, k + 1):
            count[i] += count[i - 1]
        # Populating return_array
        for i in range(len(return_array) - 1, -1, -1):
            return_array[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
    elif(digit is not None):
        digit_array = get_digit_array(array, digit=digit)
        # Cumulative frequency of array elements
        count = np.zeros(10, dtype=int) # count[i] tracks the number of occurrences of number i in array
        # Populating count
        for i in range(len(digit_array)):
            count[digit_array[i]] += 1
        for i in range(1, k + 1):
            count[i] += count[i - 1]
        # Populating return_array
        for i in range(len(return_array) - 1, -1, -1):
            return_array[count[digit_array[i]] - 1] = array[i]
            count[digit_array[i]] -= 1
    return return_array

def get_num_digits(num):
    if(num == 0):
        return 1
    count = 0
    while(num != 0):
        num = num // 10
        count += 1
    return count

def get_digit(num, digit=0):
    for i in range(digit + 1):
        rem = num % 10
        num = num // 10
    return rem

def get_digit_array(array, digit=0):
    return np.array([get_digit(num, digit=digit) for num in array])
