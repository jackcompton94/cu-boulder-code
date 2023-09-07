def max_revenue(length, table, mem):
    # Base cases
    if length == 0:
        return 0
    if length < 0:
        return -10000

    # Check if the result is memoized
    if mem[length] is not None:
        return mem[length]

    max_so_far = 0

    for li, pi in table:
        max_so_far = max(max_so_far, pi + max_revenue(length - li, table, mem))

    # Memoize the result before returning
    mem[length] = max_so_far
    return max_so_far
