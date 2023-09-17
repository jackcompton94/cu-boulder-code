def load_knapsack(i, capacity, weights, values, mem):
    # Check if the result is already memoized
    if mem[i][capacity] is not None:
        return mem[i][capacity]

    # Base cases | Reached no capacity left
    if capacity == 0:
        return 0, []
    # Added more items to knapsack than its original capacity
    if capacity < 0:
        return -float('inf'), []
    # Reached the end of possible items
    if i >= len(weights):
        return 0, []

    # Calculate the value and selected items when stealing the current item
    steal_value, steal_items = load_knapsack(i+1, capacity - weights[i], weights, values, mem)
    steal_value += values[i]
    steal_items = [i] + steal_items  # Include the current item in the selected items

    # Calculate the value and selected items when skipping the current item
    skip_value, skip_items = load_knapsack(i+1, capacity, weights, values, mem)

    # Choose the option (steal or skip) that maximizes the value
    if steal_value > skip_value:
        result_value = steal_value
        result_items = steal_items
    else:
        result_value = skip_value
        result_items = skip_items

    # Memoize the result
    mem[i][capacity] = (result_value, result_items)

    return result_value, result_items
