def make_change(target, coins, mem):
    # Base cases
    if target == 0:
        return 0, []
    if target < 0:
        return -1, []

    # Check if the result is memoized
    if mem[target] is not None:
        return mem[target]

    min_coins = float('inf')
    best_change = []

    # Iterate through each coin denomination to see if it can be used
    for coin in coins:
        if target - coin >= 0:
            # Recursively look to break the target amount down with the available coins
            total_coins, change = make_change(target - coin, coins, mem)
            # Check if this coin provides fewer coins than the current minimum
            if total_coins + 1 < min_coins:
                min_coins = total_coins + 1
                best_change = [coin] + change

    # Memoize the result and best change before returning
    mem[target] = min_coins, best_change
    return min_coins, best_change
