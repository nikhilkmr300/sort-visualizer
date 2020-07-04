import numpy as np
import matplotlib.pyplot as plt
import math
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

    def height(heap):
        return math.floor(math.log2(node_count(heap)))

    def node_count(heap):
        return len(heap)

    def parent_index(index):
        return (index - 1) // 2

    def left_child_index(index):
        return 2 * index + 1

    def right_child_index(index):
        return 2 * index + 2

    def first_leaf_index(heap):
        return node_count(heap) // 2

    def is_max_heap(array):
        max_heap_flag = True
        for i in range(first_leaf_index(array)):
            if(array[left_child_index(i)] > array[i]):
                max_heap_flag = False
                break
            if(right_child_index(i) < len(array)):
                if(array[right_child_index(i)] > array[i]):
                    max_heap_flag = False
                    break
        return max_heap_flag

    def max_heapify(heap, index=0):
        """
        Maintains the max heap property. Assumes that both left and right
        subtrees of the tree rooted at index are max heaps.
        """

        # CASE 1: Leaf node
        # Return as leaf nodes are trivially max heaps
        if(index >= first_leaf_index(heap)):
            return

        # Finding the largest among left, root and right
        left_index = left_child_index(index)
        right_index = right_child_index(index)

        # CASE 2: Node with only a left child
        # If node does not have a right child
        if(right_index >= node_count(heap)):
            # Comparing root and left child
            if(heap[index] < heap[left_index]):
                # Left is greater than root, swapping root and left
                heap[index], heap[left_index] = heap[left_index], heap[index]
            return

        # CASE 3: Internal node
        # Already max heap, return
        if(heap[index] >= heap[left_index] and heap[index] >= heap[right_index]):
            return
        elif(heap[left_index] > heap[index] and heap[left_index] >= heap[right_index]):
            # Left is greatest, swapping root and left
            heap[index], heap[left_index] = heap[left_index], heap[index]
            max_heapify(heap, left_index)
        elif(heap[right_index] > heap[index] and heap[right_index] > heap[left_index]):
            # Right is greatest, swapping root and right
            heap[index], heap[right_index] = heap[right_index], heap[index]
            max_heapify(heap, right_index)

    def build_max_heap(array):
        for i in range(first_leaf_index(array) - 1, -1, -1):
            max_heapify(array, index=i)

    def heap_sort(array, desc=False, visualize=False, sleep_time=SLEEP_TIME, title='', xlabel='', ylabel='', xticks=[], yticks=[], color='b'):
        result_array = np.zeros(len(array), dtype=int)

        if(visualize == True):
            plot_figure(result_array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

        # Converting array into max heap
        build_max_heap(array)
        build_max_heap(result_array)

        i = 0
        if(visualize == True):
            if(desc == False):
                full_array = np.concatenate((array, result_array[len(result_array) - i - 1:]))
                plot_figure(full_array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
            elif(desc == True):
                full_array = np.concatenate((result_array[:i], array))
                plot_figure(full_array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

        while(len(array) > 0):
            # Swapping last element of heap and root
            array[0], array[-1] = array[-1], array[0]

            # Sorting in ascending order
            if(desc == False):
                result_array[len(result_array) - i - 1] = array[-1]
            # Sorting in descending order
            elif(desc == True):
                result_array[i] = array[-1]

            # Removing element that was copied into result_array
            array = np.delete(array, -1)

            max_heapify(array, 0)

            if(visualize == True):
                if(desc == False):
                    full_array = np.concatenate((array, result_array[len(result_array) - i - 1:]))
                    plot_figure(full_array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
                elif(desc == True):
                    full_array = np.concatenate((result_array[:i], array))
                    plot_figure(full_array, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
            i += 1

        return result_array

    if(visualize == True):
        array_copy = heap_sort(array_copy, desc=desc, visualize=visualize, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)

    start_time = time.time()
    # Time for sorting must not include time for plotting, so visualize=False
    heap_sort(array_copy, desc=desc, visualize=False, sleep_time=sleep_time, title=title, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, color=color)
    stop_time = time.time()
    sort_time = stop_time - start_time

    return (array_copy, sort_time)
