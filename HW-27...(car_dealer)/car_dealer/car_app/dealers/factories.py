import factory


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'dealer_'
    email = 'dealer@gmail.com'
    city_id = 2
    user_id = 2


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'Ukraine'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'Lviv'
    country_id = 2


class NewsLetterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.NewsLetter'

    email = 'new_letter@mail.com'
