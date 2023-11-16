# Task
# Given a string, return if a given letter always appears immediately before another given letter.
# Worked Example
# ("he headed to the store", "h", "e") ➞ True

# # All occurences of "h": ["he", "headed", "the"]
# # All occurences of "h" have an "e" after it.
# # Return True

# ('abcdee', 'e', 'e') ➞ False
# # For first "e" we can get "ee"
# # For second "e" we cannot have "ee"
# # Return False
# Examples
# ("i found an ounce with my hound", "o", "u") ➞ True

# ("we found your dynamite", "d", "y") ➞ False
# Notes
# All sentences will be given in lowercase.

def letters(txt, a, b):

    for i in range(len(txt)-1):
        if txt[i] == a and txt[i + 1 ] == b:
          return True
    
    return False
        

# print(letters("he headed to the store", "h", "e"))
# print(letters('abcdee', 'e', 'e'))
# print(letters("i found an ounce with my hound", "o", "u"))


def best_friend(txt, a, b): #i found an ounce with my hound
    words = txt.split()
    # print(words)
    for word in words: 
        for i in range(len(word) - 1):
            if word[i] == a and word[i + 1] == b:
                return True  #f o u n d/an#        a b
    return False

#best_friend("i found an ounce with my hound", "o", "u")

print(best_friend("he headed to the store", "h", "e"))
print(best_friend('abcdee', 'e', 'e')) #false
print(best_friend("i found an ounce with my hound", "o", "u"))
print(best_friend('we found your dynamite', 'd', 'y')) #false
print(best_friend('look they took the cookies', 'o', 'o')) #false