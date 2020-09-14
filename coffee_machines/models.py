from django.db import models


class CoffeeMachines(models.Model):
    """Models class of the coffee machines"""
    COFFEE_MACHINE_SMALL = 'S'
    COFFEE_MACHINE_LARGE = 'L'
    ESPRESSO_MACHINE = 'E'

    BASE_CLASS = 'B'
    PREMIUM_CLASS = 'P'
    DELUXE_CLASS = 'D'

    TYPES_CHOICES = [
        (COFFEE_MACHINE_SMALL, "Small Coffee Machine"),
        (COFFEE_MACHINE_LARGE, "Large Coffee Machine"),
        (ESPRESSO_MACHINE, "Espresso Machine"),
    ]

    CLASS_CHOICES = [
        (BASE_CLASS, "Base Model"),
        (PREMIUM_CLASS, "Premium Model"),
        (DELUXE_CLASS, "Deluxe Model"),
    ]

    name = models.CharField(max_length=5, blank=False)

    machine_type = models.CharField(
        max_length=1,
        choices=TYPES_CHOICES,
        default=COFFEE_MACHINE_SMALL
    )

    machine_class = models.CharField(
        max_length=1,
        choices=CLASS_CHOICES,
        default=BASE_CLASS
    )

    water_line_compatiple = models.BooleanField(default=False)

    def __str__(self):
        return self.name
