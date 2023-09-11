def load_knapsack(limit, j, weights, values):
    # Base cases
    if limit == 0:
        return 0
    # we have added more items to knapsack than its original capacity
    if limit < 0:
        return -float('inf')
    if j >= len(weights):
        return 0

    return max(
        # steal item
        values[j] + load_knapsack(limit - weights[j], j+1, weights, values),
        # skip item
        load_knapsack(limit, j+1, weights, values)
    )
