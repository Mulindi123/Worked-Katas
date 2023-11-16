def fac_cal(n):
    factorial =1

    for i in range(1, n+1):
        factorial *= i

    return factorial

# print(fac_cal(5))

def triangle(b):
    for i in range(1, b+1):
        for j in range(i):
            print("*", end="")

        print()


# triangle(4)

def flip_triangle(d):
    for i in range(d, 0, -1):   #prints rows
        for j in range(d - i):
            print(" ", end="")  #prints indentation
        for j in range(2 * i - 1):
            print("*", end="")  #prints *
        print()

# flip_triangle(10)

def fibonacci(n):
    a = 0
    b = 1
    first = True  # To handle the first number without a leading comma
    while a <= n:
        if not first:
            print(',', end=' ')
        else:
            first = False
        print(a, end='')
        c = b + a
        a = b
        b = c

# fibonacci(100)

#Using a recursive function and memoizatio
def fibonacci_recursive(b, memo={}):
    if b in memo:
        return memo[b]
    if b <= 0:
        return 0
    elif b == 1:
        return 1
    else:
        memo[b] = fibonacci_recursive(b - 1, memo) + fibonacci_recursive(b - 2, memo)
        return memo[b]
    
# for i in range(20):
#     print(fibonacci_recursive(i), end="")

def fibonacci_generator(d):
     v, w = 0, 1
     for _ in range(d):
         yield v
         v, w = w, v + w

# for num in fibonacci_generator(10):
#     print(num, end=",")


def fibonacci_list(value):
    fib = [0, 1]
    while len(fib) < value:
        fib.append(fib[-1] + fib[-2])
    return fib

# fib_sequence = fibonacci_list(10)
# print(fib_sequence)


#tribonacci
def tribonacci(signature, n):
    if n <= len(signature):
        return signature[:n]
    
    while len(signature)<n:
        signature.append(signature[-1] + signature[-2] + signature[-3])
        
    return signature

def Xbonacci(signature, n):
    X = len(signature)
    
    if X >= n:
        return signature[:n]
    
    while len(signature) < n:
        signature.append(sum(signature[-X:]))
    
    return signature

# print(Xbonacci([0,1],10))
# print(Xbonacci([0,1,1],10))
# print(Xbonacci([1,1,1],10))
# print(Xbonacci([1,1,1,1],10))
# print(Xbonacci([1,0,0,0,0,0,1],10))


list = ["bananas", "mangoes", "kiwis", "melons"]
for index, fruit in enumerate(list):
    print(f"{fruit} at index {index}")