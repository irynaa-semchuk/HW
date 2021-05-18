from person import Human
from houses import House, SmallHouse
from realtor import Realtor

if __name__ == '__main__':
    house1 = House(45, 15000)
    house2 = House(165, 60000)
    house3 = House(150, 20000)
    smallhouse = SmallHouse(10000)
    person = Human('Sia', 34, 15000)

    person.info()
    person.make_money()

    realtor = Realtor('Ira', 20, [house1, house2, house3, smallhouse])
    realtor.info_houses()
    realtor.give_discount(house1)
    print("----House 1-----")
    person.buy_house(house1, realtor)
    print('----House 2 ----')
    person.buy_house(house2, realtor)
    print("----House 3-----")
    person.buy_house(house3, realtor)
    print('-----SmallHouse-----')
    realtor.steal_money(person, smallhouse)

