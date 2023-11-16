# # CreateLongestSpike
# # Task description
# # We will call a sequence of integers a spike if they first increase (strictly) and then decrease
# # (also strictly, including the last element of the increasing part). For example (4, 5, 7, 6, 3, 2)
# # is a spike, but (1, 1, 5, 4, 3) and (1, 4, 3, 5) are not. Note that the increasing and decreasing
# # parts always intersect, e.g.: for spike (3, 5, 2) sequence (3, 5) is an increasing part and sequence
# # (5, 2) is a decreasing part, and for spike (2) sequence (2) is both an increasing and a decreasing part.

# # Your are given an array A of N integers. Your task is to calculate the length of the longest possible
# # spike, which can be created from numbers from array A. Note that you are NOT supposed to find the
# # longest spike as a sub-sequence of A, but rather choose some numbers from A and reorder them to create
# # the longest spike.

# # Write a function:

# # def solution(A)

# # which, given an array A of integers of length N, returns the length of the longest spike which can be
# # created from the numbers from A.

# # Examples:

# # Given A = [1, 2], your function should return 2, because (1, 2) is already a spike.
# # Given A = [2, 5, 3, 2, 4, 1], your function should return 6, because we can create the following spike
# # of length 6: (2, 4, 5, 3, 2, 1).
# # Given A = [2, 3, 3, 2, 2, 2, 1], your function should return 4, because we can create the following
# # spike of length 4: (2, 3, 2, 1) and we cannot create any longer spike. Note that increasing and
# # decreasing parts should be strictly increasing/decreasing and they always intersect.
# # Write an efficient algorithm for the following assumptions:

# # N is an integer within the range [1..100,000];
# # each element of array A is an integer within the range [1..1,000,000]. 

# def solution(A):
#     N = len(A)
#     if N <= 2:
#         return N
    
#     increasing_part = [A[0]]                       #[2, 5, 3, 2, 4, 1]
#     prev = A[0]

#     for value in A[1:]:
#         if value > prev:
#             increasing_part.append(value)
#             prev = value

    
#     print(increasing_part)
#     decreasing_part = [A[-1]]
#     prev = A[-1]

#     #for value in reversed(A[:-1]):

#     # peak = max(A)
#     # print(max(A))
#     # print(A)
#     print(list(reversed(A[:-1])))

# print(solution([2, 5, 3, 2, 4, 1]))    #6: (2, 4, 5, 3, 2, 1).

# # print(solution([2]))


def solution(A):
    n = len(A)
    if n<= 2:
        return n
    
    msl = 2

    for i in range(1, n-1):
        il = dl=1
        j =i
        while j>0 and A[j] > A[j-1]:
            il +=1
            j -=1

        j = 1
        while j < n-1 and A[j] > A[j+1]:
            dl+=1
            j +=1

    msl =max(msl, il+dl-1)
    
    return msl

print(solution([2, 5, 3, 2, 4, 1]))    #6: (2, 4, 5, 3, 2, 1).

print(solution([2]))


# def search_element(array):
#    increase = 1
#    decrease = 1
#    n = len(array)
#    for i in range(1, n):
#       if(array[i] < array[i-1]):
#          if increase == 1:
#             decrease = decrease + 1
#          else:
#             return -1
#       elif(array[i] > array[i-1]):
#          if increase == 1:
#             pt = array[i-1]
#          if decrease >= 2:
#             increase = increase + 1
#          else:
#             return -1
#       elif(array[i] == array[i-1]):
#          return -1
#    if(increase >= 2 and decrease >= 2):
#       return pt
#    else:
#       return -1
# array = [5,4,3,4]
# element = search_element(array)
# print(element)