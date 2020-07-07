# sort-visualizer
Scripts to visualize and profile common sorting algorithms.

I've wanted to make [this](https://www.toptal.com/developers/sorting-algorithms) sort of animation since the first time I saw it in CS50 about 4 years ago,
because they look so cool.

Includes the following sorting algorithms:
* Bubble sort
* Selection sort
* Insertion sort
* Merge sort
* Quick sort
* Heap sort
* Radix sort

# Examples
## Snapshots
Snapshots of animations of insertion, merge and heap sorts.

### Insertion sort
<img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/snapshots/insertion.png" width="320">
Note the sorted portion forming on the left.

### Merge sort
<img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/snapshots/merge.png" width="320">
Note the sorted subarrays before merging.

### Heap sort
<img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/snapshots/heap.png" width="320">
Note the sorted portion forming on the right,
as the root of the max-heap is extracted and pushed to the back of the array.

## Profiling
<img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/graphs/compare_all.png" width="640">

## Initialization
Includes the following possible array initializations in the initializer directory:
* random: Randomly initializes array in range \[low, high)
* reverse: Initializes array in reverse sorted order
* many_same: Initializes array with many similar elements
* error: Initializes array with elements in a uniform distribution around an anchor

<img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/initializer/examples/random.png" width="320"><img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/initializer/examples/reverse.png" width="320"><img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/initializer/examples/many_same.png" width="320"><img src="https://github.com/nikhilkmr300/sort-visualizer/blob/master/initializer/examples/error.png" width="320">
