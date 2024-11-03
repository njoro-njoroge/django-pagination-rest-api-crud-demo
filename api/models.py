from django.db import models


class Fruit(models.Model):
    fruit_name = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.fruit_name}, {self.stock}"
