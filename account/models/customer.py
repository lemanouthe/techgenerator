from django.db import models
from .user import User


class Customer(User):
    GENDER_CHOICES = (
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
    )
    phone = models.CharField(max_length=16)
    phone2 = models.CharField(max_length=16)
    addresse = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default="Mr")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer's"
