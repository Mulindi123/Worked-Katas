# QUESTION 1:
# Write a function solution that, given an integer N, returns a string of length N containing as many different
# lower-case letters('a'-'z') as possible,in which each letter occurs an equal number of times.
 
# Examples:
# 1. Given N=3, the function may return 'fig', 'pea', 'nut', etc. Each of these strings contains three
#  different letters with the same number of occurrences.
# 2. Given N=5, the function may return 'mango', 'grape', 'melon', etc.
# 3. Given N=30, the function may return 'aabbcc....oo' (each letter from 'a' to 'o' occurs twice.

# import string
# from random import choice as rc
# from collections import Counter

# def solution(N):
#     if N < 0:
#         return "Invalid entry"

#     alphabet = list(string.ascii_lowercase)
#     result = []

#     repeat_factor = (N // len(alphabet)) + 1

#     selected_letters = set()
#     while len(result) < N:
#         letter = rc(alphabet)
#         if letter not in selected_letters:
#             selected_letters.add(letter)
#             result.extend([letter] * repeat_factor)

#     print("Selected Letters:",selected_letters)
#     print("".join(result))
#     return "".join(result)

from collections import Counter
import string
import random
def solution(N):

    alphabet = string.ascii_lowercase
    result = []
    prev = None

    for i in range(N):
        random_letter = random.choice(alphabet)
        if random_letter != prev:
            result.append(random_letter)
            prev = random_letter

    return "".join(result)


# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(30))

A = list(solution(40))

count_a = Counter(A)
print(len(A))

print(count_a)