# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

# Your task is to return:

# true if developers from all of the following age groups have signed up: teens, twenties, thirties, 
# forties, fifties, sixties, seventies, eighties, nineties, centenarian (at least 100 years young).
# false otherwise.
# For example, given the following input array:

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]
# your function should return true as there is at least one developer from each age group.

# Notes:

# The input array will always be valid and formatted as in the example above.
# Age is represented by a number which can be any positive integer up to 199.

def age_diversity(lst):
    age_groups = ['teens', 'twenties', 'thirties', 'forties', 'fifties', 'sixties', 'seventies', 'eighties', 'nineties', 'centenarian']

    age_group_count = {age_group: 0 for age_group in age_groups}

    for dev in lst:
        if dev["age"] >= 100:
            age_group = 'centenarian'
        else:
            age_group = (dev["age"] // 10) * 10

        if age_group in age_groups:
            age_group_count[age_group] += 1

    return all(count > 0 for count in age_group_count.values())


print(age_diversity(list1))






# stores name and corresponding salaries
# salary = {"raj" : 50000, "striver" : 60000, "vikram" : 5000}

# stores the salaries only
# list1 = salary.values()
# print(list(list1))
# print(sum(list1)) # prints the sum of all salaries

# d = {'a': 97, 'b': 98, 'c': 99, 'd': 100} 
# # space key added using setdefault() method 
# d.setdefault(' ', 32) 
# print(d)

# from collections import Counter

# # Your dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}

# # Use Counter to count occurrences of each value
# value_counts = Counter(my_dict.values())

# # Print the result
# print(value_counts)
