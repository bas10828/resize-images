class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getName(self):
        return self.firstName + ' ' + self.lastName

p = Person('Chase', 'Rice')
p.career = 'Singer'
p.country = 'USA'

print('Name: ' + p.getName())
print('Career: ' + p.career)
print('Country: ' + p.country)

p2 = Person('Max', 'Graham')
p2.genres = ['Electronica', 'trance', 'tech house', 'techno']

print('Name: ' + p2.getName())
print('Genres: ', p2.genres)