unsorted_array = [9, 7, 2, 4, 1, 3, 8, 6, 5, 10]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    print(f"left: {left}")
    print(f"middle: {middle}")
    print(f"right: {right}")

    return quick_sort(left) + middle + quick_sort(right)
