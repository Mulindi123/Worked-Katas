# Write a function revSub which reverses all sublists where consecutive elements are even.
# Note that the odd numbers should remain where they are.
# Example
# With [1,2,4,5,9] as input, we should get [1,4,2,5,9].
# Here, because [2,4] is a sublist of consecutive even numbers, it should be flipped. 
#There could be more than one sublist of even numbers, or none at all.
# A few other examples:
# [] -> []
# [2,4] -> [4,2]
# [2,4,3] -> [4,2,3]
# [2,4,3,10,2] -> [4,2,3,2,10]

def rev_sub(arr):
    result = []
    sub = []
    for a in arr:
        if a % 2 == 0:            #Even numbers
            sub.append(a)
        else:
            if sub:                 # Check that the sub list is not empty
                sub.reverse()
                result.extend(sub)
                sub =[]
            
            result.append(a)

    if sub:
        sub.reverse()
        result.extend(sub)
    
    return result

print(rev_sub([2,4,3]))      #[4,2,3]
print(rev_sub([2,1,6,4,3]))  #[2,1,4,6,3]
print(rev_sub([1,2,4,5,9]))  #[1,4,2,5,9]
print(rev_sub([1, 2, 4, 6, 8, 3, 5, 7, 9]))  #[1,8,6,4,2,3,5,7,9]
print(rev_sub([1, 2, 4, 11, 6, 8, 3, 5, 7, 9]))  # [1,4,2,11,8,6,3,5,7,9]
