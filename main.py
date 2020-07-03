import numpy as np

from helper import is_sorted, plot
from sort_visualizer import bubble, selection, insertion, merge, quick, heap, radix

# Test cases for each of the sorts.
# Change the parameters used to set the array depending on the sort.
array = np.random.randint(1, 100, size=100)
"""
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
sorted_array, sort_time = quick.sort_visualize(array, desc=False, visualize=True, sleep_time=0.001, partition_strategy='random', random_seed=7, title='Quick sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Quick sort: ' + str(round(sort_time, 5)) + ' s')

# Heap sort
sorted_array, sort_time = heap.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Heap sort', xlabel='', ylabel='', xticks=[], yticks=[], color='g')
print(f'Heap sort: ' + str(round(sort_time, 5)) + ' s')

# Radix sort
sorted_array, sort_time = radix.sort_visualize(array, desc=False, visualize=True, sleep_time=0.0001, title='Radix sort', xlabel='', ylabel='', xticks=[], yticks=[], color='g')
print(f'Radix sort: ' + str(round(sort_time, 5)) + ' s')
"""
