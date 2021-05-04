'''
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class

class Animals:
    """
    Parent class, should have eat, sleep
    """

class Animal1(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

'''
class Animals:
    def eat(self):
        print(f'{self.__class__.__name__} eating')

    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')

class Cat(Animals):
    def purrs(self):
        print(f'{__class__.__name__} purring')

class Dog(Animals):
    def make_sound(self):
        print(f'{self.__class__.__name__} bark')

class Chicken(Animals):
    def sit(self):
        print(f'{self.__class__.__name__} siting')

class Goose(Animals):
    def hiss(self):
        print(f'{self.__class__.__name__} hissing')

class Rabbit(Animals):
    def jump(self):
        print(f'{self.__class__.__name__} jumping')

cat = Cat()
dog = Dog()
chicken = Chicken()
goose = Goose()
rabbit = Rabbit()
cat.eat()
goose.sleep()
rabbit.sleep()
goose.eat()
chicken.sit()

print('______Instance of the Animals class________')
c = isinstance(cat, Animals)
d = isinstance(dog, Animals)
ch = isinstance(chicken, Animals)
g = isinstance(goose, Animals)
r = isinstance(rabbit, Animals)

print(f'Cat - {c}')
print(f'Dog - {d}')
print(f'Chicken - {ch}')
print(f'Goose - {g}')
print(f'Rabbit - {r}')

'''
1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.
 
 class Human:
    """
    Human class, should have eat, sleep, study, work
    """
 
 class Centaur(.. , ..):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'Human {self.name} eating')

    def sleep(self):
        print(f'Human {self.age} eating')

    def work(self):
        print(f'{self.name} working')

    def study(self):
        print(f'Human {self.name} studying')


class Centaur(Animals, Human):
    def sit(self):
        print(f'Centaur {self.name} siting')

    def info(self):
        print(f'Human {self.name} - {self.age}')

print('______Multiple inheritance_____')
centaur = Centaur('Sofia', 20)
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.sit()
centaur.info()
