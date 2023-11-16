#https://www.codewars.com/kata/65126d52a5de2b11c94096d2
# Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

# Worked Example
# 2520 ➞ 72

# # The first and last digits are 2 and 0.
# # 2 and 0 form 20.
# # The second digit is 5 and the second to last digit is 2.
# # 5 and 2 form 52.

# # 20 + 52 = 72
# Examples
# 121 ➞ 13
# # 11 + 2

# 1039 ➞ 22
# # 19 + 3

# 22225555 ➞ 100
# # 25 + 25 + 25 + 25
# Notes
# If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
# Any number which is zero-padded counts as a single digit (see example #2).
# print("7" + "6") 
# print(7+6)
def closing_in_sum(n):
    str_n = str(n) #typecast the number into a string ---->2520
    # print(str_n)
    length = len(str_n)   #4
    sum = 0
    for a in range(length//2):                                              # 0th              (4-1-0)
        first_number = str_n[a]  
        print(type(first_number), first_number)                             #  2    5   1    2      0
        last_number = str_n[length-1-a]   
        # print(type(last_number), last_number)                              #       1st   (4-1-1)
        paired_sum = int(first_number + last_number)  #"2" + "0" = "20"    

        sum += paired_sum

    if length % 2 == 1:                           #the number is odd eg 2 5 1 2 0
        sum += int(str_n[length//2]) 

    return sum

print(closing_in_sum(2520))
print(closing_in_sum(25120))
print(closing_in_sum(22225555))
# print(closing_in_sum(5332824166496569))