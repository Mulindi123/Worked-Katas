# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}

# z = x.issuperset(y)

# print(z)

x= {"g", "f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
v = {"e", "h", "g", "a", "b", "c"}

Z = x.issuperset(y)
w = y.issubset(x)


print(Z) # True
print(w) # True
print(v.issubset(x))  #False because "h" is not in x
print(v.issuperset(y)) #True coz all the elements of y are in v
