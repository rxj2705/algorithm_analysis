# Bubble Sort vs Quicksort

## How the algorithms work

Bubble sort goes through the list and compares each number with the one next to it. If the left number is bigger, they swap. After each pass the biggest number left is at the end, so the next pass can be shorter. I added a check that stops the sort early if a pass makes no swaps, because it means the list is already sorted.

Quicksort picks a pivot, which in my code is the middle number. It splits the list into numbers smaller than, equal to and bigger than the pivot. Then it sorts the smaller and bigger parts the same way (recursion) and joins everything back together.

## Small and large lists

Bubble sort is O(n²) on average and in the worst case, because each number is compared with almost every other number. On an already sorted list it is O(n), because of the early stop. Quicksort is O(n log n) on average, but it can be O(n²) if the pivot keeps splitting the list badly.

I timed both on random lists from 100 to 4,000 numbers and took the average of three runs. With 100 numbers, both took less than a thousandth of a second, so the difference did not matter. With 4,000 numbers, bubble sort took 0.2345 seconds and quicksort took 0.0017 seconds, about 138 times faster. When the list size doubled from 2,000 to 4,000, bubble sort took about 4.5 times longer, which fits O(n²).

## Comparison and real-world use

Bubble sort is easy to understand and write, so it is useful for learning or very small lists, but it is too slow for large amounts of data. Quicksort is much faster on big lists. Fast methods like it are used for things like sorting search results, game leaderboards or large spreadsheets. For a real program I would use quicksort or Python's built-in sort.