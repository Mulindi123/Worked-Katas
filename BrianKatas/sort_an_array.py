# Sort an array by value and index
# Your task is to sort an array of integer numbers by the product of the value and the index of
# the positions.

# For sorting the index starts at 1, NOT at 0!
# The sorting has to be ascending.
# The array will never be null and will always contain numbers.

# Example:

# Input: 23, 2, 3, 4, 5
# Product of value and index:
# 23 => 23 * 1 = 23  -> Output-Pos 4
#  2 =>  2 * 2 = 4   -> Output-Pos 1
#  3 =>  3 * 3 = 9   -> Output-Pos 2
#  4 =>  4 * 4 = 16  -> Output-Pos 3
#  5 =>  5 * 5 = 25  -> Output-Pos 5

# Output: 2, 3, 4, 23, 5

def sort_by_value_and_index(arr):
    prod_list = []
    
    for index, value in enumerate(arr):
        product = (index + 1) * value

        prod_list.append(product)
    
    print(prod_list)

    combo_list = list(zip(arr, prod_list))
    print(combo_list)

    sorted_list = sorted(combo_list, key=lambda x: x[1])
    print(sorted_list)

    result_list = [item[0] for item in sorted_list]
    print(result_list)

    return result_list

sort_by_value_and_index([23, 2, 3, 4, 5])



