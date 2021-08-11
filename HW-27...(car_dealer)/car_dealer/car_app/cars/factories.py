import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    engine_power = 120
    dealer_id = 1
    color_id = 2
    model_id = 2
    picture_id = 2
    number = 'AA 1234 AA'
    slug = '23FF'


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'green'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'skoda'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'sedan'
