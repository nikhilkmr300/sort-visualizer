import numpy as np
import matplotlib.pyplot as plt

from helper import is_sorted, plot
from sort_visualizer import *
from initializer import initializer

# Testing initializer
"""
random_array = initializer.random(0, 100, 100, seed=1)
fig, ax = plot.bar(random_array, title='Random initialization | seed=1')
plt.show()

reverse_array = initializer.reverse(100, 0)
fig, ax = plot.bar(reverse_array, title='Reverse initialization')
plt.show()

many_same_array = initializer.many_same([25, 50, 75], 100)
fig, ax = plot.bar(many_same_array, title='Many same initialization | choices=[25, 50, 75]', yticks=[25, 50, 75])
plt.show()

error_array = initializer.error(100, 100, error=0.2)
fig, ax = plot.bar(error_array, title='Error initialization | anchor=100, error=0.2', yticks=[80, 100, 120])
plt.show()
"""

# Testing sorts
array = initializer.random(0, 100, 20, seed=1)

# Bubble sort
sorted_array, sort_time = bubble.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Bubble sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Bubble sort: ' + str(round(sort_time, 5)) + ' s')

# Selection sort
sorted_array, sort_time = selection.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Selection sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Selection sort: ' + str(round(sort_time, 5)) + ' s')

# Insertion sort
sorted_array, sort_time = insertion.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Insertion sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Insertion sort: ' + str(round(sort_time, 5)) + ' s')

# Merge sort
sorted_array, sort_time = merge.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Merge sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Merge sort: ' + str(round(sort_time, 5)) + ' s')

# Quick sort
sorted_array, sort_time = quick.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, partition_strategy='random', random_seed=1, title='Quick sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Quick sort: ' + str(round(sort_time, 5)) + ' s')

# Heap sort
sorted_array, sort_time = heap.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Heap sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Heap sort: ' + str(round(sort_time, 5)) + ' s')

# Radix sort
sorted_array, sort_time = radix.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Radix sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Radix sort: ' + str(round(sort_time, 5)) + ' s')
