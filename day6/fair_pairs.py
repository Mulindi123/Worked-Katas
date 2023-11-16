# DESCRIPTION:
# Task
# Find pairs of elements from two input lists such that swapping these pairs results in equal sums for both lists. If no such pair exists, return an empty set.
# Input
# Two lists of integers, list1 and list2, with the same length.
# Output
# A set of tuples, each containing two elements (num_from_list1, num_from_list2). These tuples represent the pairs of elements that can be swapped to make the sums of the lists equal.
# Examples
# fair_swap([1, 1], [2, 2]) ➞ {(1, 2)}

# fair_swap([1, 2], [2, 3]) ➞ {(1, 2), (2, 3)}

def fair_swap(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)

    swapped = set()

    for num1 in list1:
        for num2 in list2:
            if (sum1-num1+num2)==(sum2-num2+num1):
                swapped.add((num1, num2))

    return swapped

print(fair_swap([1, 1], [2, 2])) #{(1, 2)}
print(fair_swap([1, 2], [2, 3])) #{(2, 3), (1, 2)}

