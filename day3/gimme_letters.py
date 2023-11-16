# Given a string indicating a range of letters, return a string
# which includes all the letters in that range, including the last letter. 
#Note that if the range is given in capital letters, return the string in capitals also!
# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"

# https://www.codewars.com/kata/6512b3775bf8500baea77663
import string
def gimme_the_letters(sp):
    letters = string.ascii_letters
    parts = sp.split("-")

    if len(parts)== 2:
        start_letter, end_letter = parts[0], parts[1]
        if len(start_letter) == 1 and len(end_letter) == 1 and start_letter.isalpha() and end_letter.isalpha():
            start_index, end_index = letters.index(start_letter), letters.index(end_letter)   

            return letters[start_index:end_index+1]
        
    return "Invalid input"


print(gimme_the_letters('a-z'))
print(gimme_the_letters("h-o"))
print(gimme_the_letters("A-Z"))