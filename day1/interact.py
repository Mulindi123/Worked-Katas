# Question1
# Given two strings comprised of + and -, return a new string which shows how the two strings 
#interact in the following way:
    #Let the two strings be str1 and str2
    #len(str1) = len(str2)
        # When positives and positives interact, they remain positive.
        # When negatives and negatives interact, they remain negative.

        # But when negatives and positives interact, they become neutral, and are shown as the number 0.
    # Worked Example
        # ("+-+", "+--") ➞ "+-0"
        # # Compare the first characters of each string, then the next in turn.
        # # "+" against a "+" returns another "+".
        # # "-" against a "-" returns another "-".
        # # "+" against a "-" returns "0".
        # # Return the string of characters.

# Examples
# ("--++--", "++--++") ➞ "000000"

# ("-+-+-+", "-+-+-+") ➞ "-+-+-+"

# ("-++-", "-+-+") ➞ "-+00"

# Notes
# The two strings will be the same length.

def pos_neg(str1, str2):

    result = ""
    for i in range(len(str1)):  #the strings are of the same length
        if str1[i] == str2[i]:            # When positives and positives interact, they remain positive.
            result += str1[i]           # When negatives and negatives interact, they remain negative.
        else:
            result += "0"  #It means the signs are not the same eg("+", "-")

    return result

print(pos_neg("--++--", "++--++")) #"000000"
print(pos_neg("-+-+-+", "-+-+-+"))
print(pos_neg("-++-", "-+-+"))
def neutralise(str1, str2):
    for index, letter in enumerate(str1):
        result = ""

        if str1[index] == str2[index]:
            result += letter
        else:
            result += "0"
    return result
#Revise on enumerate