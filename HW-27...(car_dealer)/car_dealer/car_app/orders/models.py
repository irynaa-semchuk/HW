from django.db import models
from phone_field import PhoneField


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    STATUS_OPEN = 'open'
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_OPEN, "Open"),
        (STATUS_IN_PROGRESS, "In-Progress"),
        (STATUS_COMPLETED, "Completed"),)

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
    )
    first_name = models.CharField(
        max_length=20
    )
    last_name = models.CharField(
        max_length=30
    )
    email = models.EmailField(
        max_length=20
    )
    phone = PhoneField(
        blank=True,
        help_text='Contact phone number'
    )
    message = models.TextField(
        max_length=200
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
