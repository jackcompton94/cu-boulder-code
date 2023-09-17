def max_revenue(length, table, mem):
    # Base cases
    if length == 0:
        return 0, []
    if length < 0:
        return -10000, []

    # Check if the result is memoized
    if mem[length] is not None:
        return mem[length]

    # Used to keep track of the maximum revenue found during recursive calls
    max_so_far = 0
    best_decision = []

    # Iterate through the price table for each subsequent length
    for li, pi in table:
        revenue, decision = max_revenue(length - li, table, mem)
        revenue += pi

        if revenue > max_so_far:
            max_so_far = revenue
            # Update the best decision and add the current length
            best_decision = [li] + decision

    # Memoize the result and best decision before returning
    mem[length] = max_so_far, best_decision
    return max_so_far, best_decision
