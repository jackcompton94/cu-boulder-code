def lcs(s1, s2, i, j, mem):
    if i == len(s1) or j == len(s2):
        return 0, ""

    # Check if the result is already memoized
    if mem[i][j] is not None:
        return mem[i][j]

    # Check for match and increment both pointers
    if s1[i] == s2[j]:
        length, substring = lcs(s1, s2, i + 1, j + 1, mem)
        length += 1
        substring = s1[i] + substring
    else:
        # Increment each pointer recursively
        length1, substring1 = lcs(s1, s2, i + 1, j, mem)
        length2, substring2 = lcs(s1, s2, i, j + 1, mem)

        # Recover the solution
        if length1 >= length2:
            length, substring = length1, substring1
        else:
            length, substring = length2, substring2

    # Memoize the result
    mem[i][j] = (length, substring)
    return length, substring
