# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers,
#  and return the result in %.

# Example:
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.
# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de 

def compare(a, b):
    similar_digits =0

    for i, j in zip(str(a), str(b)):
        if i==j:
            # print(type(i), type(j))
            similar_digits +=1

    percentage = f"{int((similar_digits/2)*100)}%"

    return percentage

# print(compare(12, 34))
# print(compare(23, 22))
# print(compare(15, 51)) #Fails for this
# print(compare(13, 14))
# print(compare(20, 20))
# print(compare(10, 11))


def compared(a, b):
    a, b = str(a), str(b)
    if sorted(a) == sorted(b):
        return ("100%")
    else:
        for digit in a:
            if b.count(digit) > 0: #21, 22


                return("50%")
    return("0%")

print(compared(12, 34))
print(compared(23, 22))
print(compared(15, 51)) #Passes
print(compared(13, 14))
print(compared(20, 20))
print(compared(10, 11))
