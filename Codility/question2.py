# QUESTION 2:
# There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room. In each room,
# any number of guests can be accommodated.
# However, not all guests like to have a lot of roommates.
# You are given an array A of N integers; the K-th guest wants to be in a room that contains at most A[K]
# guests, including themselves.
# Write a function: def solution(A) that, given the array A, returns the minimum number of rooms needed
# to accommodate all guests.

# Examples:
# 1. Given A = [1,1,1,1,1], your function should return 5.
# 2. Given A = [2,1,4], your function should return 2.
# 3. Given A = [2,7,2,9,8], your function should return 2.

def solution(A):
    assigned_rooms = 0

    for index, value in enumerate(A):
        if value <= index+1:
            assigned_rooms += 1


    return assigned_rooms


print(solution([1,1,1,1,1])) #5
print(solution([2,1,4]))     #2
print(solution([2,7,2,9,8])) #2
