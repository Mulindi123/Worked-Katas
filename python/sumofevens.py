def sum_of_evens():
    sum =0
    for i in range(101):
        if i % 2 == 0:
            sum += i
    
    return sum

# print(sum_of_evens())


def sum_evens():
   print(sum(i for i in range(101) if i % 2 == 0))

# sum_evens()

def sum_of_evens():
    sum_of_evens = 0

    for num in range(0, 102, 2):
        sum_of_evens += num

print(sum_of_evens())

# Write a program that finds the sum of all natural numbers below 1000 (< 1000) that are multiples of 3 or 5, and prints it.

# If we list all the natural numbers below 20 (<20) that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.

# Note that 15 is only counted once.

def sum_of_odds():
    print(sum(i for i in range(1000) if i%3==0 or i%5==0))

sum_of_odds()

# Write functions to convert from Fahrenheit to Celsius and vice-versa.

# Your functions should look like:

# def fahrenheit_to_celsius(temp):
#     ...

# def celsius_to_fahrenheit(temp):
#     ...
# You'll find conversions in the Fahrenheit Wikipedia article.

# Example
# Here how your function could be used in an interactive Python interpreter:

# >>> celsius_to_fahrenheit(100)
# 212.0

def fahrenheit_to_celsius(temp):
    pass