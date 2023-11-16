# Tuesday, October 24th
# Task description
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns the maximum among all integers 
#which are multiples of 4.
# For example, given array A as follows:
# [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
# the function should return 84.
# Assume that:
# N is an integer within the range [1..1,000];
# each element of array A is an integer within the range [−10,000..10,000];
# there is at least one element in array A which satisfies the condition in the task statement.
# In your solution, focus on correctness. The performance of your solution 

def solution(A):
    four_multiples = []
    for number in A:
        if number % 4 == 0:
            
            four_multiples.append(number)

    
    max_multiple =max(four_multiples)
    
    return max_multiple
    
# print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
# print(solution([-8, 16, -20, 0]))


def solution(A):
    return max([number for number in A if number % 4 == 0])

print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
print(solution([-8, 16, -20, 0]))