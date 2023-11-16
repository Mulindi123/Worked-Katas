# Generate odd numbers

def odds_generator(limit):
    n = 1
    while n <= limit:
        yield n
        n += 2

generator = odds_generator(110)
for n in generator:
    print(n)
