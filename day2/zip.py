#The zip() function returns a zip object, which is an iterator of tuples 
#where the first item in each passed iterator is paired together, and then the second 
#item in each passed iterator are paired together etc.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x)) #(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

y = 23
z = 22

c = zip(str(y), str(z))
print(str(y))
print(str(z))
print(tuple(c))  #(('(', '2'), ('2', '2'))