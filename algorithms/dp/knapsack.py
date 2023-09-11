def load_knapsack(i, capacity, weights, values, mem):
    # Check if the result is already memoized
    if mem[i][capacity] is not None:
        return mem[i][capacity]

    # Base cases | Reached no capacity left
    if capacity == 0:
        return 0
    # Added more items to knapsack than its original capacity
    if capacity < 0:
        return -float('inf')
    # Reached the end of possible items
    if i >= len(weights):
        return 0

    steal = values[i] + load_knapsack(i+1, capacity - weights[i], weights, values, mem)
    skip = load_knapsack(i+1, capacity, weights, values, mem)
    result = max(steal, skip)

    # Memoize the result
    mem[i][capacity] = result

    return result
