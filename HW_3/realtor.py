import random


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
        if self.houses is not []:
            print(f'I realtor {self.name} and provide information about all the houses')
            print(f'There are some beautiful houses:')
            for house in self.houses:
                print(f'- \t{house}')
        else:
            print('We do not have a moment for you at hoses')
        return self.houses

    def give_discount(self, house):
        if self.houses is not []:
            print(f'\nRealtor {self.name} can give a discount of {house.apply_disc(self.discount)}')
            return house.apply_disc(self.discount)
        else:
            print(f'There is no such house in the list')

    def steal_money(self, human, house):
        chance = random.randrange(0, 11)
        if chance >= 10:
            human.available_of_money = human.available_of_money - house.cost
            print(f'Realtor {self.name} steal money. Now {human.name} has {human.available_of_money} money')
            return chance
        else:
            print('The theft failed')
