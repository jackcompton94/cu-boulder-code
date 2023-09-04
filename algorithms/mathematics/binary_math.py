def add_binary_arrays(arr1, arr2):
    carry = 0
    ans = []

    # Sets n to the smaller array
    n = min(len(arr1), len(arr2))

    # Flips arrays
    flip_arr1 = list(reversed(arr1))
    flip_arr2 = list(reversed(arr2))

    # Add arrays
    for i in range(n):
        carry, bit_sum = sum_of_bits(flip_arr1[i], flip_arr2[i], carry)
        ans.append(bit_sum)

    # Finish looping through arr1 if longer
    if len(arr1) > n:
        for i in range(n, len(arr1)):
            carry, bit_sum = sum_of_bits(flip_arr1[i], 0, carry)
            ans.append(bit_sum)

    # Finish looping through arr2 if longer
    if len(arr2) > n:
        for i in range(n, len(arr2)):
            carry, bit_sum = sum_of_bits(flip_arr2[i], 0, carry)
            ans.append(bit_sum)

    if carry == 1:
        ans.append(carry)
    flip_ans = list(reversed(ans))
    return flip_ans


def sum_of_bits(bit1, bit2, carry):
    bit_sum = bit1 + bit2 + carry

    if bit_sum == 0:
        return carry, bit_sum
    if bit_sum == 1:
        carry = 0
        return carry, bit_sum
    if bit_sum == 2:
        bit_sum = 0
        carry = 1
        return carry, bit_sum
    if bit_sum == 3:
        bit_sum = 1
        carry = 1
        return carry, bit_sum


def grade_school_multiply(arr1, arr2):
    n, m = len(arr1), len(arr2)
    if n > m:
        temp = arr1
        bits = arr2
    else:
        temp = arr2
        bits = arr1
    result = [0]

    for bit in bits:
        if bit == 1:
            result = add_binary_arrays(result, temp)
        temp.append(0)
    return result


# Implement Karatsuba Multiply
