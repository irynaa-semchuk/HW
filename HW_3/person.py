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
    def buy_house(self, house, realtor):
        raise NotImplementedError


class Human(Person):
    def __init__(self, name, age, money, house: list = []):
        super().__init__(name, age, money, house)
        self.salary = random.randint(8000, 12000)

    def info(self):
        print(f'My name {self.name}. I am {self.age} years old.')

    def make_money(self):
        self.available_of_money += self.salary
        print(f'Availability of money {self.available_of_money}')

    def buy_house(self, house, realtor):
        if self.available_of_money <= house.cost:
            print(f'{self.name} dont have money for buy this house')
        elif house.area >= 300:
            print('The house is too large')
        elif realtor.steal_money(self, house) == 10:
            print(f'Realtor {realtor.name} steal money from {self.name}')
        else:
            print(f'{self.name} buy house in {house.area}\n')
            realtor.houses.remove(house)
            self.available_of_money -= house.cost
            self.own_home.append(house)

        return 'The house was bought'
