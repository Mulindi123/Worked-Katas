# You will be given a sequence of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

# Given the following input array:

list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]
# write a function that returns the average age of developers (rounded to the nearest integer). In the example above your function should return 50 (number).

# Notes:

# The input array will always be valid and formatted as in the example above.
# Age is represented by a number which can be any positive integer.

def average_age(lst):
    # age = [dev['age'] for dev in lst]
    # averaged_age = round(sum(age)/len(age))
    
    # return averaged_age

    return round(sum(dev['age'] for dev in lst)/len(lst))

print(average_age(list1))