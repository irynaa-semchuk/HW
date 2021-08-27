from django.test import TestCase

from car_app.newsletters.models import NewsLetter


class TestNewsLetterModel(TestCase):
    def test_model(self):
        newsletter = NewsLetter.objects.create(
            email='test@gmail.com',
        )

        self.assertIsNotNone(newsletter.id)
        self.assertEqual(str(newsletter), 'test@gmail.com')
