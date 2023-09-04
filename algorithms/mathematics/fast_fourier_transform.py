import math
import cmath


def get_roots_of_unity(n):
    assert n >= 2
    angles = [2.0 * math.pi * k/n for k in range(n)]
    lst = [cmath.cos(ang) + cmath.sin(ang)*1j for ang in angles]
    return lst


def compute_fourier_naive(seq):
    n = len(seq)
    fft_seq = []
    w = 1.0  # Initialize a complex exponential factor for rotation

    # Generate the nth roots of unity (rotation factor)
    wn = math.cos(2.0 * math.pi/n) + math.sin(2.0 * math.pi/n) * 1j

    # Compute each DFT coefficient
    for j in range(n):
        Aj = 0  # Initialize the DFT coefficient for the j-th frequency component
        wj = 1.0  # Initialize the step to rotate input values

        # Compute the summation for the j-th DFT coefficient
        for k in range(n):
            Aj = Aj + wj * seq[k]  # Accumulate contributions from the input sequence
            wj = wj * w  # Update the rotation step

        fft_seq.append(Aj)  # Append the j-th DFT coefficient to the result
        w = w * wn  # Update the rotation for the next frequency

    return fft_seq
