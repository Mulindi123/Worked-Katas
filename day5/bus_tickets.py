# DESCRIPTION:
# In one city, bus tickets use numbers from 100000 to 999999. Your task is to find the number 
# of lucky tickets between two input tickets' values.
# The ticket is considered to be lucky if the sum of first 3 digits equals to the sum of last 3 digits:
# 123321 is lucky, i.e. 1+2+3 equals to 3+2+1
# 123444 is not lucky, i.e. 1+2+3 doesn't equal to 4+4+4


# numbers = 123321  #"1234567" =[1,2,3,4,5] # 1 2 3 "1 2 3 "
# number_str = str(numbers)
# list = [int(a) for a in number_str] 
# print(list)

# print(sum(list[0:3]))
# print(sum(list[3:]))

def lucky_ticket(ticket):

    status = "lucky"
    
    # ticket_str = str(ticket)
    # digit_list = [int(digit) for digit in ticket_str]
    digit_list = [int(digit) for digit in str(ticket)]
    
    if sum(digit_list[:3]) != sum(digit_list[3:]):
        status = "not lucky"

    return status


print(lucky_ticket(123241))
# list1 = [1,2,3,4,5]
# list2 =[4,5]
# list = list1+list2
# print(list)