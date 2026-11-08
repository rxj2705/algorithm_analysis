# Bubble sort
# Goes through the list again and again, swapping neighbours that are in the wrong order.
# Time complexity: O(n^2) on average and in the worst case, O(n) if the list is already sorted.


def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if swapped == False:
            break

    return numbers


if __name__ == "__main__":
    my_list = [8, 3, 5, 1, 9, 2]
    print("Before:", my_list)
    print("After: ", bubble_sort(my_list))