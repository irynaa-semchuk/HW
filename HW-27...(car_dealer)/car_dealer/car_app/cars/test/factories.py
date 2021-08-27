import factory
from factory import fuzzy

from car_app.dealers.tests.factories import DealerFactory


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = factory.Sequence(lambda n: f'color_{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = factory.Sequence(lambda n: f'brand_{n}')


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = factory.Sequence(lambda n: f'property_{n}')


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Picture'

    url = factory.django.ImageField(from_path='test.jpg')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    name = factory.Sequence(lambda n: f'model_{n}')
    brand = factory.SubFactory(BrandFactory)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'AA 1234 AA'
    slug = factory.Sequence(lambda n: f'slug_{n}')
    model = factory.SubFactory(ModelFactory)
    engine_power = fuzzy.FuzzyInteger(30, 250)
    color = factory.SubFactory(ColorFactory)
    brand = factory.SubFactory(BrandFactory)
    dealer = factory.SubFactory(DealerFactory)
    picture = factory.SubFactory(PictureFactory)
