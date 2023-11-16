# DESCRIPTION:
# Find all the dividers!
# You are given a list of prime numbers (e.g. [5, 7, 11]) and a list of their associated powers (e.g. [2, 1, 1]). 
# The product of those primes at their specified power forms a number x (in our case x = 5^2 * 7^1 * 11^1 = 1925).
# Your goal is to find all of the dividers for this number!
# To do so, you have to multiply each prime number, from its power 0 to its power p in the power list,
# to every other prime, from their power 0 to their associated power p.
# Each result of those products is a divider of x!
# In our example: [1, 5, 7, 11, 25, 35, 55, 77, 175, 275, 385, 1925]
# Once you find those dividers, sort them in ascending order, and VOILA!
#https://www.codewars.com/kata/64600b4bbc880643faa343d1

import math

# def get_dividers(values, powers):
#     prod_powers = []

#     for val, pow in zip(values, powers):
#         prod_powers.append(val**pow)

#     product = math.prod(prod_powers)


#     dividers = []
#     for i in range(1, product+1):
#         if product % i == 0:
#             dividers.append(i)

#     return dividers

def get_dividers(values, powers):
    product = math.prod([val**pow for val, pow in zip(values, powers)])

    return [i for i in range(1, product+1) if product % i ==0]

print(get_dividers([5, 7, 11], [2, 1, 1]))  #1925
print(get_dividers([11, 113], [1, 1]))