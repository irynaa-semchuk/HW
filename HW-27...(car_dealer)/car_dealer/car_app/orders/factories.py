import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Ira'
    last_name = 'Semchuk'
    email = 'sem@test.com'
    phone = '+38095580197'
    car_id = 1