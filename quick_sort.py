# Quicksort
# Picks a pivot, splits the list into smaller and bigger numbers, then sorts each part the same way.
# Time complexity: O(n log n) on average, O(n^2) in the worst case.


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    left = []
    middle = []
    right = []

    for number in numbers:
        if number < pivot:
            left.append(number)
        elif number == pivot:
            middle.append(number)
        else:
            right.append(number)

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    my_list = [8, 3, 5, 1, 9, 2]
    print("Before:", my_list)
    print("After: ", quick_sort(my_list))