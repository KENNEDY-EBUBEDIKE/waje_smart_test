"""
Using Dynamic Programming Approach.
The efficiency of the algorithm is increased by using only two variables (a and b)
to store the two possible states of the elements.
"""


def maximum_amount(arr):
    a = 0  # represents maximum subsequence with ith element
    b = 0  # represents maximum subsequence without i element
    for i in arr:
        new_max_subsequence_without_i = max(b, a)

        a = b + i
        b = new_max_subsequence_without_i

    return max(b, a)


# Driver code
if __name__ == "__main__":
    input_array = [2, 10, 14, 8, 1]
    print(maximum_amount(input_array))
