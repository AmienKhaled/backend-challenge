from django.db import models


class CoffeePods(models.Model):
    """Models class of the coffee pods"""

    COFFEE_POD_SMALL = 'S'
    COFFEE_POD_LARGE = 'L'
    ESPRESSO_POD = 'E'

    COFFEE_FLAVOR_VANILLA = 'VAN'
    COFFEE_FLAVOR_CARAMEL = 'CAR'
    COFFEE_FLAVOR_PSL = 'PSL'
    COFFEE_FLAVOR_MOCHA = 'MOC'
    COFFEE_FLAVOR_HAZELNUT = 'HAZ'

    PACK_SIZE_1 = '1'
    PACK_SIZE_3 = '36'
    PACK_SIZE_5 = '60'
    PACK_SIZE_7 = '84'

    TYPES_CHOICES = [
        (COFFEE_POD_SMALL, "Small Coffee Pod"),
        (COFFEE_POD_LARGE, "Large Coffee Pod"),
        (ESPRESSO_POD, "Espresso Pod"),
    ]

    FLAVOR_CHOICES = [
        (COFFEE_FLAVOR_VANILLA, 'Vanilla'),
        (COFFEE_FLAVOR_CARAMEL, 'Caramel'),
        (COFFEE_FLAVOR_PSL, 'PSL'),
        (COFFEE_FLAVOR_MOCHA, 'Mocha'),
        (COFFEE_FLAVOR_HAZELNUT, 'Hazelnut'),
    ]

    PACK_SIZE = [
        (PACK_SIZE_1, '1'),
        (PACK_SIZE_3, '3'),
        (PACK_SIZE_5, '5'),
        (PACK_SIZE_7, '7'),
    ]

    name = models.CharField(max_length=5, blank=False)

    pod_type = models.CharField(
        max_length=1,
        choices=TYPES_CHOICES,
        default=COFFEE_POD_SMALL
    )

    flavors = models.CharField(
        max_length=3,
        choices=FLAVOR_CHOICES,
        default=COFFEE_FLAVOR_VANILLA
    )

    pack_size = models.CharField(
        max_length=2,
        choices=PACK_SIZE,
        default=PACK_SIZE_1
    )

    def __str__(self):
        return self.name
