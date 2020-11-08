from django.db import models


# Create your models here.

class Cars(models.Model):
    GEAR_CHOICES = [
        (1, 'механика'),
        (2, 'автомат'),
        (3, 'робот')
    ]

    mark = models.CharField(max_length=255, verbose_name="mark")
    model = models.CharField(max_length=255, verbose_name="model")
    year = models.IntegerField(verbose_name="year")
    gear = models.SmallIntegerField(choices=GEAR_CHOICES, default=None, verbose_name='cars_gear')
    color = models.CharField(max_length=255, verbose_name="color")

    def __str__(self):
        return '{}-{}'.format(self.mark, self.model)

