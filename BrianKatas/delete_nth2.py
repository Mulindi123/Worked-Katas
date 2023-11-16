def delete_nth(order, max_e):
    result =[]

    count ={}

    for a in order:
        if a not in count:
            count[a] =1
        else:
            count[a] += 1
        
        if count[a] <= max_e:
            result.append(a)
    return result


print(delete_nth([1,2,3,1,2,1,2,3], 2)) #[1,2,3,1,2,3]
print(delete_nth([20,37,20,21], 1))  # [20, 37, 21]