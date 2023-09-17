def make_change(coins, change):
    change_back = []
    i = 0
    while change > 0:
        # Base Case - Reached end of the register
        if i == len(coins):
            return change_back
        # If the current highest value coin can be added to change back - add it
        if change > coins[i]:
            change_back.append(coins[i])
            change -= coins[i]
        # Current coin is too large, move to next largest coin
        else:
            i += 1

    return change_back
