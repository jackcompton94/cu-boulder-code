from mathematics import fast_fourier_transform, binary_math
import dynamic
import sorting
from greedy import coin_changer


def main():
    # # Basics of Sorting Algorithms
    # unsorted_array = [9, 7, 2, 4, 1, 3, 8, 6, 5, 10]
    # sorting.merge_sort.merge_sort(unsorted_array)
    # print('')
    # sorting.quick_sort.quick_sort(unsorted_array)
    # print('')
    #
    # # Binary Math and Multiplication
    # arr1 = [1, 0, 1]
    # arr2 = [1, 1, 0, 1]
    # ans = binary_math.add_binary_arrays(arr1, arr2)
    # print(ans)
    # ans = binary_math.grade_school_multiply(arr1, arr2)
    # print(ans)
    #
    # # Fast Fourier Transform | Naive Approach
    # print(fast_fourier_transform.compute_fourier_naive([1,-1,1,-1]))
    #
    # # Dynamic Programming | Memoization
    # # Rod Cutting
    # length = 15
    # table = [[3, 1.5], [4, 2]]
    # mem = [None] * (length + 1)
    # print(f'max value: {dynamic.rod_cutter.max_revenue(length=length, table=table, mem=mem)}')
    # # Exchange Coins
    # target = 8
    # coins = [25, 10, 5, 1]
    # mem = [None] * (target + 1)
    # print(f'best change: {dynamic.coin_changer.make_change(target, coins, mem)}')
    # # Knapsack Problem
    # capacity = 100
    # weights = [1, 5, 10, 35, 90]
    # values = [15, 11, 30, 20, 195]
    # # Initialize a memoize table with len(weights)+1 rows and capacity+1 columns
    # mem = [[None] * (capacity + 1) for _ in range(len(weights)+1)]
    # print(f'max value: {dynamic.knapsack.load_knapsack(0, capacity, weights, values, mem)}')
    # # Longest Common Subsequence
    # s1 = "CATTAGGAT"
    # s2 = "CATTAGGAT"
    # mem = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    # print(f'longest common subsequence: {dynamic.common_subsequence.lcs(s1, s2, 0, 0, mem)}')

    coins = [25, 10, 5, 1]
    change = 69
    print(coin_changer.make_change(coins, change))


if __name__ == '__main__':
    main()
