# Write a function

# def solution(A)

# that, given an array A consisting of N integers, returns the number of distinct values in array A.

# For example, given array A consisting of six elements such that:

#  A[0] = 2    A[1] = 1    A[2] = 1
#  A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];

from collections import Counter
def solution(A):
    count_a = Counter(A)

    return (len(set(count_a)))


print(solution([1,2,3,2,1,2,3,5]))
print(solution([1,2]))
print(solution([2, 1, 1, 2, 3, 1]))

