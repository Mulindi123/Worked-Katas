
def diamond(n):
    if (n<0) or (n%2==0):
        return None
    
    diamonds =''

    for i in range(n):
        if i <= n/2:
            stars = '*' * ((i*2) +1)
        else:
            stars = '*' * ((n-i)*2 -1)
            
        diamonds += ' ' * int((n-len(stars))/2) + stars + '\n'
    return diamonds

print(diamond(5))