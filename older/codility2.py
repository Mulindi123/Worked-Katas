# Task description
# You are given a string S consisting of N digits. What is the largest sum of two two-digit
# fragments of S? The selected fragments cannot overlap.
# Write a function:
# def solution(S)
# that, given a string S, returns the largest sum of two two-digit numbers that are 
# non-overlapping fragments of S.
# Examples:
# Given S = "43798", the function should return 141. The chosen fragments are "43" and "98": 
# "43 7 98" Given S = "00101", the function should return 10. The chosen fragments are "00" and "10": "00 10 1". 
# Note that fragments "01" and "10" cannot be chosen as they overlap.Given S = "0332331",
# the function should return 66. The chosen fragments are "33" and "33": "0 33 2 33 1".Given S = "00331",
# the function should return 34. The chosen fragments are "03" and "31": "0 03 31"
# Assume that:
# N is an integer within the range [4..100];
# string S is made only of digits (0−9).
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


def solution(S):
    #s = 03432331
    #len(S)-2 =6
    max_sum =0

    for i in range(len(S)-2):
        for j in range(i+2, len(S)):
            
            num1 = int(S[i:i+2])
            print("num1 is:",num1)
            num2 = int(S[j:j+2])
            print("num2 is:",num2)
            sum = num1 + num2
            print("sum is", sum) 
            if sum > max_sum:
                max_sum = sum
    print("the naximum sum is:", max_sum)
    return max_sum

solution("03332331")
