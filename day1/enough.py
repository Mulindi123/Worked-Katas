# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].

def delete_nth(order, max_e):
    result =[]

    count ={}

    for a in order:
        if a in count:
            count[a] +=1
        else:
            count[a] =1

        if count[a] <= max_e:
            result.append(a)
    return result

# def delete_nth(order,max_e):
#     answer = []
#     for x in order:
#         if answer.count(x) < max_e:
#             answer.append(x)
            
#     return answer

#def delete_nth(order,max_e):
    # return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ] # yes!

def delete_nth(order,max_e):
    return [order[i] for i in range(len(order)) if order[0:i+1].count(order[i]) <= max_e]

print(delete_nth([1,2,3,1,2,1,2,3],2) )# [1,2,3,1,2,3]
print(delete_nth([20,37,20,21],1) )    #[20,37,21]