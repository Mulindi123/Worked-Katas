# You receive some random elements as a space-delimited string. Check if the elements are part of an
# ascending sequence of integers starting with 1, with an increment of 1 (e.g. 1, 2, 3, 4).

# Return:

# 0 if the elements can form such a sequence, and no number is missing ("not broken", e.g. "1 2 4 3")
# 1 if there are any non-numeric elements in the input ("invalid", e.g. "1 2 a")
# n if the elements are part of such a sequence, but some numbers are missing, and n is the lowest of them ("broken", e.g. "1 2 4" or "1 5")
# Examples
# "1 2 3 4"  ==>  return 0, because the sequence is complete

# "1 2 4 3"  ==>  return 0, because the sequence is complete (order doesn't matter)

# "2 1 3 a"  ==>  return 1, because it contains a non numerical character

# "1 3 2 5"  ==>  return 4, because 4 is missing from the sequence

# "1 5"      ==>  return 2, because the sequence is missing 2, 3, 4 and 2 is the lowest

def find_missing_numbers(sequence):
    if not sequence:
        return 0
    
    sequence_list = sequence.split()
    # print(sequence_list)

    digit_list = []

    for item in sequence_list:
        if not item.isnumeric():
            return 1
        
        digit_list.append(int(item))
        
    expected_sequence = set(range(1, max(digit_list)+1))
    print(expected_sequence)
    actual_sequence = set(digit_list)
    print(actual_sequence)

    missing_numbers = list(expected_sequence- actual_sequence)

    if not missing_numbers:
        return 0
    
    else:
        return min(missing_numbers)

    
find_missing_numbers("2 1 3 4 a")

# print(find_missing_numbers("2 1 3 a")) #1
# print(find_missing_numbers("1 2 3 4" )) #0
# print(find_missing_numbers("1 2 4 3")) #0
# print(find_missing_numbers("1 3 2 5")) #4
# print(find_missing_numbers("1 5")) #2
# print(find_missing_numbers("")) #0
# print(find_missing_numbers("___________")) #1


# print(range(5))
# print(set(range(5)))




def find_missing_number(sequence):
    if not sequence:
        return 0
    
    sequence_list = sequence.split()
    # print(sequence_list)

    numbers = {int(x) for x in sequence_list if x.isdigit()}
    # print(numbers)

    if len(numbers) != len(sequence_list):  # definitely contains non-numeric characters
        return 1
    for i in range(1, max(numbers)+1):  
        if i not in numbers:
            return i
    return 0


find_missing_number("2 1 3 4 a")

print(find_missing_number("2 1 3 a")) #1
print(find_missing_number("1 2 3 4" )) #0
print(find_missing_number("1 2 4 3")) #0
print(find_missing_number("1 3 2 5")) #4
print(find_missing_number("1 5")) #2
print(find_missing_number("")) #0
print(find_missing_number("___________")) #1























