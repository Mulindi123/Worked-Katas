# # from collections import Counter
# # def solution(A):
#     # digit_count ={}
#     # for num in A:
#     #     if num not in digit_count:
#     #         digit_count[num] =1
#     #     else:
#     #         digit_count[num] +=1

#     # for i in range(len(digit_count)):
#     #     for j in range(i+1, len(digit_count)-1):
#     #         if digit_count[i] == digit_count[j]
# #     print(digit_count)
# # solution([1,1,1,2,2,2])


# def solution(S):

    # n = len(S)
    # count = 0
    # for i in range(1, n):
    #     prefix = S[:i]
    #     suffix = S[i:]

    #     count_x_prefix = prefix.count("x")
    #     count_y_prefix = prefix.count("y")
    #     count_x_suffix = suffix.count("x")
    #     count_y_suffix = suffix.count("y")
        
    #     if( (count_x_prefix==count_x_suffix and count_y_prefix==count_y_suffix) or
    #        (count_x_prefix==count_y_prefix and count_y_prefix==count_x_suffix)):
    #         count +=1

    # return count
# print(solution("xzzzy"))
# print(solution("toyxmy"))
# print(solution("apple"))


# def solution(A):

#     count ={}
#     for num in A:
#         count[num] = count.get(num, 0)+1

#     frequency_list = [0]*(max(count.values()) + 1)
    
#     for freq in count.values():
#         frequency_list[freq] +=1

#     deletions = 0
#     for i in range(1, len(frequency_list)):
#         while frequency_list[i] > 1:
#             j = i - 1
#             while j>0 and frequency_list[j] > 0:
#                 j -=1

#                 frequency_list[j] +=1
#                 frequency_list[i] -=1
#                 deletions += i-j

#     return deletions



def solution(A):

    count ={}
    for num in A:
        count[num] = count.get(num, 0)+1

    occurrence_of_count = {}
    for occ in count.values():
        occurrence_of_count[occ] = occurrence_of_count.get(occ, 0)+1

    deletion =0
    seen_frequencies = set()
    for occ in occurrence_of_count.values():
        while occ in seen_frequencies:
            occ -= 1
            deletion +=1
        if occ != 0:
            seen_frequencies.add(occ)


    return deletion

print(solution([1,1,1,2,2,2]))
print(solution([5, 3, 3, 2, 5, 2, 3, 2])) #2


def solution(A):

    count = {}
    for num in A:
        count[num] = count.get(num, 0) + 1

    # Step 2: Create a frequency array
    frequency_array = [0] * (max(count.values()) + 1)

    # Step 3: Count the frequencies of frequencies
    for freq in count.values():
        frequency_array[freq] += 1

    # Step 4: Adjust frequencies to make them unique
    deletions = 0
    for i in range(1, len(frequency_array)):
        while frequency_array[i] > 1:
            j = i - 1
            while j > 0 and frequency_array[j] > 0:
                j -= 1
            frequency_array[j] += 1
            frequency_array[i] -= 1
            deletions += i - j

    return deletions