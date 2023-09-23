def iterate_fibonacci(num):
    first = 0
    second = 1
    ans = 0

    for i in range(1, num):
        ans = first + second

        first = second
        second = ans

    return ans


def memoize_fibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1

    ans = memoize_fibonacci(num - 1) + memoize_fibonacci(num - 2)
    memo[num] = ans

    return ans


def recursive_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    ans = recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)

    return ans
