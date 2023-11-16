import math
# Each floating-point number should be formatted that only the first two decimal places are returned. 
#You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

# Don't round the numbers! Just cut them after two decimal places!

# Right examples:  
# 32.8493 is 32.84  
# 14.3286 is 14.32

# Incorrect examples (e.g. if you round the numbers):  
# 32.8493 is 32.85  
# 14.3286 is 14.33


def formatted_float(number):

    #Converts the float to a string with 2 decimal places
    formatted = "{:.2f}".format(number)

    #converts it back to a float to remove the trailing zeros

    formatted = float(formatted)

    return formatted

#print(formatted_float(-7488.83485834983))

def truncated_number(number):
    
    out_put = int(number * 100)/100

    return out_put
#print(truncated_number(-7488.83485834983))


def format_float(number):
    # Truncate the number to two decimal places without rounding
    return  math.floor(number * 100) / 100
    


#print(format_float(-7488.83485834983))

def two_decimal_places(number):
    number = str(number)
    print(number)
    number = number.split('.')

    print(number)
    result = number[0] + '.' + number[1][:2]
    print(result)
    return float(result)

two_decimal_places(-7488.83485834983)

