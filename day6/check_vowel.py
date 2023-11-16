# https://www.codewars.com/kata/5a2b7edcb6486a856e00005b
# DESCRIPTION:
# Check if it is a vowel(a, e, i, o, u,) on the n position in a string (the first argument).
# Don't forget about uppercase.
# A few cases:
# {
# checkVowel('cat', 1)  ->   true // 'a' is a vowel
# checkVowel('cat', 0)  ->   false // 'c' is not a vowel
# checkVowel('cat', 4)  ->   false // this position doesn't exist
# }

# P.S. If n < 0, return false

def check_vowel(strng, n):
    lower_case_list = [letter for letter in strng.lower()]
    # print(lower_case_list)
    if 0 <= n <=len(strng):
        if lower_case_list[n] in ['a', 'e', 'i', 'o','u']:
            return True
        return False
    
    return False

#One Liner
def check_vowel(s,i):
    return 0 <= i < len(s) and s[i] in "aieouAEIOU"

print(check_vowel('cat', 4))
print(check_vowel('Amanda', 0))

