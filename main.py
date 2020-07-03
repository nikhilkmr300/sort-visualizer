import numpy as np

from helper import is_sorted, plot
from sort_visualizer import bubble, selection, insertion, merge, quick

array = np.random.randint(100, size=100)
print(f'Array size: {len(array)}')

# Bubble sort
sorted_array, sort_time = bubble.sort_visualize(array, desc=False, visualize=False, sleep_time=0.0001, title='Bubble sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Bubble sort: ' + str(round(sort_time, 5)) + ' s')

# Selection sort
sorted_array, sort_time = selection.sort_visualize(array, desc=False, visualize=False, sleep_time=0.0001, title='Selection sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Selection sort: ' + str(round(sort_time, 5)) + ' s')

# Insertion sort
sorted_array, sort_time = insertion.sort_visualize(array, desc=False, visualize=False, sleep_time=0.0001, title='Insertion sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Insertion sort: ' + str(round(sort_time, 5)) + ' s')

# Merge sort
sorted_array, sort_time = merge.sort_visualize(array, desc=False, visualize=False, sleep_time=0.0001, title='Merge sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Merge sort: ' + str(round(sort_time, 5)) + ' s')

# Quick sort
sorted_array, sort_time = quick.sort_visualize(array, desc=False, visualize=False, sleep_time=0.0001, title='Quick sort', xlabel='', ylabel='', xticks=[], yticks=[], color='b')
print(f'Quick sort: ' + str(round(sort_time, 5)) + ' s')
