import numpy as np
import matplotlib.pyplot as plt
import sys

from sort_visualizer import bubble, selection, insertion, merge, quick

if(len(sys.argv) != 2):
    print('Usage: python profiler.py <Name of sorting algorithm>')
    print('Example: python profiler.py merge')
    sys.exit()

input_sizes = np.logspace(0, 4, 50)
input_sizes = np.array([int(input_size) for input_size in input_sizes])
lower = 0
upper = int(10**7)

# If you're on a Unix/Linux machine, you can redirect the output of this script
# to a file as python profiler.py merge > data/merge.csv
print('s_no,input_size,sort_time(s)')
for i, input_size in enumerate(input_sizes):
    array = np.random.randint(low=lower, high=upper, size=input_size)
    print(f'{i + 1},{input_size},', end='')

    if(sys.argv[1].lower() == 'bubble'):
        _, sort_time = bubble.sort_visualize(array, desc=False, visualize=False)
        print(f'{sort_time}')

    elif(sys.argv[1].lower() == 'selection'):
        _, sort_time = selection.sort_visualize(array, desc=False, visualize=False)
        print(f'{sort_time}')

    elif(sys.argv[1].lower() == 'insertion'):
        _, sort_time = insertion.sort_visualize(array, desc=False, visualize=False)
        print(f'{sort_time}')

    elif(sys.argv[1].lower() == 'merge'):
        _, sort_time = merge.sort_visualize(array, desc=False, visualize=False)
        print(f'{sort_time}')

    elif(sys.argv[1].lower() == 'quick'):
        _, sort_time = quick.sort_visualize(array, desc=False, visualize=False)
        print(f'{sort_time}')
