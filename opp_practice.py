'''There is a Person whose characteristics are:
1. Name
2. Age
3. Availability of money
4. Having your own home

Human can:
1. Provide information about yourself
2. Make money
3. Buy a house

There is also a House, the properties of which include:
1. Area
2. Cost

For Home you can:
1. Apply a purchase discount

e.g.: There is also a Small Typical House with a required area of 40m2.

*Realtor:
1. Name
2. Houses
3. Discount that he/she can give you.

*There is only one realtor who handles small houses you wanna buy. (Singleton)
Realtor is only one in your city and can:
1. Provide information about all the Houses
2. Give a discount
3. Steal your money with 10% chance

'''
from abc import ABC, abstractmethod
import random


class Person(ABC):
    def __init__(self, name, age, money, house: list = []):
        self.name = name
        self.age = age
        self.available_of_money = money
        self.own_home = house

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Human(Person, ABC):
    def __init__(self, name, age, money, house: list = []):
        super().__init__(name, age, money, house)
        self.salary = random.randint(8000, 12000)

    def info(self):
        print(f'My name {self.name}. I am {self.age} years old')

    def make_money(self):
        self.available_of_money += self.salary

    def buy_house(self, house, realtor):
        if house.area >= 300:
            print('The house is too large')
        elif house.cost >= self.available_of_money:
            print(f'Not enough money to buy from a customer{self.name} ')
        elif realtor.steal_money() <= 20:
            print(f'Realtor {realtor.name} steal money from {self.name}')
            self.available_of_money -= house.cost
        else:
            self.available_of_money -= house.cost
            print(f'Hooray you bought a house')

        return self.own_home.append(house)


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_disc(self, disc):
        self.cost -= (self.cost * disc)
        return self.cost


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses: list = []):
        self.name = name
        self.discount = discount
        self.houses = houses

    def info_houses(self):
        if self.houses:
            print(f'I realtor {self.name} and provide information about all the houses')
            for house in self.houses:
                print(f' There is a nice house: \t{house}')
        else:
            print('We do not have a moment for you at hoses')
        return self.houses

    def give_discount(self):
        if self.houses:
            print(f'Realtor {self.name} can give a discount of {self.discount}%')
            return self.discount
        else:
            print(f'There is no such house in the list')

    def steal_money(self):
        return random.randrange(0, 101)

if __name__ == '__main__':
    house1 = House(67, 30000)
    house2 = House(98, 50000)
    house3 = House(300, 60000)
    realtor = Realtor('Ira', 20, [house1, house2, house3])
    realtor.info_houses()
    realtor.give_discount()
    realtor.steal_money()
    person = Human('Sia', 26, 40000)
    person.info()
    person.make_money()
    person.buy_house(house2, realtor)
    person.buy_house(house3, realtor)
    person.buy_house(house1, realtor)