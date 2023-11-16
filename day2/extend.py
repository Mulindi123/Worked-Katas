#Adds elements of a list at the end of a given list
# Similar t javascript spread operator

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

points = (1, 4, 5, 9)

fruits.extend(cars)    #takes exactly one argument
fruits.extend(points)
print(fruits)