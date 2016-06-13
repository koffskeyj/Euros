from django.db import models


class Nation(models.Model):
    name = models.CharField(max_length=20)
    Capital = models.CharField(max_length=20)
    government = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    population = models.IntegerField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.name