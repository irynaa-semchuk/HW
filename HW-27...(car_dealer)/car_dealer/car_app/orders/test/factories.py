import factory

from car_app.cars.tests.factories import CarFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = factory.Sequence(lambda n: f'first name_{n}')
    last_name = factory.Sequence(lambda n: f'last name_{n}')
    email = factory.Sequence(lambda n: f'email{n}@mail.com')
    phone = '+380976785470'
    car = factory.SubFactory(CarFactory)
