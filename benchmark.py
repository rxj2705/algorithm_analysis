# Compares how long bubble sort and quicksort take for different list sizes,
# then draws a graph of the results.

import random
import time
import matplotlib.pyplot as plt

from bubble_sort import bubble_sort
from quick_sort import quick_sort

sizes = [100, 500, 1000, 2000, 3000, 4000]
runs = 3

bubble_times = []
quick_times = []

for size in sizes:
    bubble_total = 0
    quick_total = 0

    for run in range(runs):
        # make a list of random numbers
        numbers = []
        for k in range(size):
            numbers.append(random.randint(1, 10000))

        # time bubble sort (on a copy, so quicksort gets the same unsorted list)
        start = time.time()
        bubble_sort(numbers.copy())
        bubble_total = bubble_total + (time.time() - start)

        # time quicksort
        start = time.time()
        quick_sort(numbers.copy())
        quick_total = quick_total + (time.time() - start)

    # work out the average time
    bubble_times.append(bubble_total / runs)
    quick_times.append(quick_total / runs)

    print(size, "items: bubble sort", round(bubble_total / runs, 4), "s, quicksort", round(quick_total / runs, 4), "s")

# draw the graph

plt.plot(sizes, bubble_times, marker="o", label="Bubble sort O(n²)")
plt.plot(sizes, quick_times, marker="o", label="Quicksort O(n log n)")
plt.xlabel("Number of items")
plt.ylabel("Time (seconds)")
plt.title("Bubble sort vs Quicksort")
plt.legend()
plt.savefig("performance_graph.png")
plt.show()