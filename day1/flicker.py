# Create a function that always returns True for every item in a given list. 
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.
# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.


def flicker(lst):
    result = []
    switch = True

    for word in lst:
        if word == "flick":
            switch = not switch
        result.append(switch)
    
    return result

print(flicker(['flick', 'chocolate', 'adventure', 'sunshine']))
print(flicker(['codewars', 'flick', 'code', 'wars']))
print(flicker(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))