from django.test import TestCase

from car_app.cars.tests.factories import CarFactory
from car_app.orders.models import Order


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Ira',
            last_name='Sem',
            email='sem@gmail.com',
            phone='+380934565890',
            message='text',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Ira Sem')
        self.assertEqual(order.email, 'sem@gmail.com')
        self.assertEqual(order.phone, '+380934565890')
        self.assertEqual(order.message, 'text')
