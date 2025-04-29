from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
