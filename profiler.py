import numpy as np
import matplotlib.pyplot as plt
import sys

from sort_visualizer import bubble, selection, insertion, merge, quick, heap, radix
from initializer import initializer

RANDOM_SEED = 1
SORTS = ['bubble', 'selection', 'insertion', 'merge', 'quick', 'heap', 'radix']
INITIALIZATIONS = ['random', 'reverse', 'many_same', 'error']

# Input sizes for the sorting algorithm
INPUT_SIZES = np.logspace(0, 4, 50)
INPUT_SIZES = np.array([int(input_size) for input_size in INPUT_SIZES])
LOW = 0   # Lower bound on values in the array
HIGH = int(10**7)  # Upper bound on values in the array

# Specific to many_same initialization
CHOICE_ELEMENTS = [25, 50, 75]  # Set of elements for many_same initialization

# Specific to error initialization
ANCHOR = 100    # Anchor for error initialization
ERROR = 0.2     # Error percentage for error initialization

if(len(sys.argv) != 3):
    print('Usage: python profiler.py <sort> <initialization>')
    print(f'Available sorts: ', end=''); [print(available_sort, end=' ') for available_sort in SORTS]; print()
    print(f'Available initializations: ', end=''); [print(available_initialization, end=' ') for available_initialization in INITIALIZATIONS]; print()
    sys.exit()

sort = sys.argv[1]
initialization = sys.argv[2]

if(sort not in SORTS):
    print(f'Available sorts: ', end=''); [print(available_sort, end=' ') for available_sort in SORTS]; print()
    sys.exit()
if(initialization not in INITIALIZATIONS):
    print(f'Available initializations: ', end=''); [print(available_initialization, end=' ') for available_initialization in INITIALIZATIONS]; print()
    sys.exit()

# If you're on a Unix/Linux machine, you can redirect the output of this script
# to a file as python profiler.py merge random > data/random/merge.csv
# print(f'sort: {sort}\tinitialization: {initialization}')
print('s_no,input_size,sort_time(s)')
for i, input_size in enumerate(INPUT_SIZES):
    # INITIALIZING
    if(initialization == 'random'):
        array = initializer.random(LOW, HIGH, input_size, seed=RANDOM_SEED)
    elif(initialization == 'reverse'):
        array = initializer.reverse(input_size, 0)
    elif(initialization == 'many_same'):
        array = initializer.many_same(CHOICE_ELEMENTS, input_size, seed=RANDOM_SEED)
    elif(initialization == 'error'):
        array = initializer.error(ANCHOR, input_size, error=ERROR, seed=RANDOM_SEED)
    print(f'{i + 1},{input_size},', end='')

    # SORTING
    _, sort_time = eval(f'{sys.argv[1].lower()}.sort_visualize(array, desc=False, visualize=False)')
    print(f'{sort_time}')
