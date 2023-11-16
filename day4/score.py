# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.
import string
def high(x):
    sum_of_letters =[]
    list_x = x.split()

    alphabet = string.ascii_lowercase

    for word in list_x:
        count =0
        for letter in word:
            if letter in alphabet:
                count += alphabet.index(letter)+1
        sum_of_letters.append(count)
    
    for word, num in zip(list_x, sum_of_letters):
        if num == max(sum_of_letters):
            return word

        
print(high('what time are we climbing up the volcano'))

#Try these also
#https://www.codewars.com/kata/56684677dc75e3de2500002b
#https://www.codewars.com/kata/596e91b48c92ceff0c00001f
#https://www.codewars.com/kata/57a06005cf1fa5fbd5000216
