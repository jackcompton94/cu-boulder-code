from mathematics import fast_fourier_transform
from dp import rod_cutter, coin_changer


def main():
    # # Basics of Sorting Algorithms
    # unsorted_array = [9, 7, 2, 4, 1, 3, 8, 6, 5, 10]
    # merge_sort.merge_sort(unsorted_array)
    # print('')
    # quick_sort.quick_sort(unsorted_array)
    # print('')

    # # Binary Math and Multiplication
    # arr1 = [1, 0, 1]
    # arr2 = [1, 1, 0, 1]
    # ans = binary_math.add_binary_arrays(arr1, arr2)
    # print(ans)
    # ans = binary_math.grade_school_multiply(arr1, arr2)
    # print(ans)

    # # Fast Fourier Transform | Naive Approach
    # print(fast_fourier_transform.compute_fourier_naive([1,-1,1,-1]))

    # # Dynamic Programming | Memoization
    length = 14
    table = [[3, 1.80], [4, 2]]
    mem = [None] * (length + 1)
    print(f'max value: {rod_cutter.max_revenue(length=length, table=table, mem=mem)}')

    target = 8
    coins = [25, 10, 5, 1]
    mem = [None] * (target + 1)
    print(f'best change: {coin_changer.make_change(target, coins, mem)}')


if __name__ == '__main__':
    main()
