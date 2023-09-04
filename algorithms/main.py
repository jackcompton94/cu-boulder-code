from mathematics import fast_fourier_transform


def main():
    unsorted_array = [9, 7, 2, 4, 1, 3, 8, 6, 5, 10]
    # merge_sort.merge_sort(unsorted_array)
    # print('')
    #
    # quick_sort.quick_sort(unsorted_array)
    # print('')

    # arr1 = [1, 0, 1]
    # arr2 = [1, 1, 0, 1]
    # ans = binary_math.add_binary_arrays(arr1, arr2)
    # print(ans)

    # ans = binary_math.grade_school_multiply(arr1, arr2)
    # print(ans)

    print(fast_fourier_transform.compute_fourier_naive([1,-1,1,-1]))


if __name__ == '__main__':
    main()
