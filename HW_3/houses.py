class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def __str__(self):
        return f'House with a price of {self.cost}'

    def apply_disc(self, disc):
        self.cost -= (self.cost * disc)
        return self.cost


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(area, cost)

    def __str__(self):
        return f'House with a price of {self.cost}'
