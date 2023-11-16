# Kata Task
# I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
# NOTES:
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that



def cat_dog(humanYears):
    cat_age = 0
    dog_age =0

    if humanYears == 1:
        cat_age += 15
        dog_age += 15
        
    elif humanYears == 2:
        cat_age += 24
        dog_age += 24

    elif humanYears >=3:
        cat_age = 24 + 4*(humanYears-2)
        dog_age = 24 + 5*(humanYears-2)
    return [humanYears, cat_age, dog_age]

print(cat_dog(10))
