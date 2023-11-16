x = "Hello World!"
print(list(x))
# lst_x = x.split()
# print(lst_x)

# list_x = [letter for letter in x]
# print(list_x)
#print(len(list_x))
print(len(x))

for index, char in enumerate(x):
    print(index, char, end='')  # 0 H 1 e 2 l 3 l 4 o 5  6 W 7 o 8 r 9 l 10 d 11 !
