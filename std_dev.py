"""Program takes two values, initializes and use the age to calcuate the standard deviation of the age data set."""

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
"""Determine the standard deviation(std dev) of the total population by taking age from list in the class. """

def std_dev(person_list):

    age_list = []
    for person in person_list:
        age = person.age
        age_list.append(age)
    print(age_list)

    N = len(age_list)

    mean = sum(age_list) / N

    total = 0
    for age in age_list:
        total = total + (age - mean) **2

    x = total / N
    std = x ** 0.5
    return std


# create 3 Person instances
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)

# test code
t = [p1, p2, p3]
print('Std Dev is:', std_dev(t))