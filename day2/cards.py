# You have a pack of 5 randomly numbered cards, which can range from 0-9. 
#You can win if you can produce a higher two-digit number from your cards, than your opponent. 
#Return True if your cards win that round.
# Worked Example
# ([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
# # Your cards can make the number 96
# # Your opponent can make the number 73
# # You win the round since 96 > 73
# Examples
# ([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
# ([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ False
# ([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ False
# Notes
# Return False if you and your opponent reach the same maximum number (see example #3).
# https://www.codewars.com/kata/65128d27a5de2b3539408d83

def cards(list1, list2):
    list1 = sorted(list1, reverse=True)
    print(list1)

    list2 = sorted(list2, reverse=True)
    print(list2)

    return int(str(list1[0]) + str(list1[1])) > int(str(list2[0]) + str(list2[1])) # use string concatination
  

print(cards([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])) #True
print(cards([1, 2, 3, 4, 5], [9, 8, 7, 6, 5])) #False
print(cards([4, 3, 4, 4, 5], [3, 2, 5, 4, 1])) #False
print(cards([1, 4, 9, 2, 1], [3, 7, 7, 8, 7])) #True