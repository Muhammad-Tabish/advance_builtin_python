class firsthundredgenerator:
    def __init__(self):
        self.number = 0
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

class anotheriterable:
    def __init__(self):
        self.cars = ['honda', 'toyata']
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]
for car in anotheriterable():
    print(len(car))
    print(list(car))

my_number = [x for x in [1, 2, 3, 4, 5]]
my_number_generator = (x for x in [1, 2, 3, 4, 5])

print(next(my_number_generator))

