#Append  -----> Add an element at the end of a list

list = ["bananas", "oranges", "grapes"]
# list.append("melon")
print(list)

#Extend --------> Add multiple elements to a list at once
# list.extend(["kiwis", "apples", "guavas"])
print(list)


#insert -----------> Add an element at a specific possition in a list
#It takes 2 arguments
    # The index at which the new element should be inserted.
    # The new element itself.

# list.insert(1, "papaya")
print(list)


# + Operator ----------->You can use the + operator to concatenate, or join together, two or more lists.
#  This is appending the elements of one list to another list.

# However, unlike the append(), extend(), and insert() methods, the + operator does not modify the original lists.
# Instead, it creates a new list that contains the elements of both original lists.

new_fruits = list + ["mangoes", "raspberries", "pineapples"]
print(new_fruits)
print(list)